#Empaquetar/Desempaquetar argumentos posicionales
def _sum(*values):
    print(f"{values=}")
    result = 0
    for value in values:
        result += value
    return result

print(_sum(4, 3, 2, 1)) #values=(4, 3, 2, 1) y output=10

print("-----------------------------------------------------------")

#Empaquetar/Desempaquetar argumentos nombrados
values = (4, 3, 2, 1)
print(_sum(*values)) #values=(4, 3, 2, 1) y output=10

def best_student(**marks):
    print(f"{marks=}")
    max_mark = -1
    for student, mark in marks.items():
        if mark > max_mark:
            max_mark = mark
    best_student = student
    return best_student

print(best_student(ana=8, antonio=6, inma=9, javier=7)) #marks={ ana : 8, antonio : 6, inma : 9, javier : 7} output: inma

