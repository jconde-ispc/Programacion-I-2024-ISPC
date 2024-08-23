#https://github.com/python-unsam/programacion1/blob/main/Notas/05_Listas/04_Objetos.md#copias-profundas
#A veces vas a necesitar hacer una copia de un objeto así como de todos los objetos que contenga. 
# Llamamos a esto una copia pofunda (deep copy). 
# Podés usar la función deepcopy del módulo copy para esto

a = [2,3,[100,101],4]
import copy
b = copy.deepcopy(a)
a[2].append(102)
print(b[2]) #[100,101]
print(a[2] is b[2])# False