import tkinter as tk
from tkinter import messagebox
from clases.usuario import Usuarios
from formulario import crear_ventana

def guardar_usuario(entry_nombre, entry_nickname, entry_clave):
    nombre = entry_nombre.get()
    nickname = entry_nickname.get()
    clave = entry_clave.get()


    if not nombre or not nickname or not clave:
        messagebox.showwarning("Advertencia", "Por favor complete todos los campos")
        return


    Usuarios.guardarUsuario(nombre, nickname, clave)

    entry_nombre.delete(0, tk.END)
    entry_nickname.delete(0, tk.END)
    entry_clave.delete(0, tk.END)

def actualizar_lista_usuarios(listbox_usuarios):
    listbox_usuarios.delete(0, tk.END)
    
    for usuario in Usuarios.lista_usuarios:
        listbox_usuarios.insert(tk.END, f"Nombre: {usuario.nombre}, Nickname: {usuario.nickname}")

crear_ventana(guardar_usuario, actualizar_lista_usuarios)
