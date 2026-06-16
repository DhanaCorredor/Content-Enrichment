"""Tests unitarios de Translator (deep-translator mockeado)."""

from unittest.mock import patch

import pytest
from deep_translator.exceptions import RequestError

from src.translator import Translator, TraduccionError


def test_traducir_devuelve_texto_en_idioma_destino():
    with patch("src.translator.GoogleTranslator") as MockGT:
        instancia = MockGT.return_value
        instancia.translate_batch.return_value = ["Hello", "World"]

        translator = Translator()

        resultado = translator.traducir("Hola\n\nMundo", "en")

    assert resultado == "Hello\n\nWorld"
    MockGT.assert_called_once_with(source="auto", target="en")
    instancia.translate_batch.assert_called_once_with(["Hola", "Mundo"])


def test_traducir_error_lanza_excepcion():
    with patch("src.translator.GoogleTranslator") as MockGT:
        MockGT.return_value.translate_batch.side_effect = RequestError()

        translator = Translator()

        with pytest.raises(TraduccionError):
            translator.traducir("Hola", "en")
