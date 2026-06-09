# 🗂️ Tareas (Kanban)

> Las tareas del proyecto se gestionan en **GitHub Projects**, no en Notion.
> 👉 **Tablero:** https://github.com/users/DhanaCorredor/projects/6

Notion se usa solo para **documentación**; el tablero de GitHub es la **fuente única de tareas**. Las tarjetas son *issues* del repositorio [`DhanaCorredor/Content-Enrichment`](https://github.com/DhanaCorredor/Content-Enrichment) y se mueven entre columnas a mano según avanza el trabajo.

**Columnas:** `Backlog` → `In progress` → `In review` → `Done`
**Prioridad:** `P0` mínimos del briefing · `P1` extras · `P2` soporte (calidad, docs, presentación)

---

## 📸 Estado actual (snapshot)

> Resumen para la documentación. El estado en vivo siempre está en el [tablero de GitHub](https://github.com/users/DhanaCorredor/projects/6).

### ✅ Done
- **#1** Crear el repositorio en GitHub
- **#2** Crear la estructura de carpetas y el `.gitignore`
- **#3** `requirements.txt` y entorno virtual
- **#4** Conseguir la clave gratuita de Groq y montar `.env` / `.env.example`
- **#5** Decidir motor de IA (Groq) y traducción (`deep-translator`)
- **#6** Acordar las firmas de los métodos (scaffold)
- **#7** Documentación: README, wiki técnica (Notion) y plan de trabajo

### 🚧 In progress
- **#8** Sprint Planning: fijar el orden de las historias

### 📋 Backlog
| # | Tarea | Prioridad | HU |
|---|-------|-----------|----|
| #9 | `scraper.py`: buscar en Wikipedia y extraer título + 5 párrafos | P0 | HU-2 |
| #10 | `main.py`: pedir tema e idioma y mostrar el resultado | P0 | HU-1 |
| #11 | Manejar tema no encontrado (`ArticuloNoEncontrado`) | P1 | HU-8 |
| #12 | Tests del scraper (red mockeada) | P0 | HU-2 |
| #13 | `enricher.py`: enviar texto a Groq y devolver versión mejorada | P0 | HU-3 |
| #14 | Conectar scraper con enricher en `main.py` | P0 | HU-3 |
| #15 | Controlar errores de la API (límite, sin conexión, clave inválida) | P1 | HU-8 |
| #16 | Tests del enricher (cliente mockeado) | P0 | HU-3 |
| #17 | `translator.py`: traducir con `deep-translator` | P0 | HU-4 |
| #18 | `exporter.py`: guardar en `.txt` y `.pdf` (reportlab + Flowables) | P0 | HU-5 |
| #19 | Integrar el pipeline completo (`pipeline.py` y `main.py`) | P0 | HU-4/5 |
| #20 | Tests de translator, exporter e integración del pipeline | P0 | HU-4/5 |
| #21 | `summarizer.py`: generar resumen del contenido enriquecido | P1 | HU-6 |
| #22 | `logger_config.py`: registrar el proceso en `logs/app.log` | P1 | HU-7 |
| #23 | Repasar manejo de errores y mensajes claros | P1 | HU-8 |
| #24 | Verificar cobertura de tests al 100% | P2 | — |
| #25 | Repasar README y wiki de Notion | P2 | — |
| #26 | Ensayar la demo | P2 | — |
| #27 | Demo en vivo + arquitectura y aprendizajes | P2 | — |
| #28 | Sprint Review + Retrospectiva | P2 | — |
