import tkinter as tk
from tkinter import messagebox

class LoginWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("BuScanGo - Login")
        self.geometry("300x200")
        self._init_components()
        
    def _init_components(self):
        # Usuario
        tk.Label(self, text="Usuario:").pack(pady=5)
        self.username = tk.Entry(self)
        self.username.pack(pady=5)
        
        # Contraseña
        tk.Label(self, text="Contraseña:").pack(pady=5)
        self.password = tk.Entry(self, show="*")
        self.password.pack(pady=5)
        
        # Botón login
        tk.Button(self, text="Iniciar Sesión", command=self._login).pack(pady=20)
        
    def _login(self):
        # TODO: Implementar validación real
        if self.username.get() == "admin" and self.password.get() == "admin":
            self.destroy()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")