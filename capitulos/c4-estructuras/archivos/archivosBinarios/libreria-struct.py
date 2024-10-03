import struct

""" 
Explicación de las nuevas funciones:

modificar_libro: Busca el libro por ISBN y sobrescribe el registro con los nuevos datos.
eliminar_libro: Lee todos los libros, excepto el que queremos eliminar, y luego sobrescribe
 el archivo
 con los libros restantes.
contar_libros: Calcula el tamaño del archivo y lo divide por el tamaño de un registro 
para obtener la cantidad de libros.
Ventajas de usar struct:

Eficiencia: Es más eficiente que manipular los bytes manualmente.
Claridad: El código es más legible y conciso.
Flexibilidad: Podemos definir formatos más complejos para almacenar datos de diferentes tipos.
Portabilidad: El formato de los datos puede ser más portátil entre diferentes sistemas.
Consideraciones:

Tamaño fijo: En este ejemplo, asumimos un tamaño fijo para cada campo. Para campos de 
longitud variable, se pueden utilizar códigos de longitud variable o almacenar la 
longitud de la cadena antes de la cadena misma.
Orden de bytes: La letra ! al principio del formato indica que se utiliza el orden de 
bytes de red (big-endian).
Alineación: Es importante tener en cuenta la alineación de los datos para evitar problemas
 de portabilidad.
Eficiencia: Para archivos muy grandes, considerar un índice para buscar libros por ISBN 
puede mejorar el rendimiento.
Este código proporciona una implementación completa y eficiente para gestionar un archivo
 de libros utilizando struct.
"""


def guardar_libro(libro, archivo='libreria.dat', posicion=None):
    """Guarda un libro en el archivo binario.

    Args:
        libro: Diccionario con los datos del libro.
        archivo: Nombre del archivo binario.
        posicion: Posición donde se insertará el libro (opcional).
    """
    formato = '!4s20s13s20s'  # Formato para cada registro: 4s (longitud del autor), 20s (autor), 13s (ISBN), 20s (editorial)
    registro_size = struct.calcsize(formato)

    with open(archivo, 'rb+' if posicion is not None else 'ab') as f:
        if posicion is not None:
            f.seek(posicion * registro_size)

        datos = struct.pack(formato, 
                           bytes(len(libro['autor'])), libro['autor'].encode('utf-8'),
                           bytes(len(libro['titulo'])), libro['titulo'].encode('utf-8'),
                           libro['isbn'].encode('utf-8'),
                           bytes(len(libro['editorial'])), libro['editorial'].encode('utf-8'))
        f.write(datos)

def leer_libro(archivo, posicion):
    """Lee un libro del archivo binario."""
    formato = '!4s20s13s20s'
    registro_size = struct.calcsize(formato)

    with open(archivo, 'rb') as f:
        f.seek(posicion * registro_size)
        datos = f.read(registro_size)
        autor_len, autor, titulo_len, titulo, isbn, editorial_len, editorial = struct.unpack(formato, datos)
        return {'autor': autor.decode('utf-8').rstrip('\x00'),
                'titulo': titulo.decode('utf-8').rstrip('\x00'),
                'isbn': isbn.decode('utf-8'),
                'editorial': editorial.decode('utf-8').rstrip('\x00')}

def modificar_libro(isbn, nuevo_libro, archivo='libreria.dat'):
    """Modifica un libro en el archivo binario."""
    formato = '!4s20s13s20s'
    registro_size = struct.calcsize(formato)

    with open(archivo, 'rb+') as f:
        for i in range(contar_libros(archivo)):
            libro = leer_libro(archivo, i)
            if libro['isbn'] == isbn:
                f.seek(i * registro_size)
                datos = struct.pack(formato, 
                                   bytes(len(nuevo_libro['autor'])), nuevo_libro['autor'].encode('utf-8'),
                                   bytes(len(nuevo_libro['titulo'])), nuevo_libro['titulo'].encode('utf-8'),
                                   nuevo_libro['isbn'].encode('utf-8'),
                                   bytes(len(nuevo_libro['editorial'])), nuevo_libro['editorial'].encode('utf-8'))
                f.write(datos)
                break

def eliminar_libro(isbn, archivo='libreria.dat'):
    """Elimina un libro del archivo binario."""
    # Por simplicidad, sobreescribimos el archivo sin dejar huecos
    formato = '!4s20s13s20s'
    registro_size = struct.calcsize(formato)

    libros = []
    with open(archivo, 'rb') as f:
        for i in range(contar_libros(archivo)):
            libro = leer_libro(archivo, i)
            if libro['isbn'] != isbn:
                libros.append(libro)

    with open(archivo, 'wb') as f:
        for libro in libros:
            guardar_libro(libro, archivo)

def contar_libros(archivo='libreria.dat'):
    """Cuenta la cantidad de libros en el archivo."""
    formato = '!4s20s13s20s'
    registro_size = struct.calcsize(formato)

    try:
        with open(archivo, 'rb') as f:
            f.seek(0, 2)  # Ir al final del archivo
            return f.tell() // registro_size
    except FileNotFoundError:
        return 0

# Ejemplo de uso:
libro1 = {'autor': 'García Márquez', 'titulo': 'Cien Años de Soledad', 'isbn': '12345', 'editorial': 'Planeta'}
guardar_libro(libro1)
libro2 = {'autor': 'Orwell', 'titulo': '1984', 'isbn': '67890', 'editorial': 'Debolsillo'}
guardar_libro(libro2)
modificar_libro('12345', {'autor': 'Nuevo Autor', 'titulo': 'Nuevo Título', 'isbn': '12345', 'editorial': 'Nueva Editorial'})
eliminar_libro('67890')