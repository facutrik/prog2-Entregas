class Biblioteca:
    def __init__ (self):
        self.libros = []
        self.miembros = []

    def agregar_libros(self, libro):
        self.libros.append(libro)

    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)

    def buscar_miembro(self, dni):
        for m in self.miembros:
            if m.dni == dni:
                return m
        return None

    def buscar_libro(self, titulo):
        for l in self.libros:
            if l.titulo == titulo:
                return l
        return None

    def estado_libros(self):
        print("Estado de libros: ")
        for libro in self.libros:
            if libro.disponible:
                print(f"{libro.titulo} - Disponible")
            else:
                print(f"{libro.titulo} - Prestado a {libro.prestadoA.nombre}")

    def estado_miembros(self):
        print("Estado de miembros")
        for m in self.miembros:
            for l in m.libro_prestado:
                print(f"{m.nombre} - Libros: {l.titulo}")
