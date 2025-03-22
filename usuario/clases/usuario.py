class Usuarios:
    def __init__(self, nombre, nickname, clave):
        self.nombre = nombre
        self.nickname = nickname
        self.clave = clave


    lista_usuarios = []


    @classmethod
    def guardarUsuario(cls, nombre, nickname, clave):
        usuario = Usuarios(nombre, nickname, clave)
        cls.lista_usuarios.append(usuario)
