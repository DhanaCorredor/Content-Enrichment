# language: es
Caracteristica: Enriquecer y traducir un articulo de Wikipedia
  Como usuaria
  Quiero buscar un tema, enriquecerlo y traducirlo
  Para obtener un informe mejorado en mi idioma

  Escenario: Flujo completo de un tema valido
    Dado un tema "Ada Lovelace" y el idioma destino "en"
    Cuando ejecuto el pipeline y guardo en formato "txt"
    Entonces se genera un archivo con el contenido traducido
