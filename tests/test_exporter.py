"""Tests unitarios de Exporter (.txt / .pdf)."""

import pytest

from src.exporter import Exporter, FormatoNoSoportado


@pytest.mark.skip(reason="pendiente: HU-5")
def test_exportar_txt_crea_archivo():
    raise NotImplementedError


@pytest.mark.skip(reason="pendiente: HU-5")
def test_exportar_formato_invalido_lanza_excepcion():
    raise NotImplementedError
