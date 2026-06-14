"""Tests unitarios de Enricher (cliente de IA Groq, vía SDK de OpenAI, mockeado)."""

from unittest.mock import Mock

import pytest
from openai import OpenAIError

from src.enricher import Enricher, EnriquecimientoError


def test_enriquecer_devuelve_texto_mejorado():
    # Arrange: cliente falso que imita la respuesta del SDK de OpenAI/Groq.
    # La estructura real es: respuesta.choices[0].message.content
    client_falso = Mock()
    mensaje = Mock()
    mensaje.content = "Texto mejorado."
    opcion = Mock()
    opcion.message = mensaje
    client_falso.chat.completions.create.return_value = Mock(choices=[opcion])

    enricher = Enricher(client_falso)

    # Act
    resultado = enricher.enriquecer("texto crudo")

    # Assert
    assert resultado == "Texto mejorado."
    # Comprobamos que se llamo al modelo correcto y con el texto del usuario.
    _, kwargs = client_falso.chat.completions.create.call_args
    assert kwargs["model"] == Enricher.MODELO
    assert kwargs["messages"][1]["content"] == "texto crudo"


def test_enriquecer_error_de_api_lanza_excepcion():
    # Arrange: el cliente lanza un error del SDK al llamar a la IA.
    client_falso = Mock()
    client_falso.chat.completions.create.side_effect = OpenAIError("fallo de API")

    enricher = Enricher(client_falso)

    # Act + Assert
    with pytest.raises(EnriquecimientoError):
        enricher.enriquecer("texto crudo")
