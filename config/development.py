"""
Configuración para entorno de desarrollo
"""

# Configuración de Base de Datos
DB_CONFIG = {
    'name': 'buscango_dev.db',
    'backup_enabled': False,
    'log_queries': True
}

# Configuración de Logging
LOG_CONFIG = {
    'level': 'DEBUG',
    'file': 'logs/dev.log',
    'console': True
}

# Configuración del Simulador
SIMULATOR_CONFIG = {
    'speed_multiplier': 2.0,  # Velocidad doble para pruebas
    'auto_start': True
}

# Configuración de la interfaz
UI_CONFIG = {
    'debug_mode': True,
    'show_grid': True,
    'refresh_rate': 1  # segundo
}