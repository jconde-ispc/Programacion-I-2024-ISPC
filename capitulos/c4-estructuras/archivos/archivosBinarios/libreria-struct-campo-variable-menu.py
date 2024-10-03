import struct
import libreria_struct_campos_long_variables as lib


def menu():
    print("1. Agregar libro")
    print("2. Buscar libro por ISBN")
    print("3. Modificar libro")
    print("4. Eliminar libro")
    print("5. Listar todos los libros (ordenados por título)")
    print("6. Salir")
    return int(input("Ingrese una opción: "))

def ejecutar_opcion(opcion):
    if opcion == 1:
        libro = {}
        libro['autor'] = input("Ingrese el autor: ")
        libro['titulo'] = input("Ingrese el título: ")
        libro['isbn'] = input("Ingrese el ISBN: ")
        libro['editorial'] = input("Ingrese la editorial: ")
        lib.guardar_libro(libro)
        print("Libro agregado correctamente.")
    elif opcion == 2:
        isbn = input("Ingrese el ISBN a buscar: ")
        for i in range(lib.contar_libros()):
            libro = lib.leer_libro(i)
            if libro['isbn'] == isbn:
                print(libro)
                return
        print("Libro no encontrado.")
    elif opcion == 3:
        isbn = input("Ingrese el ISBN del libro a modificar: ")
        for i in range(lib.contar_libros()):
            libro = lib.leer_libro(i)
            if libro['isbn'] == isbn:
                nuevo_libro = {}
                nuevo_libro['autor'] = input("Nuevo autor (deje en blanco para no modificar): ") or libro['autor']
                # ... (solicitar los demás datos)
                lib.modificar_libro(isbn, nuevo_libro)
                print("Libro modificado correctamente.")
                return
        print("Libro no encontrado.")
    elif opcion == 4:
        isbn = input("Ingrese el ISBN del libro a eliminar: ")
        lib.eliminar_libro(isbn)
        print("Libro eliminado correctamente.")
    elif opcion == 5:
        libros = []
        for i in range(lib.contar_libros()):
            libros.append(lib.leer_libro(i))
        libros.sort(key=lambda x: x['titulo'])  # Ordenar por título
        for libro in libros:
            print(libro)
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == 6:
            break
        ejecutar_opcion(opcion)