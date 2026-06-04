"""Etapa 1: scraping de Wikipedia."""


class ArticuloNoEncontrado(Exception):
    """Se lanza cuando Wikipedia no devuelve un articulo para el tema dado."""


class WikipediaScraper:
    """Busca un tema en Wikipedia y extrae titulo + primeros 5 parrafos.

    Responsabilidad unica: obtener contenido crudo de Wikipedia. No sabe nada
    de IA, traduccion ni exportacion.
    """

    MAX_PARRAFOS = 5
    USER_AGENT = "ContentEnricher/1.0 (proyecto educativo FemCoders)"

    def __init__(self, idioma: str = "es") -> None:
        self.idioma = idioma

    def buscar_articulo(self, tema: str) -> dict:
        """Devuelve {'titulo': str, 'parrafos': [str, ...]}.

        Lanza ArticuloNoEncontrado si el tema no existe en Wikipedia.
        """
        raise NotImplementedError
