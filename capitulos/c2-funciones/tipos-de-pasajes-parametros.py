def cuadrado(x):
    x= x**2
    return x

def cubo(x):
    x= x**3
    return x

#values = [2, 3, 4]
def square_it(values):
    # CUIDADO CON ESTO !!!
    for i in range(len(values)):
        values[i] **= 2
    return values


if __name__ == '__main__':
    y = 2
    print(f"{y=}")
    print(f"{cuadrado(y)=}")
    print(f"{y=}")
    print(f"{cubo(y)=}")
    print(f"{y=}")
    
    values = [2, 3, 4]
    print(f"{values=}") #[2, 3, 4]
    square_it(values) #Solo invoca, no asigna el retorno, sin embargo...
    print(f"{values=}") #[4, 9, 16]


# los enteros no son mutables, por lo tanto el tipo de pasaje de parametro es por copia o valor. Dato 
# las listas son mutables. Tipo de pasaje en este caso es dato-resultado o referencia (no hay copia)