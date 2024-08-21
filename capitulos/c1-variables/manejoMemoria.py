a = 10
b = a
c = 8 + 2
d = 8

print(f" {id(a)=} y el {a=}")
print(f" {id(b)=} y el {b=}")
print(f" {id(c)=} y el {c=}")
print(f" {id(d)=} y el {d=}")

b = 8
c = c + 1
d = a + 1
e = 11

print("segunda parte --------------")

print(f" {id(a)=} y el {a=}")
print(f" {id(b)=} y el {b=}")
print(f" {id(c)=} y el {c=}")
print(f" {id(d)=} y el {d=}")
print(f" {id(e)=} y el {e=}")

""" 

"""


