import tkinter as tk
from tkinter import ttk

class Styles:
    @staticmethod
    def apply_style(widget):
        style = ttk.Style()
        
        # Configurar estilo general
        style.configure("TButton",
            padding=6,
            relief="flat",
            background="#4CAF50",
            foreground="white",
            font=("Arial", 10)
        )
        
        style.configure("TLabel",
            font=("Arial", 10),
            padding=5
        )
        
        style.configure("TEntry",
            padding=5
        )
        
        # Aplicar temas específicos
        style.theme_use('clam')

    @staticmethod
    def apply_custom_style(widget):
        """Aplica el estilo visual personalizado a los widgets"""
        style = {
            "bg": "#f0f0f0",
            "fg": "#333333",
            "font": ("Arial", 10),
            "button_bg": "#4CAF50",
            "button_fg": "white",
            "entry_bg": "white"
        }
        
        widget.configure(bg=style["bg"])
        
        for child in widget.winfo_children():
            if isinstance(child, tk.Button):
                child.configure(
                    bg=style["button_bg"],
                    fg=style["button_fg"],
                    font=style["font"]
                )
            elif isinstance(child, tk.Entry):
                child.configure(
                    bg=style["entry_bg"],
                    font=style["font"]
                )