import moduloEjemplo as modEjemplo

modEjemplo.pedirNumero()


while True:
    nombre = input('Ingrese un nombre')
    mensaje = input('Ingrese un mensaje')

    modEjemplo.saludar(nombre,mensaje)

    opcion = input('¿Salir? s/n')
    if(opcion == 's'):
        print('Termino')
        break
