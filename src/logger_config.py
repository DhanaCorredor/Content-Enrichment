"""Configuracion central de logs (HU-7)."""

import logging


def configurar_logger(ruta: str = "logs/app.log") -> logging.Logger:
    """Devuelve un logger que escribe en 'ruta' con fecha y nivel."""
    raise NotImplementedError
