import math
import random

def introduce_rango_int(mensaje=''):
    '''
    Devuelve una tupla entera (inf, sup), garantizando inf <= sup.

    Parameters
    ----------
    mensaje : str
        Mensaje por pantalla para indicar el objeto de la solicitud de los valores del rango
    Returns
    -------
    inf, sup : tuple of int
        Tupla con los valores enteros del rango
    Example
    -------
    >>> inf, sup = introduce_rango('Introduce un rango de valores:')
    '''

    print(mensaje)
    while True:
        try:
            inf = int(input('Valor inferior del rango:'))
            sup = int(input('Valor superior del rango:'))
            if inf > sup:
                raise ValueError('No se cumple {} <= {}.'.format(inf, sup))
        except ValueError as error:
            print(error)
        else:
            break
    return inf, sup


#inf, sup = introduce_rango_int()
def introduce_valor_int(inf, sup):
    '''
    Devuelve un valor entero introducido por teclado por el usuario, tal que inf <= valor <= sup

    Parameters
    ----------
    inf, sup : numérico, int
        Valores inferior y superior del rango
    Returns
    -------
    valor : int
        Entero introducido por teclado por el usuario
    Raises
    ------
    ValueError
        Si inf > sup
    Example
    -------
    >>> valor = introduce_valor_int(0, 100)
    '''

    if inf > sup:
        raise ValueError('El rango de valores [{},{}] no cumple inf <= sup'.format(inf, sup))
    while True:
        print('Introduzca un valor entero dentro del rango de valores [{},{}]'.format(inf, sup))
        try:
            valor = int(input('Valor:'))
            if inf > valor or sup < valor:
                raise ValueError('El valor introducido no pertenece al rango [{},{}]'.
                                 format(inf, sup))
        except ValueError as error:
            print(error)
        else:
            break
    return valor


#print(introduce_valor_int(0, 100))

def adivina_numero(inf, sup):
    '''
    Devuelve una tupla con el resultado del proceso de adivinación

    Parameters
    ----------
    inf, sup : numérico, int
        Valores inferior y superior del rango
    Returns
    -------
    exito : bool
        True si se ha acertado el número
    i+1 : int
        Número de intentos empleados
    num_intentos_max : int
        Número de intentos máximos permitidos, en consonancia con el algoritmo de bisección
    valor_a_adivinar : int
        Número pensado por el ordenador
    Example
    -------
    >>> exito, num_intentos, num_intentos_max, valor_a_adivinar = adivina_numero(0, 100)
    '''

    num_intentos_max = int(math.log2(sup-inf+1)+1)
    print('Te daré {} oportunidades para acertar.'.format(num_intentos_max))

    valor_a_adivinar = random.randint(inf, sup)

    exito = False
    for i in range(num_intentos_max):
        valor = introduce_valor_int(inf, sup)
        if valor < valor_a_adivinar:
            print('Debes probar con un valor superior.')
        elif valor > valor_a_adivinar:
            print('Debes probar con un valor inferior.')
        else:
            exito = True
            break

    return exito, i+1, num_intentos_max, valor_a_adivinar


if __name__ == '__main__':
  # Adivinar un número pensado por el ordenador.
  # El usuario elige el rango de valores al que pertenece el número que debe adivinar el programa.
  inf, sup = introduce_rango_int('Introduzca el rango de valores enteros al que pertenece el número que debe adivinarse.')

  exito, num_intentos, num_intentos_max, valor_a_adivinar = adivina_numero(inf, sup)
  if exito:
      print('Has acertado en {} intentos.'.format(num_intentos))
  else:
      print('¡Torpe! Consumiste los {} intentos disponibles.'.format(num_intentos_max))
      print('El número que tenías que adivinar es el {}.'.format(valor_a_adivinar))
