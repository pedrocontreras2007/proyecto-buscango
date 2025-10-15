import json
import os
from pathlib import Path

class DataManager:
    def __init__(self, archivo):
        # Usar ruta absoluta para evitar problemas de directorio
        if not os.path.isabs(archivo):
            self.archivo = Path(__file__).parent.parent / archivo
        else:
            self.archivo = Path(archivo)
        self.data_dir = self.archivo.parent
        
        # Crear directorio si no existe
        if not self.data_dir.exists():
            self.data_dir.mkdir(parents=True)
    
    def cargar_datos(self):
        try:
            if self.archivo.exists():
                with open(self.archivo, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {'rutas': {}, 'buses': {}}
        except json.JSONDecodeError:
            raise ValueError(f"El archivo {self.archivo} está corrupto")
        except Exception as e:
            raise IOError(f"Error al cargar datos: {str(e)}")
    
    def guardar_datos(self, datos):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error al guardar datos: {e}")
            return False
        
    def buscar_bus(self, numero):
        """Busca un bus por su número"""
        try:
            datos = self.cargar_datos()
            return next((bus for bus in datos['buses'].values() 
                        if bus['numero'] == numero), None)
        except Exception as e:
            raise ValueError(f"Error al buscar bus: {str(e)}")

    def actualizar_posicion_bus(self, numero_bus, lat, lon):
        """Actualiza la posición de un bus"""
        try:
            datos = self.cargar_datos()
            if numero_bus in datos['buses']:
                datos['buses'][numero_bus]['posicion'] = (lat, lon)
                self.guardar_datos(datos)
                return True
            return False
        except Exception as e:
            raise ValueError(f"Error al actualizar posición: {str(e)}")