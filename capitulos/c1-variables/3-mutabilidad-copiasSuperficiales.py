#https://github.com/python-unsam/programacion1/blob/main/Notas/05_Listas/04_Objetos.md#identidad-y-referencias


#COPIAS SUPERFICIALES
a = [2,3,[100,101],4]
b = list(a) # Hacer una copia
print(a is b) # False

a.append(5)
print(a) #[2, 3, [100, 101], 4, 5]
print(b) #[2, 3, [100, 101], 4]

b[2].append(102)
print(a[2]) #[100,101,102]
print(a[2] is b[2])#True
