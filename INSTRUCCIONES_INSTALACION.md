# 📋 Instrucciones de Instalación - BuScanGo

## 🎯 Requisitos Previos

- **Python 3.13 o superior** instalado
- **Git** instalado (opcional, solo si usas GitHub)
- **Conexión a internet** (para instalar dependencias y cargar mapas)

## 🚀 Instalación Paso a Paso

### **Paso 1: Obtener el Código**

#### **Opción A: Desde GitHub (Recomendado)**
```bash
git clone https://github.com/tu-usuario/buscango.git
cd buscango
```

#### **Opción B: Desde Archivo ZIP**
1. Extraer el archivo ZIP en una carpeta
2. Abrir terminal en esa carpeta

### **Paso 2: Crear Entorno Virtual**

```bash
python -m venv venv
```

### **Paso 3: Activar Entorno Virtual**

#### **Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

#### **Windows (Git Bash):**
```bash
source venv/Scripts/activate
```

#### **Linux/Mac:**
```bash
source venv/bin/activate
```

**✅ Verificación:** Deberías ver `(venv)` al inicio de tu prompt

### **Paso 4: Instalar Dependencias**

```bash
pip install -r requirements.txt
```

**Dependencias que se instalarán:**
- `folium` - Mapas interactivos
- `tkinterweb` - Visualización web en Tkinter
- `reportlab` - Generación de reportes
- `plyer` - Notificaciones
- `python-dotenv` - Variables de entorno
- `requests` - Peticiones HTTP
- `pillow` - Procesamiento de imágenes

### **Paso 5: Ejecutar la Aplicación**

```bash
python main.py
```

## 🎯 Uso de la Aplicación

### **Funcionalidades Disponibles:**

1. **🗺️ Mapa Interactivo**
   - Pestaña "Mapa"
   - Mapa de Santiago con marcadores
   - Zoom y navegación

2. **🚌 Gestión de Buses**
   - Archivo → Nuevo Bus
   - Gestión → Listar Buses
   - Crear buses con número y capacidad

3. **🛣️ Gestión de Rutas**
   - Archivo → Nueva Ruta
   - Gestión → Listar Rutas
   - Crear rutas con paradas

4. **📊 Datos de Ejemplo**
   - 3 buses precargados
   - 3 rutas de ejemplo
   - Datos realistas de Santiago

## 🔧 Solución de Problemas

### **Error: "ModuleNotFoundError"**
```bash
# Verificar que el entorno virtual esté activado
# Deberías ver (venv) al inicio del prompt
source venv/Scripts/activate  # Reactivar si es necesario
pip install -r requirements.txt  # Reinstalar dependencias
```

### **Error: "No se puede encontrar el archivo"**
```bash
# Verificar que estás en el directorio correcto
pwd  # Debería mostrar la carpeta del proyecto
ls   # Deberías ver main.py, requirements.txt, etc.
```

### **Error: "Permission denied" (Windows)**
```powershell
# Ejecutar PowerShell como administrador
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### **El mapa no se carga**
- Verificar conexión a internet
- El mapa necesita internet para cargar los tiles
- Si hay error, aparecerá un botón "Reintentar"

## 📱 Comandos Rápidos

### **Para Windows (PowerShell):**
```powershell
cd "ruta\al\proyecto"
.\venv\Scripts\Activate.ps1
python main.py
```

### **Para Windows (Git Bash):**
```bash
cd "/ruta/al/proyecto"
source venv/Scripts/activate
python main.py
```

### **Para Linux/Mac:**
```bash
cd /ruta/al/proyecto
source venv/bin/activate
python main.py
```

## 🆘 Soporte

Si tienes problemas:

1. **Verificar Python:** `python --version` (debe ser 3.13+)
2. **Verificar entorno virtual:** Debe aparecer `(venv)` en el prompt
3. **Verificar dependencias:** `pip list` (debe mostrar todas las librerías)
4. **Verificar archivos:** `ls` (debe mostrar main.py, requirements.txt, etc.)

## 📞 Contacto

Para soporte técnico, contacta al desarrollador con:
- Sistema operativo
- Versión de Python
- Mensaje de error completo
- Pasos que seguiste

---

**¡Disfruta usando BuScanGo! 🚌✨**
