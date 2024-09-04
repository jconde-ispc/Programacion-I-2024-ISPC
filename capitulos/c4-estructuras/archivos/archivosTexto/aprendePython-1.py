import os
path = os.path.dirname(os.path.abspath(__file__)) + "/"

f = open(path+'files/temps.dat')

for line in f:    # that easy!
    print(line)

f.close()
print("----------------00000--------------------------------")

# Lectura de las 3 primeras líneas
f = open(path+'files/temps.dat')
for _ in range(3):
    print(f.readline().strip())

print("----------------11111--------------------------------")
# Lectura de las restantes líneas (4)
for line in f:
    print(line.strip())

f.close()
print("--------------22222----------------------------------")
f = open(path+'files/temps.dat')
for line in f:
    print(line.strip(), end=' ')

f.seek(0)  # desplazamiento al principio

print("----------------333333--------------------------------")
for line in f:
    print(line.strip(), end=' ')

f.close()

print("------------4444--------------------")
f = open(path+'files/temps.dat')

for line_no, line in enumerate(f, start=1):
    print(f'L{line_no}: {line.strip()}')
f.close()

print("------------5555--------------------")

with open(path+'files/temps.dat') as f:
    for line in f:
        min_temp, max_temp = line.strip().split()
        print(min_temp, max_temp)