from algoritmosOrdenamientos import selection_sort, bubble_sort, quick_sort, insertion_sort, quick_sort_largo, bubble_sort_mejorado
from busquedas import busqueda_secuencial, busqueda_binaria

# Test data
arr = [64, 34, 25, 12, 22, 11, 90]

# Selection Sort
print("Selection Sort:")
print(selection_sort(arr[:]))
print("*"*50)

# Bubble Sort
print("Bubble Sort:")
print(bubble_sort(arr[:]))
print("*"*50)

# Bubble Sort
print("Bubble Sort:")
print(bubble_sort_mejorado(arr[:]))
print("*"*50)

# Insertion Sort
print("Insertion Sort:")
print(insertion_sort(arr[:]))
print("*"*50)

# Quick Sort
print("Quick Sort:")
print(quick_sort(arr[:]))
print("*"*50)

# Quick Sort
print("Quick Sort Largo:")
print(quick_sort_largo(arr[:]))
print("*"*50)

#PARA LAS BUSQUEDAS CONSIDERAMOS EL ARREGLO YA ORDENADO.
arr.sort()  # Ordena el arreglo de forma ascendente

print("Búsqueda secuencial:")
print(f"busqueda_secuencial(arr, 90): {busqueda_secuencial(arr, 90)}")
print(f"busqueda_secuencial(arr, 91): {busqueda_secuencial(arr, 91)}")
print("*"*50)

print("Búsqueda binaria:")
print(f"busqueda_binaria(arr, 90): {busqueda_binaria(arr, 90)}")
print(f"busqueda_binaria(arr, 91): {busqueda_binaria(arr, 91)}")
print(f"busqueda_binaria(arr, 22): {busqueda_binaria(arr, 22)}")

print("*"*50)
