"""Tests unitarios de WikipediaScraper (red mockeada)."""

from unittest.mock import patch, Mock

import pytest

from src.scraper import WikipediaScraper, ArticuloNoEncontrado


# HTML falso que imita la estructura real de Wikipedia.
# A proposito: un parrafo vacio (debe ignorarse) y 6 con texto (solo deben
# devolverse los 5 primeros).
HTML_FALSO = """
<html>
  <body>
    <h1 id="firstHeading">Ada Lovelace</h1>
    <div class="mw-parser-output">
      <p></p>
      <p>Parrafo 1.</p>
      <p>Parrafo 2.</p>
      <p>Parrafo 3.</p>
      <p>Parrafo 4.</p>
      <p>Parrafo 5.</p>
      <p>Parrafo 6 (no deberia aparecer).</p>
    </div>
  </body>
</html>
"""


def test_buscar_articulo_devuelve_titulo_y_5_parrafos():
    # Arrange: respuesta falsa con codigo 200 y nuestro HTML
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.text = HTML_FALSO

    with patch("src.scraper.requests.get", return_value=respuesta_falsa):
        scraper = WikipediaScraper()

        # Act
        resultado = scraper.buscar_articulo("Ada Lovelace")

    # Assert
    assert resultado["titulo"] == "Ada Lovelace"
    assert len(resultado["parrafos"]) == 5
    assert resultado["parrafos"][0] == "Parrafo 1."
    assert "Parrafo 6" not in resultado["parrafos"]


def test_buscar_articulo_inexistente_lanza_excepcion():
    # Arrange: respuesta falsa con codigo 404
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 404

    with patch("src.scraper.requests.get", return_value=respuesta_falsa):
        scraper = WikipediaScraper()

        # Act + Assert
        with pytest.raises(ArticuloNoEncontrado):
            scraper.buscar_articulo("tema_que_no_existe_123")


# HTML de una pagina que existe (200) pero cuyos parrafos estan vacios:
# el bucle recorre los <p> sin acumular nada y debe lanzar ArticuloNoEncontrado.
HTML_SIN_CONTENIDO = """
<html>
  <body>
    <h1 id="firstHeading">Pagina vacia</h1>
    <div class="mw-parser-output">
      <p></p>
      <p>   </p>
    </div>
  </body>
</html>
"""


# HTML 200 pero sin la estructura de un articulo (sin h1#firstHeading ni
# div.mw-parser-output): debe lanzar ArticuloNoEncontrado, no un AttributeError.
HTML_ESTRUCTURA_RARA = "<html><body><p>pagina sin estructura de wikipedia</p></body></html>"


def test_buscar_articulo_estructura_inesperada_lanza_excepcion():
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.text = HTML_ESTRUCTURA_RARA

    with patch("src.scraper.requests.get", return_value=respuesta_falsa):
        scraper = WikipediaScraper()

        with pytest.raises(ArticuloNoEncontrado):
            scraper.buscar_articulo("rara")


def test_buscar_articulo_sin_parrafos_lanza_excepcion():
    # Arrange: respuesta 200 pero sin contenido legible
    respuesta_falsa = Mock()
    respuesta_falsa.status_code = 200
    respuesta_falsa.text = HTML_SIN_CONTENIDO

    with patch("src.scraper.requests.get", return_value=respuesta_falsa):
        scraper = WikipediaScraper()

        # Act + Assert
        with pytest.raises(ArticuloNoEncontrado):
            scraper.buscar_articulo("Pagina vacia")
