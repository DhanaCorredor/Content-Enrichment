"""Etapa 4: exportacion del resultado a .pdf."""

import os
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


class FormatoNoSoportado(Exception):
    """Se lanza cuando el formato pedido no es 'pdf'."""


class Exporter:
    """Guarda el contenido en .pdf.

    Responsabilidad unica: persistir el resultado en disco. El PDF se genera
    con reportlab usando Flowables (SimpleDocTemplate + story), nunca con
    posicionamiento manual del canvas (evita solapamientos).
    """

    FORMATOS = ("pdf",)

    def __init__(self, carpeta_salida: str = "output") -> None:
        self.carpeta_salida = carpeta_salida

    def exportar(self, contenido: dict, nombre: str, formato: str) -> str:
        """Guarda el archivo y devuelve la ruta final.

        'formato' debe estar en {'pdf'}; si no, lanza FormatoNoSoportado.
        """
        if formato not in self.FORMATOS:
            raise FormatoNoSoportado(
                f"Formato '{formato}' no soportado. Usa uno de: {self.FORMATOS}."
            )

        os.makedirs(self.carpeta_salida, exist_ok=True)
        ruta = os.path.join(self.carpeta_salida, f"{nombre}.{formato}")

        self._exportar_pdf(contenido, ruta)

        return ruta

    def _exportar_pdf(self, contenido: dict, ruta: str) -> None:
        estilos = getSampleStyleSheet()
        documento = SimpleDocTemplate(ruta, pagesize=A4)

        story = [
            Paragraph(escape(contenido["titulo"]), estilos["Title"]),
            Spacer(1, 0.5 * cm),
        ]
        for encabezado, cuerpo in contenido["secciones"]:
            story.append(Paragraph(escape(encabezado), estilos["Heading2"]))
            for parrafo in cuerpo.split("\n\n"):
                story.append(Paragraph(escape(parrafo), estilos["BodyText"]))
            story.append(Spacer(1, 0.4 * cm))

        documento.build(story)


if __name__ == "__main__":  # pragma: no cover
    contenido_demo = {
        "titulo": "Ada Lovelace",
        "secciones": [
            ("Original", "Texto original de ejemplo.\n\nSegundo parrafo del original."),
            ("Enriquecido", "Texto enriquecido de ejemplo por la IA."),
            ("Traducido", "Translated sample text."),
        ],
    }
    ruta_pdf = Exporter().exportar(contenido_demo, "demo", "pdf")
    print(f"PDF generado en: {ruta_pdf}")
