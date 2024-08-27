#Calling a Function
def my_function():
  print("Hello from a function")

my_function()

print("1111111111111111111111111111111111111")
#Arguments
def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

print("2222222222222222222222222222222222222")
#Number of Arguments
def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Emil", "Refsnes")
my_function3("Emil")# This function expects 2 arguments, but gets only 1:

print("3333333333333333333333333333333333333")
#Arbitrary Arguments, *args 
#(Si no sabe cuántos argumentos se pasarán a su función, agregue un *antes del nombre 
# del parámetro en la definición de la función.)
def my_function4(*kids):
  print("The youngest child is " + kids[2])

my_function4("Emil", "Tobias", "Linus")

print("4444444444444444444444444444444444444")
#Keyword Arguments (You can also send arguments with the key = value syntax.)
def my_function5(child3, child2, child1):
  print("The youngest child is " + child3)

my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("5555555555555555555555555555555555555")
#Arbitrary Keyword Arguments, **kwargs
#Si no sabe cuántos argumentos de palabras clave se pasarán a su función, agregue 
# dos asteriscos: **antes del nombre del parámetro en la definición de la función.
def my_function6(**kid):
  print("His last name is " + kid["lname"])

my_function6(fname = "Tobias", lname = "Refsnes")

print("6666666666666666666666666666666666666")
#Default Parameter Value
def my_function7(country = "Norway"):
  print("I am from " + country)

my_function7("Sweden")
my_function7("India")
my_function7()
my_function7("Brazil")

print("7777777777777777777777777777777777777")
#Passing a List as an Argument
def my_function8(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function8(fruits)

print("8888888888888888888888888888888888888")
#Return Values
def my_function9(x):
  return 5 * x

print(my_function9(3))
print(my_function9(5))
print(my_function9(9))

print("9999999999999999999999999999999999999")
#The pass Statement
def myfunction10():
  pass

print("0000000000000000000000000000000000000")
#Positional-Only Arguments
#Puede especificar que una función puede tener SÓLO argumentos posicionales
def my_function11(x, /):
  print(x)

my_function11(3)

print("1111111111111111111111111111111111111")
#Keyword-Only Arguments
def my_function12(*, x):
  print(x)

my_function12(x = 3)

print("222222222222222222222222222222222222")
#Combine Positional-Only and Keyword-Only
#Cualquier argumento antes de / ,solo deben ser posicionales, y
# cualquier argumento después de *, solo deben ser palabras clave.
def my_function13(a, b, /, *, c, d):
  print(a + b + c + d)

my_function13(5, 6, c = 7, d = 8)

print("333333333333333333333333333333333333333333333")
""" 
Recursión
Python también acepta la recursión de funciones, lo que significa que una función definida puede llamarse a sí misma.

La recursión es un concepto matemático y de programación común. Significa que una función se llama a sí misma. Esto tiene la ventaja de que permite recorrer los datos en bucle para llegar a un resultado.

El desarrollador debe tener mucho cuidado con la recursión, ya que puede resultar muy fácil escribir una función que nunca finalice o que utilice cantidades excesivas de memoria o potencia del procesador. Sin embargo, cuando se escribe correctamente, la recursión puede ser un método de programación muy eficiente y matemáticamente elegante.

En este ejemplo, tri_recursion() es una función que hemos definido para que se llame a sí misma ("recurse"). Usamos la variable k como dato, que decrementa ( -1 ) cada vez que realizamos una recursión. La recursión finaliza cuando la condición no es mayor que 0 (es decir, cuando es 0).

Para un desarrollador nuevo puede llevar algún tiempo comprender exactamente cómo funciona esto; la mejor forma de descubrirlo es probándolo y modificándolo.
"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)