"""Fixtures compartidas para los tests.

Las llamadas de red/API (Wikipedia, OpenAI, traduccion) se mockean siempre:
los tests no deben tocar internet ni gastar tokens.
"""

import pytest


@pytest.fixture
def articulo_ejemplo() -> dict:
    return {
        "titulo": "Ada Lovelace",
        "parrafos": ["Parrafo 1.", "Parrafo 2.", "Parrafo 3.", "Parrafo 4.", "Parrafo 5."],
    }
