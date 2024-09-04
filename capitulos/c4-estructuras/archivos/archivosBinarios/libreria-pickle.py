import pickle #Este módulo se utiliza para serializar y deserializar objetos de Python, 
                    #lo que permite guardarlos en archivos binarios.

def crear_libro(autor, titulo, isbn, editorial):
  """Crea un diccionario representando un libro."""
  return {'autor': autor, 'titulo': titulo, 'isbn': isbn, 'editorial': editorial}

def guardar_libro(libro, archivo='libreria.dat', posicion=None):
  """Guarda un libro en el archivo binario.

  Args:
    libro: Diccionario con los datos del libro.
    archivo: Nombre del archivo binario.
    posicion: Posición donde se insertará el libro (opcional).
  """

  try:
    with open(archivo, 'rb+') as f:
      libros = pickle.load(f)
      if posicion is not None:
        libros.insert(posicion, libro)
      else:
        libros.append(libro)
      f.seek(0)
      pickle.dump(libros, f)
  except EOFError:
    with open(archivo, 'wb') as f:
      pickle.dump([libro], f)

def modificar_libro(isbn, nuevo_libro, archivo='libreria.dat'):
  """Modifica un libro en el archivo binario.

  Args:
    isbn: ISBN del libro a modificar.
    nuevo_libro: Nuevo diccionario con los datos del libro.
    archivo: Nombre del archivo binario.
  """

  with open(archivo, 'rb+') as f:
    libros = pickle.load(f)
    for i, libro in enumerate(libros):
      if libro['isbn'] == isbn:
        libros[i] = nuevo_libro
        break
    f.seek(0)
    pickle.dump(libros, f)

def eliminar_libro(isbn, archivo='libreria.dat'):
  """Elimina un libro del archivo binario.

  Args:
    isbn: ISBN del libro a eliminar.
    archivo: Nombre del archivo binario.
  """

  with open(archivo, 'rb+') as f:
    libros = pickle.load(f)
    libros = [libro for libro in libros if libro['isbn'] != isbn]
    f.seek(0)
    pickle.dump(libros, f)

def eliminar_ultimo_libro(archivo='libreria.dat'):
  """Elimina el último libro del archivo binario."""

  with open(archivo, 'rb+') as f:
    libros = pickle.load(f)
    libros.pop()
    f.seek(0)
    pickle.dump(libros, f)

def eliminar_archivo(archivo='libreria.dat'):
  """Elimina el archivo binario."""
  import os
  os.remove(archivo)

# Ejemplo de uso:
libro1 = crear_libro("Autor1", "Título1", "ISBN123", "Editorial1")
libro2 = crear_libro("Autor2", "Título2", "ISBN456", "Editorial2")

guardar_libro(libro1)
guardar_libro(libro2, posicion=0)  # Insertar al principio

modificar_libro("ISBN123", crear_libro("Nuevo Autor", "Nuevo Título", "ISBN123", "Nueva Editorial"))

eliminar_libro("ISBN456")
eliminar_ultimo_libro()

eliminar_archivo()  # Eliminar el archivo al finalizar