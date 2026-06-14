"""Etapa 1: scraping de Wikipedia."""

import requests
from bs4 import BeautifulSoup


class ArticuloNoEncontrado(Exception):
    """Se lanza cuando Wikipedia no devuelve un articulo para el tema dado."""


class WikipediaScraper:
    """Busca un tema en Wikipedia y extrae titulo + primeros 5 parrafos.

    Responsabilidad unica: obtener contenido crudo de Wikipedia. No sabe nada
    de IA, traduccion ni exportacion.
    """

    MAX_PARRAFOS = 5
    USER_AGENT = "ContentEnricher/1.0 (bootcamp project; educational use)"

    def __init__(self, idioma: str = "es") -> None:
        self.idioma = idioma

    def buscar_articulo(self, tema: str) -> dict:
        """Devuelve {'titulo': str, 'parrafos': [str, ...]}.

        Lanza ArticuloNoEncontrado si el tema no existe en Wikipedia.
        """
        nombre = tema.strip().replace(" ", "_")
        url = f"https://{self.idioma}.wikipedia.org/wiki/{nombre}"

        respuesta = requests.get(
            url,
            headers={"User-Agent": self.USER_AGENT},
            timeout=10,
        )

        if respuesta.status_code == 404:
            raise ArticuloNoEncontrado(f"No se encontro un articulo para '{tema}'.")
        respuesta.raise_for_status()

        sopa = BeautifulSoup(respuesta.text, "html.parser")
        encabezado = sopa.find("h1", id="firstHeading")
        cuerpo = sopa.find("div", class_="mw-parser-output")
        if encabezado is None or cuerpo is None:
            raise ArticuloNoEncontrado(
                f"La pagina de '{tema}' no tiene el formato esperado de un articulo."
            )

        titulo = encabezado.get_text(strip=True)
        parrafos = []
        for p in cuerpo.find_all("p"):
            texto = p.get_text().strip()
            if texto:
                parrafos.append(texto)
            if len(parrafos) == self.MAX_PARRAFOS:
                break

        if not parrafos:
            raise ArticuloNoEncontrado(f"El articulo '{tema}' no tiene contenido legible.")

        return {"titulo": titulo, "parrafos": parrafos}


if __name__ == "__main__":  # pragma: no cover
    scraper = WikipediaScraper(idioma="es")

    try:
        resultado = scraper.buscar_articulo("Marketing")
        print(f"Título encontrado: {resultado['titulo']}\n")
        print("Primer párrafo de muestra:")
        print(resultado['parrafos'][0])

    except ArticuloNoEncontrado as e:
        print(f"Error esperado: {e}")