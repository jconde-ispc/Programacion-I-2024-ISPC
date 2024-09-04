import struct
import os
path = os.path.dirname(os.path.abspath(__file__)) + "/"
pathArchivo = path+'files/libreria.dat'
""" 
Explicación de las funciones:

guardar_libro: Guarda un libro en el archivo, calculando el tamaño del registro dinámicamente.
leer_libro: Lee un libro del archivo, leyendo la longitud de cada campo antes de leer el valor.
modificar_libro: Busca el libro por ISBN y sobrescribe el registro completo con los nuevos datos.
eliminar_libro: Crea una nueva lista de libros sin el libro a eliminar y sobrescribe el archivo.
contar_libros: Cuenta los libros leyendo el archivo secuencialmente y calculando el tamaño de cada registro.
calcular_tamanio_registro: Calcula el tamaño de un registro dado un diccionario de libro.
Mejoras:

Cálculo dinámico del tamaño del registro: La función calcular_tamanio_registro permite calcular el tamaño exacto de cada registro en función de los datos.
Manejo de errores: Se incluye un manejo básico de errores para evitar caídas inesperadas.
Consideraciones:

Eficiencia: Para archivos muy grandes, podría ser más eficiente utilizar un índice para buscar libros por ISBN.
Flexibilidad: Este código permite almacenar libros con campos de longitud variable de forma flexible.
Complejidad: La gestión de los tamaños variables puede hacer que el código sea un poco más complejo.
"""

def guardar_libro(libro, archivo='libreria.dat', posicion=None):
    """Guarda un libro en el archivo binario.

    Args:
        libro: Diccionario con los datos del libro.
        archivo: Nombre del archivo binario.
        posicion: Posición donde se insertará el libro (opcional).
    """
    with open(path+'files/'+archivo, 'rb+' if posicion is not None else 'ab') as f:
        if posicion is not None:
            f.seek(posicion)

        datos = b''
        for campo in libro.values():
            datos += struct.pack('!i', len(campo))
            datos += campo.encode('utf-8')

        f.write(datos)

def leer_libro(archivo, posicion):
    """Lee un libro del archivo binario."""
    with open(path+'files/'+archivo, 'rb') as f:
        f.seek(posicion)
        
        def leer_campo(f):
            longitud, = struct.unpack('!i', f.read(4))
            return f.read(longitud).decode('utf-8')

        autor = leer_campo(f)
        titulo = leer_campo(f)
        isbn = leer_campo(f)
        editorial = leer_campo(f)

        return {'autor': autor, 'titulo': titulo, 'isbn': isbn, 'editorial': editorial}

def modificar_libro(isbn, nuevo_libro, archivo='libreria.dat'):
    """Modifica un libro en el archivo binario."""
    with open(path+'files/'+archivo, 'rb+') as f:
        for i in range(contar_libros(archivo)):
            libro = leer_libro(archivo, i * calcular_tamanio_registro(libro))
            if libro['isbn'] == isbn:
                f.seek(i * calcular_tamanio_registro(libro))
                guardar_libro(nuevo_libro, archivo, posicion=i * calcular_tamanio_registro(libro))
                break

def eliminar_libro(isbn, archivo='libreria.dat'):
    """Elimina un libro del archivo binario."""
    # Por simplicidad, sobreescribimos el archivo sin dejar huecos
    libros = []
    with open(path+'files/'+archivo, 'rb') as f:
        for i in range(contar_libros(archivo)):
            libro = leer_libro(archivo, i * calcular_tamanio_registro(libro))
            if libro['isbn'] != isbn:
                libros.append(libro)

    with open(path+'files/'+archivo, 'wb') as f:
        for libro in libros:
            guardar_libro(libro, archivo)

def contar_libros(archivo='libreria.dat'):
    """Cuenta la cantidad de libros en el archivo."""
    try:
        with open(path+'files/'+archivo, 'rb') as f:
            contador = 0
            while True:
                try:
                    leer_libro(archivo, contador * calcular_tamanio_registro({'autor': '', 'titulo': '', 'isbn': '', 'editorial': ''}))
                    contador += 1
                except struct.error:
                    break
            return contador
    except FileNotFoundError:
        return 0

def calcular_tamanio_registro(libro):
    """Calcula el tamaño de un registro en bytes."""
    tamanio = 0
    for campo in libro.values():
        tamanio += 4 + len(campo)  # 4 bytes para la longitud + longitud del campo
    return tamanio