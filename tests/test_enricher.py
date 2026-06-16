"""Tests unitarios de Enricher (cliente de IA Groq, vía SDK de OpenAI, mockeado)."""

from unittest.mock import Mock

import pytest
from openai import OpenAIError

from src.enricher import Enricher, EnriquecimientoError


def test_enriquecer_devuelve_texto_mejorado():
    client_falso = Mock()
    mensaje = Mock()
    mensaje.content = "Texto mejorado."
    opcion = Mock()
    opcion.message = mensaje
    client_falso.chat.completions.create.return_value = Mock(choices=[opcion])

    enricher = Enricher(client_falso)

    resultado = enricher.enriquecer("texto crudo")

    assert resultado == "Texto mejorado."
    _, kwargs = client_falso.chat.completions.create.call_args
    assert kwargs["model"] == Enricher.MODELO
    assert kwargs["messages"][1]["content"] == "texto crudo"


def test_enriquecer_error_de_api_lanza_excepcion():
    client_falso = Mock()
    client_falso.chat.completions.create.side_effect = OpenAIError("fallo de API")

    enricher = Enricher(client_falso)

    with pytest.raises(EnriquecimientoError):
        enricher.enriquecer("texto crudo")
