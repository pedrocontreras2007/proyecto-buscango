from utils.constants import BUS_STATES

class Bus:
    def __init__(self, numero, capacidad=40):
        if not isinstance(numero, str):
            raise ValueError("El número de bus debe ser una cadena de texto")
        if not isinstance(capacidad, int) or capacidad <= 0:
            raise ValueError("La capacidad debe ser un número entero positivo")
            
        self.numero = numero
        self.capacidad = capacidad
        self.estado = "AVAILABLE"
        self.posicion = None
        self.pasajeros = 0
        self.ruta_actual = None
        self.posicion_ruta = 0

    def asignar_ruta(self, ruta):
        self.ruta_actual = ruta
        self.estado = BUS_STATES["IN_ROUTE"]
        self.posicion = 0 if ruta else None

    def actualizar_posicion(self, lat, lon):
        self.posicion = (lat, lon)
        
    def subir_pasajeros(self, cantidad):
        if not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un número entero positivo")
        if self.pasajeros + cantidad > self.capacidad:
            raise ValueError("No hay suficiente espacio en el bus")
        self.pasajeros += cantidad
        
    def bajar_pasajeros(self, cantidad):
        bajados = min(cantidad, self.pasajeros)
        self.pasajeros -= bajados
        return bajados

    def to_dict(self):
        return {
            "numero": self.numero,
            "capacidad": self.capacidad,
            "estado": self.estado,
            "ruta": self.ruta_actual.nombre if self.ruta_actual else None,
            "posicion": self.posicion,
            "pasajeros": self.pasajeros
        }

    @classmethod
    def from_dict(cls, data):
        bus = cls(data["numero"], data["capacidad"])
        bus.estado = data["estado"]
        bus.posicion = data["posicion"]
        bus.pasajeros = data["pasajeros"]
        return bus

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del bus verificando que sea válido"""
        estados_validos = ["AVAILABLE", "IN_ROUTE", "MAINTENANCE"]
        if nuevo_estado not in estados_validos:
            raise ValueError(f"Estado no válido. Debe ser uno de: {estados_validos}")
        self.estado = nuevo_estado

    def obtener_siguiente_parada(self):
        """Obtiene la siguiente parada en la ruta actual"""
        if not self.ruta_actual:
            return None
        if self.posicion_ruta >= len(self.ruta_actual.paradas) - 1:
            return None
        return self.ruta_actual.paradas[self.posicion_ruta + 1]

    def calcular_tiempo_estimado(self, parada_destino):
        """Calcula el tiempo estimado hasta la parada destino"""
        if not self.posicion or not parada_destino.posicion:
            return None
        # TODO: Implementar cálculo real basado en distancia y tráfico
        return 0  # Temporal
    
    def mover_siguiente_parada(self):
        """Mueve el bus a la siguiente parada en la ruta"""
        if not self.ruta_actual or not self.ruta_actual.paradas:
            return False
        
        if self.posicion_ruta < len(self.ruta_actual.paradas) - 1:
            self.posicion_ruta += 1
            # Actualizar posición con la nueva parada
            if hasattr(self.ruta_actual.paradas[self.posicion_ruta], 'posicion'):
                self.posicion = self.ruta_actual.paradas[self.posicion_ruta].posicion
            return True
        return False