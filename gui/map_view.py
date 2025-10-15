import tkinter as tk
import folium
import os
from tkinterweb import HtmlFrame

class MapView(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self._init_map()
        
    def _init_map(self):
        try:
            # Crear el mapa centrado en Santiago
            m = folium.Map(
                location=[-33.4489, -70.6693],
                zoom_start=13,
                tiles='OpenStreetMap'
            )
            
            # Agregar título al mapa
            title_html = '''
            <h3 align="center" style="font-size:20px"><b>BuScanGo - Sistema de Gestión de Buses</b></h3>
            '''
            m.get_root().html.add_child(folium.Element(title_html))
            
            # Agregar algunos marcadores de ejemplo con coordenadas reales de Santiago
            folium.Marker(
                [-33.4489, -70.6693],
                popup='Plaza de Armas',
                tooltip='Plaza de Armas',
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)
            
            folium.Marker(
                [-33.4500, -70.6800],
                popup='Estación Central',
                tooltip='Estación Central',
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(m)
            
            folium.Marker(
                [-33.4400, -70.6500],
                popup='Parque Forestal',
                tooltip='Parque Forestal',
                icon=folium.Icon(color='green', icon='info-sign')
            ).add_to(m)
            
            folium.Marker(
                [-33.4600, -70.6600],
                popup='Providencia',
                tooltip='Providencia',
                icon=folium.Icon(color='orange', icon='info-sign')
            ).add_to(m)
            
            # Guardar el mapa como HTML con ruta absoluta
            import tempfile
            self.temp_file = os.path.join(tempfile.gettempdir(), "buscango_map.html")
            m.save(self.temp_file)
            
            # Verificar que el archivo se creó
            if not os.path.exists(self.temp_file):
                raise Exception("No se pudo crear el archivo del mapa")
            
            # Mostrar el mapa en el frame
            self.html_frame = HtmlFrame(self, messages_enabled=False)
            self.html_frame.load_file(self.temp_file)
            self.html_frame.pack(expand=True, fill="both")
            
        except Exception as e:
            # Si hay error, mostrar un mensaje en lugar del mapa
            error_frame = tk.Frame(self, bg="white")
            error_frame.pack(expand=True, fill="both")
            
            error_label = tk.Label(error_frame, text=f"Error al cargar el mapa: {str(e)}", 
                                 bg="white", fg="red", font=("Arial", 12))
            error_label.pack(expand=True)
            
            # Botón para reintentar
            retry_button = tk.Button(error_frame, text="Reintentar", 
                                   command=self._retry_map, bg="#4CAF50", fg="white")
            retry_button.pack(pady=10)
    
    def _retry_map(self):
        """Reintenta cargar el mapa"""
        # Limpiar el frame actual
        for widget in self.winfo_children():
            widget.destroy()
        
        # Intentar cargar el mapa nuevamente
        self._init_map()
    
    def __del__(self):
        """Limpia el archivo temporal al destruir el objeto"""
        try:
            if hasattr(self, 'temp_file') and os.path.exists(self.temp_file):
                os.remove(self.temp_file)
        except:
            pass
        
    def actualizar_ubicacion_bus(self, bus_id, lat, lon):
        # TODO: Implementar actualización de marcadores
        pass