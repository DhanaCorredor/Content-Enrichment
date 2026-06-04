"""Tests unitarios de WikipediaScraper (red mockeada)."""

import pytest

from src.scraper import WikipediaScraper, ArticuloNoEncontrado


@pytest.mark.skip(reason="pendiente: HU-2")
def test_buscar_articulo_devuelve_titulo_y_5_parrafos():
    raise NotImplementedError


@pytest.mark.skip(reason="pendiente: HU-2")
def test_buscar_articulo_inexistente_lanza_excepcion():
    raise NotImplementedError
