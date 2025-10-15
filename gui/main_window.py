import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from .map_view import MapView
from .styles import Styles
from models.bus import Bus

class MainWindow(tk.Frame):
    def __init__(self, parent, data_manager):
        super().__init__(parent)
        self.data_manager = data_manager
        self.parent = parent
        
        self._create_menu()
        self._init_ui()
        self.styles = Styles()
        self.styles.apply_style(self)
        
    def _create_menu(self):
        menubar = tk.Menu(self.parent)
        
        # Menú Archivo
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Nuevo Bus", command=self._nuevo_bus)
        file_menu.add_command(label="Nueva Ruta", command=self._nueva_ruta)
        file_menu.add_separator()
        file_menu.add_command(label="Salir", command=self.parent.quit)
        menubar.add_cascade(label="Archivo", menu=file_menu)
        
        self.parent.config(menu=menubar)
    
    def _init_ui(self):
        # Notebook principal
        self.notebook = ttk.Notebook(self)
        
        # Pestaña de mapa
        self.map_frame = ttk.Frame(self.notebook)
        self.map_view = MapView(self.map_frame)
        self.map_view.pack(expand=True, fill="both")
        
        # Pestaña de gestión
        self.management_frame = self._create_management_frame()
        
        self.notebook.add(self.map_frame, text="Mapa")
        self.notebook.add(self.management_frame, text="Gestión")
        self.notebook.pack(expand=True, fill="both", padx=5, pady=5)
    
    def _create_management_frame(self):
        """Crea el frame de gestión de buses y rutas"""
        frame = ttk.Frame(self.notebook)
        
        # Panel de buses
        bus_frame = ttk.LabelFrame(frame, text="Gestión de Buses")
        bus_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Button(bus_frame, text="Agregar Bus", command=self._nuevo_bus).pack(side="left", padx=5)
        ttk.Button(bus_frame, text="Listar Buses", command=self._listar_buses).pack(side="left", padx=5)
        
        # Panel de rutas
        route_frame = ttk.LabelFrame(frame, text="Gestión de Rutas")
        route_frame.pack(fill="x", padx=10, pady=5)
        
        ttk.Button(route_frame, text="Agregar Ruta", command=self._nueva_ruta).pack(side="left", padx=5)
        ttk.Button(route_frame, text="Listar Rutas", command=self._listar_rutas).pack(side="left", padx=5)
        
        return frame
    
    def _nuevo_bus(self):
        """Abre diálogo para crear nuevo bus"""
        dialog = BusDialog(self.parent, self.data_manager)
        self.parent.wait_window(dialog.dialog)
    
    def _nueva_ruta(self):
        """Abre diálogo para crear nueva ruta"""
        dialog = RutaDialog(self.parent, self.data_manager)
        self.parent.wait_window(dialog.dialog)
    
    def _listar_buses(self):
        """Muestra lista de buses"""
        try:
            datos = self.data_manager.cargar_datos()
            buses = datos.get('buses', {})
            
            if not buses:
                messagebox.showinfo("Lista de Buses", "No hay buses registrados")
                return
            
            # Crear ventana de lista
            list_window = tk.Toplevel(self.parent)
            list_window.title("Lista de Buses")
            list_window.geometry("500x400")
            list_window.transient(self.parent)
            
            # Frame principal
            main_frame = ttk.Frame(list_window, padding="10")
            main_frame.pack(fill="both", expand=True)
            
            # Treeview para mostrar buses
            columns = ("Número", "Capacidad", "Estado", "Pasajeros")
            tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=15)
            
            # Configurar columnas
            for col in columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)
            
            # Agregar datos
            for numero, bus_data in buses.items():
                tree.insert("", "end", values=(
                    numero,
                    bus_data.get('capacidad', 'N/A'),
                    bus_data.get('estado', 'N/A'),
                    bus_data.get('pasajeros', 0)
                ))
            
            # Scrollbar
            scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            
            tree.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar la lista de buses: {str(e)}")
    
    def _listar_rutas(self):
        """Muestra lista de rutas"""
        try:
            datos = self.data_manager.cargar_datos()
            rutas = datos.get('rutas', {})
            
            if not rutas:
                messagebox.showinfo("Lista de Rutas", "No hay rutas registradas")
                return
            
            # Crear ventana de lista
            list_window = tk.Toplevel(self.parent)
            list_window.title("Lista de Rutas")
            list_window.geometry("600x400")
            list_window.transient(self.parent)
            
            # Frame principal
            main_frame = ttk.Frame(list_window, padding="10")
            main_frame.pack(fill="both", expand=True)
            
            # Treeview para mostrar rutas
            columns = ("Nombre", "Paradas")
            tree = ttk.Treeview(main_frame, columns=columns, show="headings", height=15)
            
            # Configurar columnas
            tree.heading("Nombre", text="Nombre de la Ruta")
            tree.heading("Paradas", text="Número de Paradas")
            tree.column("Nombre", width=200)
            tree.column("Paradas", width=100)
            
            # Agregar datos
            for nombre, ruta_data in rutas.items():
                paradas = ruta_data.get('paradas', [])
                tree.insert("", "end", values=(
                    nombre,
                    len(paradas)
                ))
            
            # Scrollbar
            scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=tree.yview)
            tree.configure(yscrollcommand=scrollbar.set)
            
            tree.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar la lista de rutas: {str(e)}")


class BusDialog:
    def __init__(self, parent, data_manager):
        self.data_manager = data_manager
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Nuevo Bus")
        self.dialog.geometry("300x200")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Centrar la ventana
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))
        
        self._create_widgets()
    
    def _create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.dialog, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Número de bus
        ttk.Label(main_frame, text="Número de Bus:").grid(row=0, column=0, sticky="w", pady=5)
        self.numero_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.numero_var, width=20).grid(row=0, column=1, pady=5, padx=(10, 0))
        
        # Capacidad
        ttk.Label(main_frame, text="Capacidad:").grid(row=1, column=0, sticky="w", pady=5)
        self.capacidad_var = tk.StringVar(value="40")
        ttk.Entry(main_frame, textvariable=self.capacidad_var, width=20).grid(row=1, column=1, pady=5, padx=(10, 0))
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Crear", command=self._crear_bus).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Cancelar", command=self.dialog.destroy).pack(side="left", padx=5)
    
    def _crear_bus(self):
        try:
            numero = self.numero_var.get().strip()
            capacidad = int(self.capacidad_var.get())
            
            if not numero:
                messagebox.showerror("Error", "El número de bus es obligatorio")
                return
            
            if capacidad <= 0:
                messagebox.showerror("Error", "La capacidad debe ser mayor a 0")
                return
            
            # Crear el bus
            bus = Bus(numero, capacidad)
            
            # Guardar en el data manager
            datos = self.data_manager.cargar_datos()
            if 'buses' not in datos:
                datos['buses'] = {}
            
            datos['buses'][numero] = bus.to_dict()
            self.data_manager.guardar_datos(datos)
            
            messagebox.showinfo("Éxito", f"Bus {numero} creado exitosamente")
            self.dialog.destroy()
            
        except ValueError as e:
            messagebox.showerror("Error", f"Error en los datos: {str(e)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear el bus: {str(e)}")


class RutaDialog:
    def __init__(self, parent, data_manager):
        self.data_manager = data_manager
        self.dialog = tk.Toplevel(parent)
        self.dialog.title("Nueva Ruta")
        self.dialog.geometry("400x300")
        self.dialog.resizable(False, False)
        self.dialog.transient(parent)
        self.dialog.grab_set()
        
        # Centrar la ventana
        self.dialog.geometry("+%d+%d" % (parent.winfo_rootx() + 50, parent.winfo_rooty() + 50))
        
        self._create_widgets()
    
    def _create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.dialog, padding="10")
        main_frame.pack(fill="both", expand=True)
        
        # Nombre de la ruta
        ttk.Label(main_frame, text="Nombre de la Ruta:").grid(row=0, column=0, sticky="w", pady=5)
        self.nombre_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=self.nombre_var, width=30).grid(row=0, column=1, pady=5, padx=(10, 0))
        
        # Lista de paradas
        ttk.Label(main_frame, text="Paradas (una por línea):").grid(row=1, column=0, sticky="nw", pady=5)
        
        # Text widget para paradas
        text_frame = ttk.Frame(main_frame)
        text_frame.grid(row=1, column=1, pady=5, padx=(10, 0), sticky="nsew")
        
        self.paradas_text = tk.Text(text_frame, width=30, height=8)
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.paradas_text.yview)
        self.paradas_text.configure(yscrollcommand=scrollbar.set)
        
        self.paradas_text.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        ttk.Button(button_frame, text="Crear", command=self._crear_ruta).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Cancelar", command=self.dialog.destroy).pack(side="left", padx=5)
    
    def _crear_ruta(self):
        try:
            nombre = self.nombre_var.get().strip()
            paradas_text = self.paradas_text.get("1.0", tk.END).strip()
            
            if not nombre:
                messagebox.showerror("Error", "El nombre de la ruta es obligatorio")
                return
            
            # Procesar paradas
            paradas = []
            if paradas_text:
                paradas = [p.strip() for p in paradas_text.split('\n') if p.strip()]
            
            # Crear la ruta
            from models.ruta import Ruta
            ruta = Ruta(nombre, paradas)
            
            # Guardar en el data manager
            datos = self.data_manager.cargar_datos()
            if 'rutas' not in datos:
                datos['rutas'] = {}
            
            datos['rutas'][nombre] = ruta.to_dict()
            self.data_manager.guardar_datos(datos)
            
            messagebox.showinfo("Éxito", f"Ruta '{nombre}' creada exitosamente con {len(paradas)} paradas")
            self.dialog.destroy()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear la ruta: {str(e)}")