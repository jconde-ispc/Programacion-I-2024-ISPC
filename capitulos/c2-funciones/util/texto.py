import string
import re #espresiones regulares

def contiene_mayuscula(texto):
  """Verifica si una cadena contiene al menos una letra mayúscula.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos una mayúscula, False en caso contrario.
  """

  return any(caracter.isupper() for caracter in texto)

def contiene_mayuscula_(texto):
  """Verifica si una cadena contiene al menos una letra mayúscula.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos una mayúscula, False en caso contrario.
  """

  for caracter in texto:
    if caracter.isupper():
      return True
  return False

def contiene_minuscula(texto):
  """Verifica si una cadena contiene al menos una letra minúscula.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos una minúscula, False en caso contrario.
  """

  return any(caracter.islower() for caracter in texto)

def contiene_minuscula_(texto):
  """Verifica si una cadena contiene al menos una letra minúscula.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos una minúscula, False en caso contrario.
  """

  for caracter in texto:
    if caracter.islower():
      return True
  return False

def contiene_mayusculas_y_minusculas(texto):
  """Verifica si una cadena contiene al menos una mayúscula y una minúscula.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos una mayúscula y una minúscula, False en caso contrario.
  """

  tiene_mayuscula = any(c.isupper() for c in texto)
  tiene_minuscula = any(c.islower() for c in texto)
  return tiene_mayuscula and tiene_minuscula

def contiene_caracteres_especiales(texto):
  """Verifica si una cadena contiene caracteres especiales.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos un carácter especial, False en caso contrario.
  """

  caracteres_validos = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ')
  return any(c not in caracteres_validos for c in texto)



def contiene_caracteres_especiales_string(texto):
  """Verifica si una cadena contiene caracteres especiales.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos un carácter especial, False en caso contrario.
  """

  caracteres_validos = string.ascii_letters + string.digits + ' '
  return any(c not in caracteres_validos for c in texto)

def contiene_caracteres_especiales_re(texto):
  """Verifica si una cadena contiene caracteres especiales.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos un carácter especial, False en caso contrario.
  """

  patron = r"[^\w\s]"  # Coincide con cualquier carácter que no sea alfanumérico o espacio
                    # r"[^\w\s]": Esta expresión regular busca cualquier carácter que no esté en el conjunto
                    #  de caracteres alfanuméricos (\w) o espacios en blanco (\s).
  return bool(re.search(patron, texto))


def contiene_numero_entero_positivo(texto):
  """Verifica si una cadena contiene al menos un número.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos un número, False en caso contrario.
  """

  for caracter in texto:
    if caracter.isdigit():
      return True
  return False

def contiene_numero_entero_positivo_re(texto):
  """Verifica si una cadena contiene al menos un número.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos un número, False en caso contrario.
  """

  patron = r"\d"  # Coincide con cualquier dígito
  return bool(re.search(patron, texto))

def contiene_numero_entero_positivo_set(texto):
  """Verifica si una cadena contiene al menos un número.

  Args:
    texto: La cadena de texto a evaluar.

  Returns:
    True si hay al menos un número, False en caso contrario.
  """

  digitos = set('0123456789')
  return any(c in digitos for c in texto)

def es_numero(cadena):
  """Verifica si una cadena representa un número.

  Args:
    cadena: La cadena a evaluar.

  Returns:
    True si la cadena es un número, False en caso contrario.
  """

  try:
    float(cadena)  # Intenta convertir la cadena a float
    return True
  except ValueError:
    return False
  
def es_numero_re(cadena):
  """Verifica si una cadena representa un número.

  Args:
    cadena: La cadena a evaluar.

  Returns:
    True si la cadena es un número, False en caso contrario.
  """

  patron = r"^-?\d+(\.\d+)?$"  # Permite números enteros, decimales, positivos y negativos
  """ 
  ^-?\d+(\.\d+)?$: Esta expresión regular permite:
        Un signo menos opcional al principio (^-?).
        Uno o más dígitos (\d+).
        Un punto decimal opcional seguido de uno o más dígitos ((\.\d+)?).
        El ^ y el $ aseguran que toda la cadena coincida con el patrón.
  """
  return bool(re.fullmatch(patron, cadena))