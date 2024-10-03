import random

def es_par(numero):
  """Verifica si un número es par.

  Args:
    numero: El número a evaluar.

  Returns:
    True si el número es par, False en caso contrario.
  """

  return numero % 2 == 0

def numero_aleatorio(limite_inferior, limite_superior):
  """Genera un número aleatorio entre dos límites (inclusivos).

  Args:
    limite_inferior: Límite inferior del rango.
    limite_superior: Límite superior del rango.

  Returns:
    Un número aleatorio entre los límites especificados.
  """

  return random.randint(limite_inferior, limite_superior)

def generar_lista_aleatoria(n, limite_inferior, limite_superior):
  """Genera una lista de n números aleatorios entre dos límites.

  Args:
    n: Cantidad de números aleatorios a generar.
    limite_inferior: Límite inferior del rango.
    limite_superior: Límite superior del rango.

  Returns:
    Una lista con n números aleatorios.
  """

  lista_aleatoria = []
  for _ in range(n):
    numero_aleatorio = random.randint(limite_inferior, limite_superior)
    lista_aleatoria.append(numero_aleatorio)
  return lista_aleatoria

#retornar un valor aleatorio de una lista: la función choice nos permite elegir un elemento aleatorio de una lista

def factorial(numero):
  """Calcula el factorial de un número.

  Args:
    numero: El número cuyo factorial se calculará.

  Returns:
    El factorial del número.
  """

  if numero == 0:
    return 1
  else:
    return numero * factorial(numero - 1)
  

def es_primo(numero):
  """Verifica si un número es primo.

  Args:
    numero: El número a evaluar.

  Returns:
    True si el número es primo, False en caso contrario.
  """

  if numero <= 1:
    return False
  for i in range(2, int(numero**0.5) + 1): #(numero**0.5)Calcula la raíz cuadrada del número.
    if numero % i == 0:
      return False
  return True
""" 
¿Por qué hasta la raíz cuadrada?

Optimización: No es necesario comprobar la divisibilidad de un número por todos los números menores que él.
 Si un número n no es primo, entonces tiene al menos un divisor mayor que 1 y menor o igual a su raíz cuadrada.
   Si no encontramos ningún divisor en este rango, entonces el número es primo.
Es una optimización clave para determinar si un número es primo, evitando realizar cálculos innecesarios
 y mejorando la eficiencia del algoritmo.
"""


def fibonacci(n):
  """Genera la serie de Fibonacci hasta el término n.

  Args:
    n: El número de términos de la serie.

  Returns:
    Una lista con los primeros n términos de la serie de Fibonacci.
  """

  if n <= 0:
    return []
  elif n == 1:
    return [0]
  else:
    fib = [0, 1]
    for i in range(2, n):
      fib.append(fib[i-1] + fib[i-2])
    return fib
  
def test():
    # Verificar si un número es par
    numero = 10
    print(es_par(numero))  # Imprime True

    # Generar un número aleatorio entre 1 y 100
    nro_aleatorio = numero_aleatorio(1, 100)
    print(nro_aleatorio)

    lista = generar_lista_aleatoria(10, 1, 100)
    print(lista)

    print(f"la función choice nos permite elegir un elemento aleatorio de una lista {random.choice(lista)=}")

    # Calcular el factorial de 5
    factorial_5 = factorial(5)
    print(factorial_5)

    # Verificar si 7 es primo
    es_primo_7 = es_primo(7)
    print(es_primo_7)

    # Generar los primeros 10 términos de la serie de Fibonacci
    fibonacci_10 = fibonacci(10)
    print(fibonacci_10)

if __name__ == '__main__':
    test()