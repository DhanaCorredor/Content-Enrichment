"""Etapa 2: enriquecimiento del texto con la API de OpenAI."""


class Enricher:
    """Mejora un texto usando OpenAI (modelo gpt-4o-mini).

    Responsabilidad unica: hablar con OpenAI para enriquecer. La clave de API
    se lee de .env (nunca hardcodear).
    """

    MODELO = "gpt-4o-mini"

    def __init__(self, client) -> None:
        # 'client' es una instancia ya configurada de openai.OpenAI,
        # inyectada para poder mockearla en los tests.
        self.client = client

    def enriquecer(self, texto: str) -> str:
        """Devuelve el texto enriquecido por la IA."""
        raise NotImplementedError
