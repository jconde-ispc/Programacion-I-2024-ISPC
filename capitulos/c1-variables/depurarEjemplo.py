n = 10
contador = 0
suma = 0
multiplo = 1
pares=0
impares=0

def esPar(n):
  return n % 2 == 0

while contador < n:
  contador += 1
  suma = suma + contador
  multiplo = multiplo * contador
  print(contador)
  if(esPar(contador)):
    print("es par")
    pares += 1
  else:
    print("es impar")
    impares += 1
