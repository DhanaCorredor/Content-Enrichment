"""Etapa 4: exportacion del resultado a .txt o .pdf."""


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
        raise NotImplementedError
