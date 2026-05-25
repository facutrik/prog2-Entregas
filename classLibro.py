class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestadoA = None

    def prestar(self, miembro):
        if self.disponible:
            self.disponible = False
            self.prestadoA = miembro
            return True
        return False

    def devolver(self):
        self.disponible = True
        self.prestadoA = None