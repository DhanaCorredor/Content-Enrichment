"""Etapa 2: enriquecimiento del texto con la IA (Groq vía SDK de OpenAI)."""


class Enricher:
    """Mejora un texto usando Groq (modelo llama-3.3-70b-versatile).

    Responsabilidad unica: hablar con la IA para enriquecer. Se usa el SDK
    oficial de openai apuntando al base_url de Groq; la clave se lee de .env
    como GROQ_API_KEY (nunca hardcodear).
    """

    MODELO = "llama-3.3-70b-versatile"

    def __init__(self, client) -> None:
        # 'client' es una instancia ya configurada de openai.OpenAI apuntando
        # al base_url de Groq, inyectada para poder mockearla en los tests.
        self.client = client

    def enriquecer(self, texto: str) -> str:
        """Devuelve el texto enriquecido por la IA."""
        raise NotImplementedError
