"""Tests unitarios de Exporter (.txt / .pdf)."""

import pytest

from src.exporter import Exporter, FormatoNoSoportado


CONTENIDO = {
    "titulo": "Ada Lovelace",
    "secciones": [
        ("Original", "Primer parrafo.\n\nSegundo parrafo."),
        ("Traducido", "First paragraph.\n\nSecond paragraph."),
    ],
}


def test_exportar_pdf_crea_archivo(tmp_path):
    exporter = Exporter(carpeta_salida=str(tmp_path))

    ruta = exporter.exportar(CONTENIDO, "informe", "pdf")

    archivo = tmp_path / "informe.pdf"
    assert ruta.endswith("informe.pdf")
    assert archivo.exists()
    assert archivo.read_bytes().startswith(b"%PDF")


def test_exportar_formato_invalido_lanza_excepcion(tmp_path):
    exporter = Exporter(carpeta_salida=str(tmp_path))

    with pytest.raises(FormatoNoSoportado):
        exporter.exportar(CONTENIDO, "informe", "txt")
