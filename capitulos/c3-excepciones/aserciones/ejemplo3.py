def funRecu():
    try:#aca pongo mi bloque de codigo

        result = int(input("Ingrese un numero positivo"))
        assert result > 0, 'El resultado debe ser positivo'
        print("1111111111111")
    except Exception as error:# que hacer si hay errores
        print(error)
        funRecu()
    else:# que hago si no hubo errores
        print("el numero es ", result)
        a= 3

    finally:# aca van las instrucciones sea cualquier caso, si hay errores o no
        print("esta en el finaly")

funRecu()









""" 
Traceback (most recent call last):
  File "/home/usuario/desarrollo/proyectosISPC/Programacion-I-2024-ISPC/capitulos/c3-excepciones/aserciones/ejemplo3.py", line 3, in <module>
    assert result > 0, 'El resultado debe ser positivo'
AssertionError: El resultado debe ser positivo
"""