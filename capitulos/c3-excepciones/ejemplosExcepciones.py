# 1) Pedir un número al usuario y devolver el cuadrado del mismo. Si el usuario introduce un valor no numérico, solicitarlo nuevamente.

# 2) Buscar un elemento de la lista
miLista = [1, 3, 5, 7]
posicionElementoBuscado = miLista.index(5)
print(posicionElementoBuscado)

posicionElementoBuscado = miLista.index(25)
print(posicionElementoBuscado)

"""  SALIDA
2
Traceback (most recent call last):
  File "/home/julian/desarrollo/proyectosISPC/Programacion_I-2024-ISPC/capitulos/c3-excepciones/ejemplosExcepciones.py", line 8, in <module>
    posicionElementoBuscado = miLista.index(25)
                              ^^^^^^^^^^^^^^^^^
ValueError: 25 is not in list
"""

""" 
Vemos que usar la función index() resuelve nuestro problema si el valor buscado está en la lista, pero si el valor no está no sólo no devuelve un -1, sino que se produce un error.

El problema es que para poder aplicar la función index() debemos estar seguros de que el valor está en la lista, y para averiguar eso Python nos provee del operador in:

>>> 5 in [1, 3, 5, 7]
True
>>> 20 in [1, 3, 5, 7]
False

"""

