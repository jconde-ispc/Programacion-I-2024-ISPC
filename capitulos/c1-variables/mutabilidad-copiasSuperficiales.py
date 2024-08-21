#https://github.com/python-unsam/programacion1/blob/main/Notas/05_Listas/04_Objetos.md#identidad-y-referencias

#IDENTIDAD Y REFERENCIAS

a = [1,2,3]
b = a
print(a is b)  #True

id(a) #3588944
id(b) #3588944

#COPIAS SUPERFICIALES
a = [2,3,[100,101],4]
b = list(a) # Hacer una copia
print(a is b) # False

a.append(5)
print(a) #[2, 3, [100, 101], 4, 5]
print(b) #[2, 3, [100, 101], 4]

a[2].append(102)
print(b[2]) #[100,101,102]
print(a[2] is b[2])#True
