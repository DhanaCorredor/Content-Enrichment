"""Tests unitarios de Translator (deep-translator mockeado)."""

from unittest.mock import patch

import pytest
from deep_translator.exceptions import RequestError

from src.translator import Translator, TraduccionError


def test_traducir_devuelve_texto_en_idioma_destino():
    # Arrange: mockeamos GoogleTranslator para no salir a internet.
    with patch("src.translator.GoogleTranslator") as MockGT:
        instancia = MockGT.return_value
        instancia.translate_batch.return_value = ["Hello", "World"]

        translator = Translator("en")

        # Act
        resultado = translator.traducir("Hola\n\nMundo")

    # Assert
    assert resultado == "Hello\n\nWorld"
    # Se construyo con el idioma destino correcto y deteccion automatica.
    MockGT.assert_called_once_with(source="auto", target="en")
    # Se tradujo parrafo a parrafo (la lista, no el texto entero).
    instancia.translate_batch.assert_called_once_with(["Hola", "Mundo"])


def test_traducir_error_lanza_excepcion():
    # Arrange: la libreria lanza un error de red al traducir.
    with patch("src.translator.GoogleTranslator") as MockGT:
        MockGT.return_value.translate_batch.side_effect = RequestError()

        translator = Translator("en")

        # Act + Assert
        with pytest.raises(TraduccionError):
            translator.traducir("Hola")
