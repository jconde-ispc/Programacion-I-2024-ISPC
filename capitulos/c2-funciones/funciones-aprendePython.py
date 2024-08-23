def empty():
    x = 0 # return None
print(empty()) #None

def quick():
    return

print(quick())#None

def multiple():
    return 0, 1 # es una tupla!

result = multiple()
print(type(result))#tuple
print(result)

a, b = multiple()# a=0 y b=1

def _min(a, b):
    if a < b:
        return a
    else:
        return b

_min(7, 9)# 7
"""Nótese que la sentencia return puede escribirse en múltiples ocasiones y puede encontrarse
en cualquier lugar de la función, no necesariamente al final del cuerpo. Esta técnica puede
ser beneficiosa en distintos escenarios.
Uno de esos escenarios se relaciona con el concepto de cláusula guarda: una pieza de código
que normalmente está al comienzo de la función y comprueba una serie de condiciones para
continuar con la ejecución o cortarla"""

#Teniendo en cuenta que la sentencia return finaliza la ejecución de una función, es viable
#eliminar la sentencia else del ejemplo visto anteriormente

def _min2(a, b):
    if a < b:
        return a
    return b

_min2(7, 9)# 7

def build_cpu(vendor, num_cores, freq):
    return dict(vendor=vendor,num_cores=num_cores,freq=freq)

#Argumentos posicionales
build_cpu('AMD', 8, 2.7) #{ vendor : AMD , num_cores : 8,freq : 2.7}
build_cpu(8, 2.7, 'AMD' )#{ vendor : 8, num_cores : 2.7,freq :'AMD' }

#Argumentos con nombre
build_cpu(vendor='AMD', num_cores=8, freq=2.7 )#{ vendor : AMD , num_cores : 8,freq : 2.7}
build_cpu(num_cores=8, freq=2.7, vendor= 'AMD' )#{ vendor : AMD , num_cores : 8, freq : 2.7}

#mezcla de argumentos posicionales y nombre
build_cpu('AMD', 8, freq=2.7)#{ vendor : AMD , num_cores : 8,freq : 2.7}
build_cpu( 'INTEL' , freq=3.1,num_cores=4)#{ vendor : INTEL , num_cores : 4,freq : 3.1}
#build_cpu(num_cores=4, 'INTEL' , freq=3.1)#File "<stdin>", line 1 SyntaxError: positional argument follows keyword argument

#Argumentos por defecto
build_cpu('AMD', freq=2.7, num_cores=8)#{ vendor : AMD , num_cores : 8,freq : 2.7}

def build_cpu2(vendor, num_cores, freq=2.0):
    return dict(vendor=vendor,num_cores=num_cores,freq=freq)

build_cpu2('AMD', 8)#{ vendor : AMD , num_cores : 8,freq : 2.0}
build_cpu('INTEL', 2, 3.4)#{ vendor : INTEL , num_cores : 2,freq : 3.4}


# ---- Los valores por defecto en los parámetros se calculan cuando se define la función, no cuando se ejecuta.

DEFAULT_FREQ = 2.0
def build_cpu3(vendor, num_cores, freq=DEFAULT_FREQ):
    return dict(vendor=vendor,num_cores=num_cores,freq=freq)

build_cpu3( 'AMD' , 4)#{ vendor : AMD , num_cores : 4,freq : 2.0}

DEFAULT_FREQ = 3.5
build_cpu3( 'AMD' , 4)#{ vendor : AMD , num_cores : 4,freq : 2.0}





