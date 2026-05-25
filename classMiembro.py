class Miembro:
    def __init__(self, nombre, id):
        self.nombre = nombre 
        self.dni = id
        self.libro_prestado = []

    def tomar_libro(self, libro):
        if libro.prestar(self):
            self.libro_prestado.append(libro)
            print(f"{self.nombre} tomo prestado '{libro.titulo}'")
        else: 
            print(f"El libro {libro.titulo} no esta disponible")

    def devolver_libro(self, libro):
        if libro in self.libro_prestado:
            libro.devolver()
            self.libro_prestado.remove(libro)
            print(f"{self.nombre} devolvio '{libro.titulo}'")
        else:
            print(f"{self.nombre} no tiene ese libro")