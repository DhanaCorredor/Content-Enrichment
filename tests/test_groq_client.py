"""Tests de la fabrica del cliente de Groq."""

from src.groq_client import crear_cliente_groq, GROQ_BASE_URL


def test_crear_cliente_groq_configura_url_y_clave():
    client = crear_cliente_groq("clave-test")

    assert str(client.base_url).startswith(GROQ_BASE_URL)
    assert client.api_key == "clave-test"
