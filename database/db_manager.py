import sqlite3
from contextlib import contextmanager
from pathlib import Path

class DatabaseError(Exception):
    pass

class DatabaseManager:
    def __init__(self):
        self.db_path = Path(__file__).parent / "buscango.db"
        self._create_tables()
    
    @contextmanager
    def get_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_path)
            yield conn
        except sqlite3.Error as e:
            if conn:
                conn.rollback()
            raise DatabaseError(f"Error en la base de datos: {str(e)}")
        finally:
            if conn:
                conn.close()

    def _create_tables(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Tabla Usuarios
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    password TEXT NOT NULL,
                    tipo TEXT DEFAULT 'usuario'
                )
            """)
            
            # Tabla Buses
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS buses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero TEXT NOT NULL,
                    estado TEXT DEFAULT 'DETENIDO',
                    ultima_ubicacion TEXT
                )
            """)
            
            # Tabla Paradas
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS paradas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    ubicacion TEXT NOT NULL
                )
            """)
            
            conn.commit()