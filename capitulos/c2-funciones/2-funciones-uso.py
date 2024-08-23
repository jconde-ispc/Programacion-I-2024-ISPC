import funciones2

funciones2.pedirNumero()


while True:
    nombre = input('Ingrese un nombre')
    mensaje = input('Ingrese un mensaje')

    funciones2.saludar(nombre,mensaje)

    opcion = input('¿Salir? s/n')
    if(opcion == 's'):
        print('Termino')
        break
