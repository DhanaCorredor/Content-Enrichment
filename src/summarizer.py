"""Extra: generacion de resumenes con la IA (Groq vía SDK de OpenAI)."""


class Summarizer:
    """Genera un resumen del contenido enriquecido usando Groq.

    Responsabilidad unica: resumir. Usa el SDK de openai apuntando a Groq.
    """

    MODELO = "llama-3.3-70b-versatile"

    def __init__(self, client) -> None:
        self.client = client

    def resumir(self, texto: str) -> str:
        """Devuelve un resumen breve del texto."""
        raise NotImplementedError
