import os

path = os.path.dirname(os.path.abspath(__file__)) + "/"

pathArchivo = path+"demo2.txt"

if os.path.exists(pathArchivo):
  os.remove(pathArchivo)
  print(f"Se elimino correctamente el archivo {pathArchivo}")
else:
  print(f"The file {pathArchivo} does not exist")


