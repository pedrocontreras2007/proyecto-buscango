class Ruta:
    def __init__(self, nombre, paradas=None):
        self.nombre = nombre
        self.paradas = paradas or []
    
    def agregar_parada(self, parada):
        self.paradas.append(parada)
    
    def eliminar_parada(self, indice):
        return self.paradas.pop(indice)
    
    def mover_parada(self, indice_origen, indice_destino):
        parada = self.paradas.pop(indice_origen)
        self.paradas.insert(indice_destino, parada)
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'paradas': self.paradas
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['nombre'], data['paradas'])
    
    def validar_ruta(self):
        """Valida que la ruta sea válida"""
        if not self.paradas:
            raise ValueError("La ruta debe tener al menos una parada")
        
        # Validar que no haya paradas duplicadas
        paradas_unicas = set(parada.id for parada in self.paradas)
        if len(paradas_unicas) != len(self.paradas):
            raise ValueError("La ruta tiene paradas duplicadas")

    def calcular_tiempo_total(self):
        """Calcula el tiempo total estimado de la ruta"""
        tiempo_total = 0
        for i in range(len(self.paradas) - 1):
            tiempo_tramo = self._calcular_tiempo_entre_paradas(
                self.paradas[i], 
                self.paradas[i + 1]
            )
            tiempo_total += tiempo_tramo
        return tiempo_total
    
    def _calcular_tiempo_entre_paradas(self, parada_origen, parada_destino):
        """Calcula el tiempo estimado entre dos paradas"""
        # TODO: Implementar cálculo real basado en distancia y velocidad promedio
        # Por ahora retorna un tiempo fijo de 5 minutos entre paradas
        return 5  # minutos