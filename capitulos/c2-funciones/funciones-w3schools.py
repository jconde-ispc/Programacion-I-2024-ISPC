def my_function():
  print("Hello from a function")

my_function()

print("1111111111111111111111111111111111111")

def my_function2(fname):
  print(fname + " Refsnes")

my_function2("Emil")
my_function2("Tobias")
my_function2("Linus")

print("2222222222222222222222222222222222222")

def my_function3(fname, lname):
  print(fname + " " + lname)

my_function3("Emil", "Refsnes")
my_function3("Emil")# This function expects 2 arguments, but gets only 1:

print("3333333333333333333333333333333333333")

def my_function4(*kids):
  print("The youngest child is " + kids[2])

my_function4("Emil", "Tobias", "Linus")

print("4444444444444444444444444444444444444")

def my_function5(child3, child2, child1):
  print("The youngest child is " + child3)

my_function5(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

print("5555555555555555555555555555555555555")

def my_function6(**kid):
  print("His last name is " + kid["lname"])

my_function6(fname = "Tobias", lname = "Refsnes")

print("6666666666666666666666666666666666666")

def my_function7(country = "Norway"):
  print("I am from " + country)

my_function7("Sweden")
my_function7("India")
my_function7()
my_function7("Brazil")

print("7777777777777777777777777777777777777")

def my_function8(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function8(fruits)

print("8888888888888888888888888888888888888")

def my_function9(x):
  return 5 * x

print(my_function9(3))
print(my_function9(5))
print(my_function9(9))

print("9999999999999999999999999999999999999")

def myfunction10():
  pass

print("0000000000000000000000000000000000000")

def my_function11(x, /):
  print(x)

my_function11(3)

print("1111111111111111111111111111111111111")

