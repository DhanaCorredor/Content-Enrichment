# Content Enrichment

> Herramienta CLI que busca un tema en Wikipedia, enriquece el contenido con IA, lo traduce al idioma elegido y genera un informe en `.txt` o `.pdf`.

**Estado:** 🚧 En desarrollo (proyecto de aprendizaje · FemCoders P5 Madrid) · **Python 3.10+**

---

## ¿Qué hace?

Dado un tema y un idioma, ejecuta una **tubería (pipeline)** de cuatro pasos:

```
Tema ─▶ Wikipedia ─▶ Enriquecer (IA) ─▶ Traducir ─▶ Exportar ─▶ informe .txt / .pdf
```

1. **Busca** el tema en Wikipedia y extrae el título + los primeros 5 párrafos.
2. **Enriquece** el texto con IA (Groq, vía el SDK oficial de OpenAI).
3. **Traduce** el contenido al idioma elegido (`deep-translator`).
4. **Exporta** el resultado a `.txt` o a un PDF maquetado con `reportlab`.
5. *(Extra)* Genera un **resumen** del contenido enriquecido.

---

## Arquitectura

Pipeline **orientado a objetos**: una clase por etapa, con **responsabilidad única**. La clase `Pipeline` orquesta las etapas; `main.py` solo lee la entrada y cablea las piezas.

```
main.py ─▶ Pipeline ─▶ WikipediaScraper · Enricher · Translator · Summarizer · Exporter
```

| Clase | Responsabilidad |
|-------|-----------------|
| `WikipediaScraper` | Buscar y extraer contenido de Wikipedia. |
| `Enricher` | Enriquecer el texto con IA (Groq). |
| `Translator` | Traducir al idioma destino. |
| `Summarizer` | Resumir el contenido (extra). |
| `Exporter` | Guardar en `.txt` / `.pdf`. |
| `Pipeline` | Coordinar todas las etapas. |

---

## Estructura

```
src/        Código fuente (una clase por módulo)
tests/      Tests unitarios, de integración y escenarios Gherkin (pytest-bdd)
output/     Archivos generados (ignorado por git)
logs/       Logs de ejecución (ignorado por git)
```

---

## Stack

- **Python 3.10+**
- `requests` + `beautifulsoup4` — scraping
- `openai` (SDK) apuntado a **Groq** — enriquecimiento y resúmenes (modelo `llama-3.3-70b-versatile`)
- `deep-translator` — traducción (backend de Google, sin clave)
- `reportlab` — exportación a PDF
- `python-dotenv` — gestión de secretos
- `pytest` + `pytest-cov` + `pytest-bdd` — tests (objetivo de cobertura: 100%)

> **Nota:** el briefing pide la "API de OpenAI", pero usamos **Groq** (gratuito y compatible con el SDK de OpenAI) cambiando solo el `base_url`. La traducción usa `deep-translator` en lugar de "DeepTranslate". Ambas decisiones están documentadas.

---

## Instalación

```bash
# 1. Clonar y entrar al proyecto
git clone git@github.com:DhanaCorredor/Content-Enrichment.git
cd Content-Enrichment

# 2. Crear y activar el entorno virtual
python -m venv venv
venv\Scripts\activate          # Windows
# source venv/bin/activate     # Mac/Linux

# 3. Instalar dependencias
pip install -r requirements.txt
```

---

## Configuración

La IA usa una clave **gratuita** de Groq. Copia la plantilla y rellena tu clave:

```bash
copy .env.example .env         # Windows  (cp en Mac/Linux)
```

```env
# .env
GROQ_API_KEY=tu_clave_aqui
```

> Consigue tu clave gratis en https://console.groq.com/keys
> El archivo `.env` **nunca** se sube a git.

---

## Uso

```bash
python src/main.py
```

La aplicación pedirá el **tema**, el **idioma de destino** y el **formato/nombre** del archivo de salida, y guardará el informe en `output/`.

---

## Tests

```bash
pytest                                          # ejecuta toda la suite
pytest --cov=src --cov-report=term-missing      # cobertura (objetivo: 100%)
```

Todas las llamadas de red/API se **mockean**: los tests no usan internet ni gastan tokens.

---

## Documentación

- **Documentación completa (wiki, arquitectura, plan)**: [Notion](https://app.notion.com/p/dhanacorredor/37a54980d23480b1beb1fc50fe329cd7?v=37a54980d234805eb17a000c067172c7&source=copy_link).
- **Tablero de tareas (Kanban)**: [GitHub Projects #6](https://github.com/users/DhanaCorredor/projects/6).

---

## Autora

DhanaCorredor — FemCoders P5 Madrid.

## Licencia

Distribuido bajo licencia **MIT**. Ver [`LICENSE`](LICENSE).
