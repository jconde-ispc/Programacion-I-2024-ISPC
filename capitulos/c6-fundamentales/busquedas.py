def busqueda_secuencial(arr, elemento):
    print(f"El arreglo es {arr} y el elemento a buscar es {elemento}")
    for i in range(len(arr)):  # Itera sobre cada elemento del arreglo
        if arr[i] == elemento:  # Compara el elemento actual con el elemento buscado
            print(f"El elemento {elemento} se encuentra en la ubicación {i}. Elemento encontrado!!!")
            return i  # Retorna la posición si se encuentra el elemento
    print(f"El elemento {elemento} no se encuentra en el arreglo")
    return -1  # Retorna -1 si el elemento no se encuentra en el arreglo

def busqueda_binaria(arr, elemento):
    inicio = 0
    fin = len(arr) - 1
    print(f"El arreglo es {arr} y el elemento a buscar es {elemento}")
    while inicio <= fin:
        medio = (inicio + fin) // 2  # Calcula el índice medio del arreglo

        if arr[medio] == elemento:
            print(f"El elemento {elemento} se encuentra en la ubicación {medio}. Elemento encontrado!!!")
            return medio  # Retorna la posición si se encuentra el elemento en el medio
        elif arr[medio] < elemento:
            print(f"El elemento {elemento} es mas grande que {arr[medio]} entonces buscamos en la mitad derecha")
            inicio = medio + 1  # Actualiza el índice de inicio si el elemento está en la mitad derecha
        else:
            print(f"El elemento {elemento} es mas chico que {arr[medio]} entonces buscamos en la mitad izquierda")
            fin = medio - 1  # Actualiza el índice de fin si el elemento está en la mitad izquierda

    return -1  # Retorna -1 si el elemento no se encuentra en el arreglo

