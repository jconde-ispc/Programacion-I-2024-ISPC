"""
Los programas están formados por código y datos. Pero a nivel interno de la memoria del
ordenador no son más que ufna secuencia de bits. La interpretación de estos bits depende del
lenguaje de programación, que almacena en la memoria no sólo el puro dato sino distintos
metadatos.1
Cada «trozo» de memoria contiene realmente un objeto, de ahí que se diga que en Python
todo son objetos. Y cada objeto tiene, al menos, los siguientes campos:
• Un tipo del dato almacenado.
• Un identificador único para distinguirlo de otros objetos.
• Un valor consistente con su tipo.

Las variables son fundamentales ya que permiten definir nombres para los valores que
tenemos en memoria y que vamos a usar en nuestro programa.


Las variables son nombres, no lugares. Detrás de esta frase se esconde la reflexión de que
cuando asignamos un valor a una variable, lo que realmente está ocurriendo es que se hace
apuntar el nombre de la variable a una zona de memoria en el que se representa el objeto
(con su valor)
"""
#MUTABILIDAD
a = 10
b = a

print("11111 el id de a es {id(a)}")
print(f"11111 el id de b es {id(b)}")

a = 5

print(f"2222 el id de a es {id(a)}")
print(f"2222 el id de b es {id(b)}")

print(f"El valor de la variable a es {a}") #5
print (f"El valor de la variable b es {b}") #?

"""
Cuando la zona de memoria que ocupa el objeto se puede modificar hablamos de tipos de
datos mutables. En otro caso hablamos de tipos de datos inmutables.
Por ejemplo, las listas son un tipo de dato mutable ya que podemos modificar su contenido
(aunque la asignación de un nuevo valor sigue generando un nuevo espacio de memoria).

Importante: El hecho de que un tipo de datos sea inmutable significa que no podemos
modificar su valor «in-situ», pero siempre podremos asignarle un nuevo valor (hacerlo apuntar
a otra zona de memoria).
"""
