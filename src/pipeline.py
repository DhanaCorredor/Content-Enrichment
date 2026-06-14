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
        # 1. Scraping: texto crudo de Wikipedia
        articulo = self.scraper.buscar_articulo(tema)
        texto_original = "\n\n".join(articulo["parrafos"])

        # 2. Enriquecer con la IA
        texto_enriquecido = self.enricher.enriquecer(texto_original)

        # 3. Traducir la version enriquecida. El idioma destino es un dato de
        # esta ejecucion, asi que se pasa directamente a traducir.
        texto_traducido = self.translator.traducir(texto_enriquecido, idioma_destino)

        secciones = [
            ("Original", texto_original),
            ("Enriquecido", texto_enriquecido),
            ("Traducido", texto_traducido),
        ]

        # Extra (HU-6): resumen, solo si se inyecto un Summarizer
        if self.summarizer is not None:
            secciones.append(("Resumen", self.summarizer.resumir(texto_enriquecido)))

        # 4. Exportar
        contenido = {"titulo": articulo["titulo"], "secciones": secciones}
        return self.exporter.exportar(contenido, nombre, formato)
