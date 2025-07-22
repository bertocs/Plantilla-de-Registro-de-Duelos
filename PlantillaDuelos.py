#Librerías necesarias
import tkinter as tk
import csv
import os

#  Ventana principal
root = tk.Tk()
root.title("Registro de Duelos")
root.geometry("400x600")  

# Color de fondo de la ventana
root.configure(bg="#f4f4f4")  

# Definir la ruta y nombre del archivo CSV
carpeta = "C:\\Users\\josea\\Desktop\\Proyectospython"  # Sustituir por tu ruta
if not os.path.exists(carpeta):
    os.makedirs(carpeta)
ruta_csv = os.path.join(carpeta, 'Duelos.csv')

# Lista de opciones para los menús desplegables
jugadores = [
    "Jugador 1", "Jugador 2", "Jugador 3", "Jugador 4", "Jugador 5", #Asigna jugadores que se quieren analizar
    "Jugador 6", "Jugador 7", "Jugador 8", "Jugador 9", "Jugador 10", 
    "Jugador 11", "Jugador 12", "Jugador 13", "Jugador 14", "Jugador 15",
    "Jugador 16", "Jugador 17", "Jugador 18", "Jugador 19", "Jugador 20",
    "Jugador 21", "Jugador 22", "Jugador 23", "Jugador 24", "Jugador 25" 
]
aereo_o_suelo = ['Aéreo', 'Suelo']
zonas = ['Zona 1', 'Zona 2', 'Zona 3']
evento = ['1vs1 Ofensivo', '1vs1 Defensivo', 'Balón Dividido/Caída']
consecuencia = ['Pérdida', 'Recuperación', 'Conservación Equipo', 'Conservación Rival'] 
jornadas = [str(i) for i in range(1, 31)]

# Variables de selección
jugador_seleccionado = tk.StringVar()
aereo_suelo_seleccionado = tk.StringVar()
zona_seleccionada = tk.StringVar()
evento_seleccionado = tk.StringVar()
consecuencia_seleccionada = tk.StringVar()
jornada_seleccionada = tk.StringVar()

# Frame para categorías
frame_categorias = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10, bg="#e0e0e0")
frame_categorias.pack(pady=20)

# Estilo de los botones y menús desplegables
estilo = {
    "bg": "#4CAF50",  # Color de fondo del botón
    "fg": "white",    # Color de texto
    "font": ("Arial", 12, "bold"),
    "relief": "raised",
    "bd": 2
}

# Función para crear los menús desplegables
def crear_desplegable(frame, label_text, variable, opciones, row):
    label = tk.Label(frame, text=label_text, anchor="w", bg="#f4f4f4", font=("Arial", 10))
    label.grid(row=row, column=0, sticky="w", padx=5, pady=5)
    dropdown = tk.OptionMenu(frame, variable, *opciones)
    dropdown.grid(row=row, column=1, padx=5, pady=5)
    dropdown.config(bg="#f4f4f4", font=("Arial", 10), relief="solid", bd=1)

# Crear los menús desplegables
crear_desplegable(frame_categorias, "Jugador:", jugador_seleccionado, jugadores, 0)
crear_desplegable(frame_categorias, "Aéreo o Suelo:", aereo_suelo_seleccionado, aereo_o_suelo, 1)
crear_desplegable(frame_categorias, "Zona:", zona_seleccionada, zonas, 2)
crear_desplegable(frame_categorias, "Evento:", evento_seleccionado, evento, 3)
crear_desplegable(frame_categorias, "Consecuencia:", consecuencia_seleccionada, consecuencia, 4)
crear_desplegable(frame_categorias, "Jornada:", jornada_seleccionada, jornadas, 5)

# Listbox con Scrollbar para mostrar registros
frame_historial = tk.Frame(root)
frame_historial.pack(pady=10, padx=10)

scrollbar = tk.Scrollbar(frame_historial)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox_registros = tk.Listbox(frame_historial, width=80, height=10, yscrollcommand=scrollbar.set, bg="#ffffff", font=("Arial", 10), selectmode=tk.SINGLE)
listbox_registros.pack(padx=10, pady=10)
scrollbar.config(command=listbox_registros.yview)

# Verificar si el archivo CSV existe y si está vacío para crear el encabezado
if not os.path.exists(ruta_csv) or os.stat(ruta_csv).st_size == 0:
    with open(ruta_csv, mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(["Jugador", "Aéreo o Suelo", "Zona", "Evento", "Consecuencia", "Jornada"])  # Escribe encabezado


# Función para guardar el registro en el CSV y en el Listbox
def guardar_registro():
    registro = [
        jugador_seleccionado.get(),
        aereo_suelo_seleccionado.get(),
        zona_seleccionada.get(),
        evento_seleccionado.get(),
        consecuencia_seleccionada.get(),
        jornada_seleccionada.get()
    ]
    # Guardar en el archivo CSV
    with open(ruta_csv, mode='a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow(registro)

    # Añadir el registro al Listbox con índice
    listbox_registros.insert(tk.END, f"{listbox_registros.size() + 1}. {', '.join(registro)}")

# Función para eliminar el último registro
def eliminar_ultimo_registro():
    # Eliminar último registro del Listbox
    if listbox_registros.size() > 0:
        listbox_registros.delete(tk.END)
        
    # Leer todos los registros del archivo CSV excepto el último
    with open(ruta_csv, mode='r', newline='') as archivo_csv:
        rows = list(csv.reader(archivo_csv))

    # Guardar de nuevo sin el último registro
    with open(ruta_csv, mode='w', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerows(rows[:-1])  # Escribir todas las filas menos la última

# Botones para guardar y eliminar registros
boton_guardar = tk.Button(root, text="Guardar Registro", command=guardar_registro, **estilo)
boton_guardar.pack(pady=10)

boton_eliminar = tk.Button(root, text="Eliminar último registro", command=eliminar_ultimo_registro, **estilo)
boton_eliminar.pack(pady=10)

# Ejecutar la ventana
root.mainloop()


