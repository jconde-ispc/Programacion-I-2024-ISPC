import os
path = os.path.dirname(os.path.abspath(__file__)) + "/"

nombre_archivo = "demo.txt"
modo_apertura = "a" # "w" (sobreescribe) o "a" (añade)

with open(path+nombre_archivo, modo_apertura) as f:
    f.write("Ahora el archivo tiene mas contenido!. Desde with")

#No hay que cerrarlo, lo hace python luego de ejecutar las instrucciones dentro del with
