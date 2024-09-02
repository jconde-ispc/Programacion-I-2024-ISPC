import os
path = os.path.dirname(os.path.abspath(__file__)) + "/"

nombre_archivo = path+'Data/arboles.csv'
def test1():
    f = open(nombre_archivo, 'rt')  
    data = f.read()
    print(data)
    f.close()

def test2():
    with open(nombre_archivo, 'rt') as archivo:
        for i, linea in enumerate(archivo):
            print(i, linea)

l=[]
f = open(nombre_archivo, 'rt')
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    print(fila)
    registro = dict(zip(encabezados, fila))
    l.append(registro)

print("La lista es:",l)

print("-----------------------------------------------------")
f = open(nombre_archivo, 'rt', encoding='utf8') 
encabezados = next(f).split(',')
for line in f:
    fila = line.split(',')
    print("#####")
    for e,d in zip(encabezados,fila):
        el = e.strip("\n")
        dl = d.strip("\n")
        print(f'{el:>12s}: {dl}')
print("-----------------------------------------------------")


