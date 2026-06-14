"""Etapa 3: traduccion del contenido con deep-translator."""

from deep_translator import GoogleTranslator
from deep_translator.exceptions import (
    BaseError,
    RequestError,
    ServerException,
    TooManyRequests,
)

# deep-translator no expone una unica excepcion madre: las de red y limite
# heredan directamente de Exception. Agrupamos las relevantes para capturarlas
# sin recurrir a un 'except Exception' generico.
ERRORES_TRADUCCION = (BaseError, RequestError, ServerException, TooManyRequests)


class TraduccionError(Exception):
    """Se lanza cuando deep-translator falla al traducir el texto."""


class Translator:
    """Traduce texto al idioma destino usando deep-translator (Google).

    Responsabilidad unica: traducir. No usa la IA (Groq). deep-translator no
    necesita clave de API.
    """

    def __init__(self, idioma_destino: str) -> None:
        self.idioma_destino = idioma_destino

    def traducir(self, texto: str) -> str:
        """Devuelve el texto traducido al idioma destino.

        Traduce parrafo a parrafo (separados por lineas en blanco) para
        respetar el limite de ~5000 caracteres por peticion de Google y
        conservar la estructura del texto.
        """
        parrafos = texto.split("\n\n")
        traductor = GoogleTranslator(source="auto", target=self.idioma_destino)

        try:
            traducidos = traductor.translate_batch(parrafos)
        except ERRORES_TRADUCCION as error:
            raise TraduccionError(f"No se pudo traducir el texto: {error}") from error

        return "\n\n".join(traducidos)


if __name__ == "__main__":  # pragma: no cover
    try:
        from src.scraper import WikipediaScraper
    except ModuleNotFoundError:
        from scraper import WikipediaScraper

    # Etapa 1: texto crudo de Wikipedia (sin gastar Groq)
    articulo = WikipediaScraper(idioma="es").buscar_articulo("Marketing")
    texto = "\n\n".join(articulo["parrafos"])

    # Etapa 3: traducir al ingles
    traducido = Translator("en").traducir(texto)

    print("===== ORIGINAL (es) =====\n")
    print(texto)
    print("\n===== TRADUCIDO (en) =====\n")
    print(traducido)
