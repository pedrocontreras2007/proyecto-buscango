# Configuración de la aplicación
APP_NAME = "BuScanGo"
VERSION = "1.0.0"

# Estados de los buses
BUS_STATES = {
    "AVAILABLE": "Disponible",
    "IN_ROUTE": "En ruta",
    "MAINTENANCE": "En mantenimiento"
}

# Configuración de la interfaz
WINDOW_SIZE = "800x600"
WINDOW_TITLE = "BuScanGo - Sistema de Gestión de Buses"

# Configuración del mapa
MAP_CENTER = [-33.4489, -70.6693]  # Santiago, Chile
MAP_ZOOM = 13

# Mensajes
MESSAGES = {
    "ERROR_LOGIN": "Usuario o contraseña incorrectos",
    "SUCCESS_SAVE": "Datos guardados correctamente",
    "ERROR_SAVE": "Error al guardar los datos"
}

# Configuración de tiempos
TIEMPO_ACTUALIZACION = 5  # segundos
TIEMPO_SIMULACION = 0.1  # segundos

# Límites y restricciones
MAX_PASAJEROS = 40
MIN_DISTANCIA_PARADAS = 0.1  # km
MAX_VELOCIDAD = 60  # km/h

# Colores de la interfaz
COLORS = {
    'primary': '#4CAF50',
    'secondary': '#2196F3',
    'warning': '#FFC107',
    'error': '#F44336',
    'success': '#4CAF50',
    'background': '#F5F5F5',
    'text': '#212121'
}