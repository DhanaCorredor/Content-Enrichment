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
    # Arrange
    exporter = Exporter(carpeta_salida=str(tmp_path))

    # Act
    ruta = exporter.exportar(CONTENIDO, "informe", "pdf")

    # Assert: el archivo existe y empieza por la firma de un PDF (%PDF)
    archivo = tmp_path / "informe.pdf"
    assert ruta.endswith("informe.pdf")
    assert archivo.exists()
    assert archivo.read_bytes().startswith(b"%PDF")


def test_exportar_formato_invalido_lanza_excepcion(tmp_path):
    # Arrange
    exporter = Exporter(carpeta_salida=str(tmp_path))

    # Act + Assert: 'txt' ya no esta soportado (solo PDF)
    with pytest.raises(FormatoNoSoportado):
        exporter.exportar(CONTENIDO, "informe", "txt")
