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
        print(f"{student=} y {mark=}")
        if mark > max_mark:
            max_mark = mark
            best_student = student
    return best_student

print(best_student(ana=8, antonio=6, inma=9, javier=7)) #marks={ ana : 8, antonio : 6, inma : 9, javier : 7} output: inma

print("------------------------------------------------")
marks = dict(ana=8, antonio=6, inma=9, javier=7)
#best_student(marks)#TypeError: best_student() takes 0 positional arguments but 1 was given
print(f"{best_student(**marks)=}")


if __name__ == "__main__":
    # Pruebas para la función _sum con argumentos posicionales
    print("Resultado de _sum(4, 3, 2, 1):", _sum(4, 3, 2, 1))  # values=(4, 3, 2, 1) y output=10
    print("-----------------------------------------------------------")
    
    # Pruebas para la función _sum con desempaquetado de tupla
    values = (4, 3, 2, 1)
    print("Resultado de _sum(*values):", _sum(*values))  # values=(4, 3, 2, 1) y output=10
    
    # Otras pruebas para _sum
    print("Resultado de _sum(1, 2, 3):", _sum(1, 2, 3))  # output=6
    print("Resultado de _sum(10, 20):", _sum(10, 20))  # output=30
    print("Resultado de _sum(5):", _sum(5))  # output=5
    print("Resultado de _sum():", _sum())  # output=0

    # Pruebas para la función best_student
    print("Mejor estudiante:", best_student(ana=8, antonio=6, inma=9, javier=7))  # output: inma
    print("------------------------------------------------")
    
    # Pruebas para best_student con un diccionario
    marks = dict(ana=8, antonio=6, inma=9, javier=7)
    print("Mejor estudiante con dict:", best_student(**marks))  # output: inma
    
    # Otras pruebas para best_student
    print("Mejor estudiante:", best_student(maria=10, juan=8, pedro=9))  # output: maria
    print("Mejor estudiante:", best_student(luis=7, sofia=8, carlos=6))  # output: sofia
    print("Mejor estudiante:", best_student(jorge=5, clara=5))  # output: jorge
    print("Mejor estudiante:", best_student())  # output: None (sin estudiantes)