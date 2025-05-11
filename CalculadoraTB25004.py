import tkinter as tk
from math import sqrt  # Importar raíz cuadrada

# --- CONFIGURACIÓN PERSONALIZABLE ---
FUENTE = ("Arial", 18)
COLOR_FONDO = "#f0f0f0"
COLOR_BOTON = "#d9d9d9"
COLOR_ENTRADA = "#ffffff"

def agregar_caracter(caracter):
    entrada.set(entrada.get() + str(caracter))

def limpiar():
    entrada.set("")

def borrar_ultimo():
    entrada.set(entrada.get()[:-1])

def calcular():
    try:
        resultado = eval(entrada.get())
        entrada.set(str(resultado))
    except:
        entrada.set("Error")

def raiz_cuadrada():
    try:
        valor = eval(entrada.get())
        if valor < 0:
            entrada.set("Error")
        else:
            resultado = sqrt(valor)
            entrada.set(str(resultado))
    except:
        entrada.set("Error")

# --- VENTANA PRINCIPAL ---
ventana = tk.Tk()
ventana.title("Calculadora Responsive")
ventana.configure(bg=COLOR_FONDO)
ventana.geometry("400x500")

# Expandir columnas y filas proporcionalmente
for i in range(6):
    ventana.rowconfigure(i, weight=1)
for j in range(4):
    ventana.columnconfigure(j, weight=1)

# --- ENTRADA ---
entrada = tk.StringVar()
entrada_entry = tk.Entry(
    ventana, textvariable=entrada, font=("Arial", 24),
    bd=10, bg=COLOR_ENTRADA, relief=tk.FLAT, justify="right"
)
entrada_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# --- BOTONES ---
botones = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("+", 4, 2), ("=", 4, 3),
    ("C", 5, 0), ("←", 5, 1), ("√", 5, 2)
]

acciones = {
    "C": limpiar,
    "←": borrar_ultimo,
    "=": calcular,
    "√": raiz_cuadrada
}

for (texto, fila, columna) in botones:
    comando = acciones.get(texto, lambda t=texto: agregar_caracter(t))
    boton = tk.Button(
        ventana, text=texto, font=FUENTE,
        bg=COLOR_BOTON, relief="raised", borderwidth=1,
        command=comando
    )
    boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

# --- INICIAR APLICACIÓN ---
ventana.mainloop()
