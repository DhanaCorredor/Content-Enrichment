"""Tests de integracion del Pipeline (todas las etapas mockeadas)."""

from unittest.mock import Mock

from src.pipeline import Pipeline


def _stages():
    """Crea las 4 etapas mockeadas con respuestas controladas."""
    scraper = Mock()
    scraper.buscar_articulo.return_value = {
        "titulo": "Ada Lovelace",
        "parrafos": ["P1", "P2"],
    }
    enricher = Mock()
    enricher.enriquecer.return_value = "enriquecido"
    translator = Mock()
    translator.traducir.return_value = "traducido"
    exporter = Mock()
    exporter.exportar.return_value = "output/informe.pdf"
    return scraper, enricher, translator, exporter


def test_ejecutar_flujo_completo_devuelve_ruta():
    scraper, enricher, translator, exporter = _stages()

    pipeline = Pipeline(scraper, enricher, translator, exporter)
    ruta = pipeline.ejecutar("Ada Lovelace", "en", "informe", "pdf")

    # Devuelve la ruta del exporter
    assert ruta == "output/informe.pdf"
    # El flujo de datos encadena correctamente cada etapa
    enricher.enriquecer.assert_called_once_with("P1\n\nP2")
    translator.traducir.assert_called_once_with("enriquecido", "en")
    # El exporter recibe el contenido bien armado
    contenido, nombre, formato = exporter.exportar.call_args.args
    assert nombre == "informe"
    assert formato == "pdf"
    assert contenido["titulo"] == "Ada Lovelace"
    assert ("Traducido", "traducido") in contenido["secciones"]
    # Sin Summarizer no hay seccion de resumen
    assert all(enc != "Resumen" for enc, _ in contenido["secciones"])


def test_ejecutar_con_summarizer_incluye_resumen():
    scraper, enricher, translator, exporter = _stages()
    summarizer = Mock()
    summarizer.resumir.return_value = "resumen breve"

    pipeline = Pipeline(scraper, enricher, translator, exporter, summarizer)
    pipeline.ejecutar("Ada Lovelace", "en", "informe", "pdf")

    # El resumen se genera a partir del texto enriquecido
    summarizer.resumir.assert_called_once_with("enriquecido")
    contenido = exporter.exportar.call_args.args[0]
    assert ("Resumen", "resumen breve") in contenido["secciones"]
