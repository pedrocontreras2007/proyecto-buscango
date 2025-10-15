import logging
import os
from pathlib import Path

def setup_logger():
    # Crear directorio de logs si no existe
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Configurar el logger
    logger = logging.getLogger('BuScanGo')
    logger.setLevel(logging.INFO)

    # Handler para archivo
    file_handler = logging.FileHandler(log_dir / 'buscango.log', encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # Handler para consola
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Formato
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger