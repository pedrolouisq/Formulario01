import tkinter as tk
from tkinter import messagebox

def crear_ventana(guardar_usuario, actualizar_lista_usuarios):

    ventana = tk.Tk()
    ventana.title("Formulario de Usuarios")
    ventana.config(bg='#f0f0f0') 

    tk.Label(ventana, text="Nombre:", fg="black", bg="#f0f0f0", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
    entry_nombre = tk.Entry(ventana, bg="#ffffff", fg="black", font=("Arial", 12))
    entry_nombre.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(ventana, text="Nickname:", fg="black", bg="#f0f0f0", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
    entry_nickname = tk.Entry(ventana, bg="#ffffff", fg="black", font=("Arial", 12))
    entry_nickname.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(ventana, text="Clave:", fg="black", bg="#f0f0f0", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
    entry_clave = tk.Entry(ventana, show="*", bg="#ffffff", fg="black", font=("Arial", 12))
    entry_clave.grid(row=2, column=1, padx=10, pady=10)

    boton_guardar = tk.Button(ventana, text="Guardar", command=lambda: guardar_usuario(entry_nombre, entry_nickname, entry_clave), bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
    boton_guardar.grid(row=3, columnspan=2, pady=10)

    listbox_usuarios = tk.Listbox(ventana, height=10, width=50, bg="#ffffff", fg="black", font=("Arial", 12))
    listbox_usuarios.grid(row=4, columnspan=2, padx=10, pady=10)


    actualizar_lista_usuarios(listbox_usuarios)

    ventana.mainloop()
