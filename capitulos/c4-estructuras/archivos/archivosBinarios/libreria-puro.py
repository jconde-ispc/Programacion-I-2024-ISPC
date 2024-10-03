""" 
Formato fijo: En este ejemplo, se asume un tamaño fijo de 80 bytes por registro. Se puede ajustar este tamaño según las necesidades.
Codificación: Se utiliza encode('utf-8') para convertir las cadenas a bytes.
Posicionamiento: Se utiliza seek para posicionarnos en el archivo antes de leer o escribir.
Decodificación: Leemos los bytes y los decodificamos según el formato definido.

Desventajas de este enfoque:
Rigidez: El formato es fijo y difícil de modificar sin reescribir gran parte del código.
Eficiencia: Para archivos grandes, leer y escribir bytes puede ser menos eficiente que utilizar bibliotecas como struct.
Error prone: Es fácil cometer errores al calcular los offsets y tamaños de los campos.

Consideraciones adicionales:
Estructura de datos: Para almacenar una lista de libros, puedes utilizar un archivo de índice que almacene las posiciones
 de cada libro en el archivo de datos.
Optimizaciones: Para mejorar el rendimiento, puedes utilizar búferes para leer y escribir grandes bloques de datos.

Conclusión:
Aunque este enfoque es más bajo nivel y requiere más código, te brinda un control completo sobre el formato de los datos y
 cómo se almacenan en el archivo. Es una buena opción si necesitas un formato personalizado y quieres evitar las dependencias
   de bibliotecas externas.
"""



def guardar_libro(libro, archivo='libreria.dat', posicion=None):
    """Guarda un libro en el archivo binario.

    Args:
        libro: Diccionario con los datos del libro.
        archivo: Nombre del archivo binario.
        posicion: Posición donde se insertará el libro (opcional).
    """
    registro_size = 80  # Tamaño fijo de un registro en bytes
    with open(archivo, 'rb+' if posicion is not None else 'ab') as f:
        if posicion is not None:
            f.seek(posicion * registro_size)
        
        # Codificar los datos del libro a bytes
        datos = (
            str(len(libro['autor'])).encode('utf-8'),
            libro['autor'].encode('utf-8'),
            str(len(libro['titulo'])).encode('utf-8'),
            libro['titulo'].encode('utf-8'),
            libro['isbn'].encode('utf-8'),
            str(len(libro['editorial'])).encode('utf-8'),
            libro['editorial'].encode('utf-8')
        )

        # Completar el registro con espacios en blanco si es necesario
        while len(b''.join(datos)) < registro_size:
            datos.append(b' ')

        f.write(b''.join(datos))

def leer_libro(archivo, posicion):
    """Lee un libro del archivo binario."""
    registro_size = 80
    with open(archivo, 'rb') as f:
        f.seek(posicion * registro_size)
        datos = f.read(registro_size)

        offset = 0
        def leer_campo(datos, offset):
            longitud = int(datos[offset:offset+4].decode('utf-8'))
            valor = datos[offset+4:offset+4+longitud].decode('utf-8')
            return valor, offset+4+longitud

        autor, offset = leer_campo(datos, offset)
        titulo, offset = leer_campo(datos, offset)
        isbn, offset = leer_campo(datos, offset)
        editorial, _ = leer_campo(datos, offset)

        return {'autor': autor, 'titulo': titulo, 'isbn': isbn, 'editorial': editorial}

def modificar_libro(isbn, nuevo_libro, archivo='libreria.dat'):
    """Modifica un libro en el archivo binario."""
    for i in range(contar_libros(archivo)):
        libro = leer_libro(archivo, i)
        if libro['isbn'] == isbn:
            guardar_libro(nuevo_libro, archivo, i)
            break

def eliminar_libro(isbn, archivo='libreria.dat'):
    """Elimina un libro del archivo binario."""
    # Por simplicidad, sobreescribimos el archivo sin dejar huecos
    libros = []
    for i in range(contar_libros(archivo)):
        libro = leer_libro(archivo, i)
        if libro['isbn'] != isbn:
            libros.append(libro)
    with open(archivo, 'wb') as f:
        for libro in libros:
            guardar_libro(libro, archivo)

def eliminar_ultimo_libro(archivo='libreria.dat'):
    """Elimina el último libro del archivo binario."""
    # Similar a eliminar_libro, pero sin buscar por ISBN
    libros = []
    for i in range(contar_libros(archivo) - 1):
        libro = leer_libro(archivo, i)
        libros.append(libro)
    with open(archivo, 'wb') as f:
        for libro in libros:
            guardar_libro(libro, archivo)

def contar_libros(archivo='libreria.dat'):
    """Cuenta la cantidad de libros en el archivo."""
    try:
        with open(archivo, 'rb') as f:
            f.seek(0, 2)  # Ir al final del archivo
            return f.tell() // 80  # Dividir por el tamaño de un registro
    except FileNotFoundError:
        return 0

# Ejemplo de uso:
libro1 = {'autor': 'García Márquez', 'titulo': 'Cien Años de Soledad', 'isbn': '12345', 'editorial': 'Planeta'}
guardar_libro(libro1)
libro2 = {'autor': 'Orwell', 'titulo': '1984', 'isbn': '67890', 'editorial': 'Debolsillo'}
guardar_libro(libro2)
modificar_libro('12345', {'autor': 'Nuevo Autor', 'titulo': 'Nuevo Título', 'isbn': '12345', 'editorial': 'Nueva Editorial'})
eliminar_libro('67890')