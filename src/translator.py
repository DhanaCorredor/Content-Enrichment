"""Etapa 3: traduccion del contenido con deep-translator."""


class Translator:
    """Traduce texto al idioma destino usando deep-translator (Google).

    Responsabilidad unica: traducir. No usa OpenAI. deep-translator no
    necesita clave de API.
    """

    def __init__(self, idioma_destino: str) -> None:
        self.idioma_destino = idioma_destino

    def traducir(self, texto: str) -> str:
        """Devuelve el texto traducido al idioma destino."""
        raise NotImplementedError
