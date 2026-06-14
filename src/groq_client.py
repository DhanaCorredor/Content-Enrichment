"""Fabrica del cliente de IA: SDK oficial de OpenAI apuntado a Groq.

Centraliza la construccion del cliente para no repetir el base_url ni la
configuracion en cada sitio que lo necesita (DRY).
"""

from openai import OpenAI

GROQ_BASE_URL = "https://api.groq.com/openai/v1"


def crear_cliente_groq(api_key: str) -> OpenAI:
    """Devuelve un cliente OpenAI configurado para el backend de Groq."""
    return OpenAI(base_url=GROQ_BASE_URL, api_key=api_key)
