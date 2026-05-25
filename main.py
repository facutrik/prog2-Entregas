from classLibro import Libro
from classMiembro import Miembro
from classBiblioteca import Biblioteca
from menu import mostrar_menu

def main():
    biblioteca = Biblioteca()
    
    while True:
        mostrar_menu()
        opcion = input("\nIngrese la opcion deseada: ")


        if opcion == "1": #Agregar miembro
            while True:
                nombre = input("Nombre: ")
                if nombre == "":
                    print('El nombre no puede estar vacio')
                elif not nombre.replace(" ", "").isalpha():
                    print("El nombre solo debe contener letras")
                else: 
                    break
            while True:
                dni = input("Dni: ")
                if dni == "":
                    print("El DNI no puede estar vacio")
                elif len(dni) < 7 or len(dni) > 8:
                    print("El DNI debe ser numerico entre 7 y 8 digitos.")
                elif not dni.isdigit():
                    print('El DNI solo debe contener numeros')
                else: 
                    dni_existe = False
                    for m in biblioteca.miembros:
                        if m.dni == dni:
                            dni_existe = True
                    if dni_existe: 
                        print('El DNI ingresado ya existe')
                    else:
                        miembro = Miembro(nombre, dni)
                        biblioteca.agregar_miembro(miembro)
                        print('Miembro agregado correctamente.')
                        break


        elif opcion == "2": #Agregar libro
            while True:
                titulo = input("Titulo: ")
                if titulo == "":
                    print('El titulo no puede estar vacio')
                else:
                    libro_encontrado = biblioteca.buscar_libro(titulo)
                    if libro_encontrado:
                        print('El libro ya existe')
                    else:
                        break
            while True:
                autor = input("Autor: ")
                if autor == "":
                    print('El autor no puede estar vacio')
                elif not autor.replace(" ", "").isalpha():
                    print('El autor solo debe contener letras')
                else:
                    break
            while True:
                isbn = input("Isbn: ")
                if isbn == "":
                    print('El isbn no puede estar vacio')
                elif not isbn.isdigit():
                    print('El ISBN solo debe contener numeros')
                elif len(isbn) < 9 or len(isbn) > 14:
                    print('El ISBN debe contener entre 10 a 13 digitos')
                else: 
                    isbn_existe = False
                    for l in biblioteca.libros:
                        if l.isbn == isbn:
                            isbn_existe = True
                    if isbn_existe:
                        print('El ISBN ingresado ya existe')
                    else:
                        libro = Libro(titulo, autor, isbn)
                        biblioteca.agregar_libros(libro)
                        print('Libro agregado correctamente.')
                        break


        elif opcion == "3": #Prestar libro
            miembro_encontrado = None
            libro_encontrado = None
            while True: 
                dni = input("Ingrese DNI del miembro: ")
                miembro_encontrado = biblioteca.buscar_miembro(dni)
                if miembro_encontrado:
                    break
                else:
                    print("El DNI no puede estar vacio y debe ser numerico")
            while True:
                titulo = input("Titulo del libro: ")
                libro_encontrado = biblioteca.buscar_libro(titulo)
                if libro_encontrado:
                    break
                else:
                    print("El titulo no puede estar vacio")
            miembro_encontrado.tomar_libro(libro_encontrado)


        elif opcion == "4": #Devolver libro
            miembro_encontrado = None
            libro_encontrado = None
            while True:
                dni = input('Ingrese DNI del miembro: ')
                miembro_encontrado = biblioteca.buscar_miembro(dni)
                if miembro_encontrado:
                    break
                else:
                    print("Ingrese un DNI válido")
            while True:
                titulo = input("Titulo del libro: ")
                libro_encontrado = biblioteca.buscar_libro(titulo)
                if libro_encontrado:
                    break
                else:
                    print("Libro no encontrado")
            miembro_encontrado.devolver_libro(libro_encontrado)

        
        elif opcion == "5": #Consultar estado libro
            biblioteca.estado_libros()

        
        elif opcion == "6": #Consultar estado miembro
            biblioteca.estado_miembros()

        
        elif opcion == "0": #Salir
            break
        else:
            print ('Opcion inavalida')

if __name__ == "__main__":
    main()
