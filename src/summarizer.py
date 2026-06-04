"""Extra: generacion de resumenes con OpenAI."""


class Summarizer:
    """Genera un resumen del contenido enriquecido usando OpenAI.

    Responsabilidad unica: resumir.
    """

    MODELO = "gpt-4o-mini"

    def __init__(self, client) -> None:
        self.client = client

    def resumir(self, texto: str) -> str:
        """Devuelve un resumen breve del texto."""
        raise NotImplementedError
