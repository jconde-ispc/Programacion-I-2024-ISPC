def selection_sort(arr):
    n = len(arr)  # Obtiene la longitud del arreglo
    print(f"El arreglo desordenado es {arr}. Ordenamos con seleccion")
    for i in range(n):  # Itera sobre el arreglo
        min_idx = i  # Supone que el elemento actual es el mínimo
        for j in range(i+1, n):  # Busca el mínimo en el resto del arreglo
            if arr[j] < arr[min_idx]:  # Si encuentra un nuevo mínimo
                min_idx = j  # Actualiza el índice del mínimo
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambia el mínimo con el elemento actual
        print(f"Intercambia el mínimo con el elemento actual {arr[i]} con {arr[min_idx]}")
        print(f"El arreglo ahora es {arr}")
    return arr  # Retorna el arreglo ordenado

def bubble_sort(arr):
    n = len(arr)  # Obtiene la longitud del arreglo
    print(f"El arreglo desordenado es {arr}. Ordenamos con burbuja")
    for i in range(n):  # Itera sobre el arreglo
        for j in range(0, n-i-1):  # Itera sobre los elementos restantes
            if arr[j] > arr[j+1]:  # Compara elementos adyacentes
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Intercambia si están en el orden incorrecto
                print(f"Intercambia si están en el orden incorrecto {arr[j]} con {arr[j+1]}")
        print(f"El arreglo ahora es {arr}") # esto puede mejorarse mucho y terminar antes, no siempre es necesario imprimirlo, puede no entrar al ciclo.
    return arr  # Retorna el arreglo ordenado


"""
En esta versión mejorada, se agrega la variable  swapped  que se actualiza a  True  si se realiza algún intercambio durante una iteración.
 Si al finalizar una iteración no se ha realizado ningún intercambio (es decir,  swapped  sigue siendo  False ),
 el algoritmo termina prematuramente ya que el arreglo ya está ordenado.
"""
def bubble_sort_mejorado(arr):
    n = len(arr)
    print(f"El arreglo desordenado es {arr}. Ordenamos con burbuja mejorado")
    for i in range(n):
        swapped = False  # Variable para indicar si se realizó algún intercambio en esta iteración
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Se realizó un intercambio, por lo tanto, se actualiza la variable swapped
        print(f"El arreglo ahora es {arr}")
        if not swapped:
            print(f"El arreglo ya esta ordenado, sale del bucle sabiendo que le queda por iterar {n - i} elementos")
            break  # Si no se realizó ningún intercambio en esta iteración, el arreglo ya está ordenado
    return arr



def insertion_sort(arr):
    print(f"El arreglo desordenado es {arr}. Ordenamos con inserción")
    for i in range(1, len(arr)):  # Itera sobre el arreglo desde el segundo elemento
        key = arr[i]  # Almacena el valor actual
        j = i - 1  # Inicializa el índice del elemento anterior
        intercambio = False
        while j >= 0 and key < arr[j]:  # Mueve los elementos mayores al valor actual
            arr[j + 1] = arr[j]  # Desplaza el elemento hacia la derecha
            j -= 1  # Actualiza el índice
            intercambio = True
        if intercambio:
            print(f"Intercambia el elemento {arr[j + 1]} con {key}")
            arr[j + 1] = key  # Inserta el valor en la posición correcta
            print(f"El arreglo ahora es {arr}")
        else:  # No se realizó intercambio
            print(f"No se realizó intercambio, el elemento {key} ya está en la ubicación correcta")
    print(f"El arreglo ordenado es {arr}")
    return arr  # Retorna el arreglo ordenado


def quick_sort(arr):
    if len(arr) <= 1:  # Caso base: arreglo vacío o con un solo elemento
        return arr
    pivot = arr[len(arr) // 2]  # Selecciona un pivote (usualmente el elemento central)
    left = [x for x in arr if x < pivot]  # Elementos menores que el pivote
    middle = [x for x in arr if x == pivot]  # Elementos iguales al pivote
    right = [x for x in arr if x > pivot]  # Elementos mayores que el pivote
    return quick_sort(left) + middle + quick_sort(right)  # Combina los subarreglos ordenados

def quick_sort_largo(arr):
    if len(arr) <= 1:  # Caso base: si el arreglo es vacío o tiene un solo elemento, no es necesario ordenarlo
        return arr

    pivot = arr[len(arr) // 2]  # Selecciona el pivote como el elemento en la mitad del arreglo
    print(f"El arreglo es {arr} y el elemepnto pivote es {pivot}, Selecciona el pivote como el elemento en la mitad del arreglo")
    left = []  # Arreglo para almacenar elementos menores que el pivote
    middle = []  # Arreglo para almacenar elementos iguales al pivote
    right = []  # Arreglo para almacenar elementos mayores que el pivote

    # Partición del arreglo en los subarreglos left, middle y right
    for x in arr:
        print(f"El pivote es {pivot} y el elemento actual es {x}")
        if x < pivot:
            left.append(x)
            print(f"Agrega elemento actual {x} a left")
        elif x == pivot:
            middle.append(x)
            print(f"Agrega elemento actual {x} a middle")
        else:
            right.append(x)
            print(f"Agrega elemento actual {x} a right")

    # Imprime información sobre el pivote y los subarreglos en cada paso de la partición
    print("Pivote:", pivot)
    print("Izquierda:", left)
    print("Medio:", middle)
    print("Derecha:", right)

    # Llamadas recursivas para ordenar los subarreglos izquierdo y derecho
    return quick_sort_largo(left) + middle + quick_sort_largo(right)  # Combina los subarreglos ordenados
