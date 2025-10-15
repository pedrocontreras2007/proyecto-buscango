# Configuración de la base de datos
DB_NAME = "buscango.db"

# Configuración de logging
LOG_CONFIG = {
    'filename': 'buscango.log',
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
}

# Configuración de la base de datos
DB_CONFIG = {
    'name': DB_NAME,
    'backup_interval': 24,  # horas
    'max_connections': 5
}

# Configuración del servidor
HOST = "localhost"
PORT = 8000

# Configuración del mapa
MAP_CENTER = [-33.4489, -70.6693]  # Santiago, Chile
MAP_ZOOM = 13

# Configuración de la interfaz
WINDOW_SIZE = "800x600"
WINDOW_TITLE = "BuScanGo"

# Configuración del simulador
SIMULATOR_CONFIG = {
    'update_interval': 1.0,  # segundos
    'speed_multiplier': 1.0
}

# Configuración de notificaciones
NOTIFICATION_TIMEOUT = 5000  # milisegundos