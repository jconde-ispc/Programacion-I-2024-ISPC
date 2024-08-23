values = [2, 3, 4]
def square_it(values):
    # CUIDADO CON ESTO !!!
    for i in range(len(values)):
        values[i] **= 2
    return values

square_it(values) #Solo invoca, no asigna el retorno, sin embargo...
print(values) #[4, 9, 16]

#...sin embargo las listas son mutables. Tipo de pasaje en este 
# caso es dato-resultado o referencia (no hay copia)