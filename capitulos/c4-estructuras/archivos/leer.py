import os
path = os.path.dirname(os.path.abspath(__file__)) + "/"
f = open(path+"demo.txt", "r")
print(f.read())
f.close()
print("----------------------------------------------------------------")
f = open(path+"demo.txt", "r")
print(f.read(5))
f.close()
print("----------------------------------------------------------------")
f = open(path+"demo.txt", "r")
for x in f:
  print(x)
f.close()

