# Content Enrichment

Herramienta CLI que busca un tema en Wikipedia, enriquece el contenido con la
API de OpenAI, lo traduce al idioma elegido (`deep-translator`) y genera un
informe en `.txt` o `.pdf`.

## Arquitectura

Pipeline orientado a objetos (una clase por etapa, responsabilidad unica):

```
Tema -> WikipediaScraper -> Enricher -> Translator -> (Summarizer) -> Exporter -> archivo
```

`Pipeline` orquesta las etapas; `main.py` solo lee la entrada y cablea.

## Estructura

```
src/        Codigo fuente (una clase por modulo)
tests/      Tests unitarios, integracion y escenarios Gherkin (pytest-bdd)
output/     Archivos generados (ignorado por git)
logs/       Logs de ejecucion (ignorado por git)
```

## Dependencias

- Python 3.10+
- requests, beautifulsoup4 (scraping)
- openai (enriquecimiento y resumenes, modelo gpt-4o-mini)
- deep-translator (traduccion)
- reportlab (PDF), python-dotenv (.env)
- pytest, pytest-cov, pytest-bdd (tests)

## Instalacion local

```bash
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
cp .env.example .env           # rellena OPENAI_API_KEY
```

## Uso

```bash
python src/main.py
```

## Tests

```bash
pytest                                          # ejecuta la suite
pytest --cov=src --cov-report=term-missing      # cobertura (objetivo 100%)
```
