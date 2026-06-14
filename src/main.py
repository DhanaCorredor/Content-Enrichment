"""Punto de entrada CLI.

Responsabilidad unica: leer la entrada de la usuaria, construir las clases
del pipeline (cableado) y delegar en Pipeline. Sin logica de negocio aqui.
"""

import os

from dotenv import load_dotenv

from src.groq_client import crear_cliente_groq
from src.scraper import WikipediaScraper, ArticuloNoEncontrado
from src.enricher import Enricher, EnriquecimientoError
from src.translator import Translator, TraduccionError
from src.exporter import Exporter
from src.pipeline import Pipeline


def _pedir(mensaje: str) -> str:
    """Pide un dato por terminal y valida que no este vacio."""
    valor = input(mensaje).strip()
    while not valor:
        print("Este campo no puede estar vacio.")
        valor = input(mensaje).strip()
    return valor


def main() -> None:
    load_dotenv()
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        print("Falta GROQ_API_KEY en el archivo .env.")
        return

    tema = _pedir("Tema a buscar en Wikipedia: ")
    idioma = _pedir("Idioma destino (ej. en, fr, it): ")
    nombre = _pedir("Nombre del archivo de salida: ")

    client = crear_cliente_groq(api_key)
    pipeline = Pipeline(
        scraper=WikipediaScraper(idioma="es"),
        enricher=Enricher(client),
        translator=Translator(),
        exporter=Exporter(),
    )

    try:
        ruta = pipeline.ejecutar(tema, idioma, nombre, "pdf")
    except ArticuloNoEncontrado:
        print(f"No se encontro un articulo de Wikipedia para '{tema}'.")
    except EnriquecimientoError:
        print("No se pudo enriquecer el texto con la IA. Revisa tu conexion o la clave de Groq.")
    except TraduccionError:
        print("No se pudo traducir el texto. Revisa tu conexion a internet.")
    else:
        print(f"Informe generado en: {ruta}")


if __name__ == "__main__":  # pragma: no cover
    main()
