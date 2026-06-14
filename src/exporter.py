"""Etapa 4: exportacion del resultado a .txt o .pdf."""

import os
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


class FormatoNoSoportado(Exception):
    """Se lanza cuando el formato pedido no es 'txt' ni 'pdf'."""


class Exporter:
    """Guarda el contenido en .txt o .pdf.

    Responsabilidad unica: persistir el resultado en disco. El PDF se genera
    con reportlab usando Flowables (SimpleDocTemplate + story), nunca con
    posicionamiento manual del canvas (evita solapamientos).
    """

    FORMATOS = ("txt", "pdf")

    def __init__(self, carpeta_salida: str = "output") -> None:
        self.carpeta_salida = carpeta_salida

    def exportar(self, contenido: dict, nombre: str, formato: str) -> str:
        """Guarda el archivo y devuelve la ruta final.

        'formato' debe estar en {'txt', 'pdf'}; si no, lanza FormatoNoSoportado.
        """
        if formato not in self.FORMATOS:
            raise FormatoNoSoportado(
                f"Formato '{formato}' no soportado. Usa uno de: {self.FORMATOS}."
            )

        os.makedirs(self.carpeta_salida, exist_ok=True)
        ruta = os.path.join(self.carpeta_salida, f"{nombre}.{formato}")

        if formato == "txt":
            self._exportar_txt(contenido, ruta)
        else:
            self._exportar_pdf(contenido, ruta)

        return ruta

    def _exportar_txt(self, contenido: dict, ruta: str) -> None:
        titulo = contenido["titulo"]
        lineas = [titulo, "=" * len(titulo), ""]
        for encabezado, cuerpo in contenido["secciones"]:
            lineas.append(encabezado)
            lineas.append("-" * len(encabezado))
            lineas.append(cuerpo)
            lineas.append("")

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write("\n".join(lineas))

    def _exportar_pdf(self, contenido: dict, ruta: str) -> None:
        estilos = getSampleStyleSheet()
        documento = SimpleDocTemplate(ruta, pagesize=A4)

        # 'story' es la lista de Flowables; reportlab los coloca y pagina solo.
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
    ruta_txt = Exporter().exportar(contenido_demo, "demo", "txt")
    ruta_pdf = Exporter().exportar(contenido_demo, "demo", "pdf")
    print(f"TXT generado en: {ruta_txt}")
    print(f"PDF generado en: {ruta_pdf}")
