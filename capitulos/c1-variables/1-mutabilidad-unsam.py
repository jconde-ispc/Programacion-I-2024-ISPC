#https://github.com/python-unsam/programacion1/blob/main/Notas/05_Listas/04_Objetos.md#identidad-y-referencias
a = [1,2,3]
b = a
c = [a,b]

a.append(999)
print(a) #[1,2,3,999]
print(b) #[1,2,3,999]
print(c) #[[1,2,3,999], [1,2,3,999]]

print(f"{id(a)=}") #id(a)=140004109508224
print(f"{id(b)=}") #id(b)=140004109508224
print(f"{id(c)=}") #id(c)=140004110238912


