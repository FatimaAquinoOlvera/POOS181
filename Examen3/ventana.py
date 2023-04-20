import tkinter as tk
from tkinter import ttk
from controlador import ControladorBD

# Crear un objeto controlador clase ControladorBD
controlador = ControladorBD()

def registro():
    mercancia = mercancia_ingresar.get()
    pais = pais_ingresar.get()
    try:
        controlador.registar(mercancia, pais)
    except:
        print("Error al ingresar")

def consultar():
    pais = pais_consultar.get()
    mercancia = controlador.consultar(pais)
    if mercancia is None:
        textoBuscar.delete(1.0, tk.END)  # Borra el contenido actual del widget de texto
        textoBuscar.insert(tk.END, "No se encontró mercancía para ese país")
    else:
        textoBuscar.delete(1.0, tk.END)  # Borra el contenido actual del widget
        #Usa un ciclo for para recorrer la lista de mercancia y mostar los datos
        for mercancia in mercancia:
            id = mercancia[0]
            nombre_mercancia = mercancia[1]
            pais_mercancia = mercancia[2]
            textoBuscar.insert(tk.END, "\nID: " + str(id) + "\nMercancia: " + nombre_mercancia + "\nPais: " + pais_mercancia)

        
def eliminar():
    id = id_eliminar.get()
    controlador.eliminar(id)


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

#Panel de registro

labelIngresar = tk.Label(panel1, text="Insertar mercancia", fg="green")
labelIngresar.pack(pady=10)

labelMercancia = tk.Label(panel1, text="Nombre de mercancia", fg="green")
labelMercancia.pack(pady=10)
mercancia_ingresar = tk.StringVar()
entryMercancia = tk.Entry(panel1, textvariable=mercancia_ingresar)
entryMercancia.pack(pady=5)

labelPais = tk.Label(panel1, text="Pais", fg="green")
labelPais.pack(pady=10)
pais_ingresar = tk.StringVar()
entryPais = tk.Entry(panel1, textvariable=pais_ingresar)
entryPais.pack(pady=5)

botonIngresar = tk.Button(panel1, text="Ingresar", command=registro, bg="green", fg="white")
botonIngresar.pack(pady=10)


#Panel de consulta

labelConsultar = tk.Label(panel2, text="Buscar por pais", fg="blue")
labelConsultar.pack(pady=10)

labelPais = tk.Label(panel2, text="Pais", fg="blue")
labelPais.pack(pady=10)
pais_consultar = tk.StringVar()
entryPais = tk.Entry(panel2, textvariable=pais_consultar)
entryPais.pack(pady=5)

botonConsultar = tk.Button(panel2, text="Consultar", command=consultar, bg="blue", fg="white")
botonConsultar.pack(pady=10)

textoBuscar = tk.Text(panel2, width=40, height=10)
textoBuscar.pack(pady=10)


#Panel de eliminacion

labelEliminar = tk.Label(panel3, text="Eliminar por ID", fg="red")
labelEliminar.pack(pady=10)

labelID = tk.Label(panel3, text="ID", fg="red")
labelID.pack(pady=10)
id_eliminar = tk.StringVar()
entryID = tk.Entry(panel3, textvariable=id_eliminar)
entryID.pack(pady=5)

botonEliminar = tk.Button(panel3, text="Eliminar", command=eliminar, bg="red", fg="white")
botonEliminar.pack(pady=10)



Ventana.mainloop()
