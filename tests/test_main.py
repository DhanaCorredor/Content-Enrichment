"""Tests del punto de entrada CLI (main)."""

from unittest.mock import patch, Mock

from src import main as main_module
from src.scraper import ArticuloNoEncontrado
from src.enricher import EnriquecimientoError
from src.translator import TraduccionError


def _ejecutar_main(inputs, ejecutar_resultado=None, ejecutar_error=None, con_clave=True):
    """Lanza main() con todo mockeado.

    'inputs' son las respuestas simuladas del teclado; 'ejecutar_resultado' o
    'ejecutar_error' controlan que devuelve/lanza pipeline.ejecutar().
    """
    pipeline_falso = Mock()
    if ejecutar_error is not None:
        pipeline_falso.ejecutar.side_effect = ejecutar_error
    else:
        pipeline_falso.ejecutar.return_value = ejecutar_resultado

    entorno = {"GROQ_API_KEY": "clave-test"} if con_clave else {}

    with patch("src.main.load_dotenv"), \
         patch("src.main.crear_cliente_groq"), \
         patch("src.main.Pipeline", return_value=pipeline_falso), \
         patch.dict("src.main.os.environ", entorno, clear=True), \
         patch("builtins.input", side_effect=inputs):
        main_module.main()

    return pipeline_falso


def test_main_flujo_completo(capsys):
    inputs = ["", "Marketing", "en", "informe"]
    pipeline = _ejecutar_main(inputs, ejecutar_resultado="output/informe.pdf")

    pipeline.ejecutar.assert_called_once_with("Marketing", "en", "informe", "pdf")
    salida = capsys.readouterr().out
    assert "output/informe.pdf" in salida
    assert "no puede estar vacio" in salida


def test_main_sin_clave_avisa(capsys):
    pipeline = _ejecutar_main(["Marketing", "en", "informe"], con_clave=False)

    pipeline.ejecutar.assert_not_called()
    assert "GROQ_API_KEY" in capsys.readouterr().out


def test_main_articulo_no_encontrado(capsys):
    _ejecutar_main(
        ["NoExiste", "en", "informe"],
        ejecutar_error=ArticuloNoEncontrado("x"),
    )
    assert "No se encontro un articulo" in capsys.readouterr().out


def test_main_error_enriquecimiento(capsys):
    _ejecutar_main(
        ["Marketing", "en", "informe"],
        ejecutar_error=EnriquecimientoError("x"),
    )
    assert "No se pudo enriquecer" in capsys.readouterr().out


def test_main_error_traduccion(capsys):
    _ejecutar_main(
        ["Marketing", "en", "informe"],
        ejecutar_error=TraduccionError("x"),
    )
    assert "No se pudo traducir" in capsys.readouterr().out
