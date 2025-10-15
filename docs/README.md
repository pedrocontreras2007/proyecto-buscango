# BuScanGo - Documentación

## Estructura del Proyecto

```
proyectoBuScanGo/
├── auth/          # Autenticación de usuarios
├── database/      # Gestión de base de datos
├── gui/           # Interfaz gráfica
├── models/        # Modelos de datos
├── reports/       # Generación de reportes
├── services/      # Servicios del sistema
├── tests/         # Pruebas unitarias
├── utils/         # Utilidades
└── docs/          # Documentación
```

## Instalación

1. Clonar el repositorio
2. Crear entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activar entorno virtual:
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
4. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Desarrollo

### Convenciones de código
- PEP 8
- Docstrings en formato Google
- Nombres de variables y funciones en español

### Tests
Ejecutar tests:
```bash
python -m unittest discover tests
```