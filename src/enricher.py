"""Etapa 2: enriquecimiento del texto con la IA (Groq vía SDK de OpenAI)."""

from openai import OpenAIError


class EnriquecimientoError(Exception):
    """Se lanza cuando la IA (Groq) falla al enriquecer el texto."""


class Enricher:
    """Mejora un texto usando Groq (modelo llama-3.3-70b-versatile).

    Responsabilidad unica: hablar con la IA para enriquecer. Se usa el SDK
    oficial de openai apuntando al base_url de Groq; la clave se lee de .env
    como GROQ_API_KEY (nunca hardcodear).
    """

    MODELO = "llama-3.3-70b-versatile"

    SYSTEM_PROMPT = (
        "Eres un editor profesional en espanol. Mejora la redaccion del texto "
        "que recibas: hazlo mas claro, fluido y bien estructurado, corrigiendo "
        "gramatica y estilo. No cambies el idioma (responde siempre en espanol), "
        "no anadas informacion nueva ni inventes datos, y conserva el significado "
        "original. Devuelve unicamente el texto mejorado, sin comentarios ni "
        "explicaciones."
    )

    def __init__(self, client) -> None:
        self.client = client

    def enriquecer(self, texto: str) -> str:
        """Devuelve el texto enriquecido por la IA."""
        try:
            respuesta = self.client.chat.completions.create(
                model=self.MODELO,
                messages=[
                    {"role": "system", "content": self.SYSTEM_PROMPT},
                    {"role": "user", "content": texto},
                ],
            )
        except OpenAIError as error:
            raise EnriquecimientoError(
                f"No se pudo enriquecer el texto con la IA: {error}"
            ) from error

        return respuesta.choices[0].message.content
