"""Orquestador del flujo completo (el 'director de orquesta').

Conecta las etapas: scraping -> enriquecer -> traducir -> (resumir) -> exportar.
Cada etapa es una dependencia inyectada, lo que permite mockearlas en los tests
y respeta el principio de responsabilidad unica (Pipeline solo coordina).
"""


class Pipeline:
    def __init__(self, scraper, enricher, translator, exporter, summarizer=None) -> None:
        self.scraper = scraper
        self.enricher = enricher
        self.translator = translator
        self.exporter = exporter
        self.summarizer = summarizer

    def ejecutar(self, tema: str, idioma_destino: str, nombre: str, formato: str) -> str:
        """Ejecuta el flujo completo y devuelve la ruta del archivo generado."""
        articulo = self.scraper.buscar_articulo(tema)
        texto_original = "\n\n".join(articulo["parrafos"])

        texto_enriquecido = self.enricher.enriquecer(texto_original)

        texto_traducido = self.translator.traducir(texto_enriquecido, idioma_destino)

        secciones = [
            ("Original", texto_original),
            ("Enriquecido", texto_enriquecido),
            ("Traducido", texto_traducido),
        ]

        if self.summarizer is not None:
            secciones.append(("Resumen", self.summarizer.resumir(texto_enriquecido)))

        contenido = {"titulo": articulo["titulo"], "secciones": secciones}
        return self.exporter.exportar(contenido, nombre, formato)
