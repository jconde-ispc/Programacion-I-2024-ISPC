"""
Hay que tener cuidado a la hora de manejar los parámetros que pasamos a una función ya
que podemos obtener resultados indeseados, especialmente cuando trabajamos con tipos de
datos mutables.
Supongamos una función que añade elementos a una lista que pasamos como argumento. La
idea es que si no pasamos la lista, ésta siempre empiece siendo vacía. Y aca veremos que
las listas en python son mutables (son parametros dato-resultado), el tipo de pasaje es por referencia.

"""


def buggy(arg, result=[]):
  result.append(arg)
  print(result)
  print(f"El id de la variable (parametro) result es: {id(result)}")

print("PARTE 1 ----------------------------------")

buggy('a')
#['a']
buggy('b')
#['b']
buggy('a' , [ 'x','y' ,'z' ])#[ 'x' , 'y' , 'z' , 'a' ]
buggy('b' , [ 'x','y' ,'z' ])#[ 'x' , 'y' , 'z' , 'b' ]

#Aparentemente todo está funcionando de manera correcta, pero veamos qué ocurre en las siguientes llamadas:
print("PARTE 2 ----------------------------------")
buggy('a')
#[ a ]

buggy('b') # Se esperaría [´b´]
#[ a , b ]

"""
Obviamente algo no ha funcionado correctamente. Se esperaría que result tuviera una lista
vacía en cada ejecución. Sin embargo esto no sucede por estas dos razones:
1. El valor por defecto se establece cuando se define la función.
2. La variable result apunta a una zona de memoria en la que se modifican sus valores.

Ejecución paso a paso a través de Python Tutor: https://cutt.ly/sBNpVT2
"""

#-----------------------------------
# La forma de arreglar el código anterior utilizando un parámetro con valor por defecto sería
# utilizar un tipo de dato inmutable y tener en cuenta cuál es la primera llamada:

def nonbuggy(arg, result=None):
  if result is None:
    result = []
  result.append(arg)
  print(result)
  print(f"El id de la variable (parametro) result es: {id(result)}")

print("PARTE 3 ----------------------------------")
nonbuggy('a')
#['a']
nonbuggy('b')
#['b']
nonbuggy('a' , [ 'x','y' ,'z' ])
#[ 'x' , 'y' , 'z' , 'a' ]
nonbuggy('b' , [ 'x','y' ,'z' ])
#[ 'x' , 'y' , 'z' , 'b' ]

