import tkinter as tk
from tkinter import ttk

Ventana = tk.Tk()
Ventana.title("Importaciones Europa")
Ventana.geometry("400x400")

notebook = ttk.Notebook(Ventana)
notebook.pack(fill="both", expand=True)

panel1 = ttk.Frame(notebook)
notebook.add(panel1, text="Insertar")

panel2 = ttk.Frame(notebook)
notebook.add(panel2, text="Consultar")

panel3 = ttk.Frame(notebook)
notebook.add(panel3, text="Eliminar")

Ventana.mainloop()