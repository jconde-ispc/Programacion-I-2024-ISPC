def funcionRecursiva():
    try:#aca las instrucciones
        result = int(input("Ingresar valor entero positivo: "))
        assert result >= 0, 'Ingreso un valor negativo'
        print("luego de assert dentro del try")
        a = 3/result
    except AssertionError as error:
        #aca veo que hago con el error
        print("entro por assertionError")
        print(error)
        funcionRecursiva()    
    except Exception as e:
        #aca veo que hago con el error
        print('entro por exception')
        print(e)
        funcionRecursiva()
    else:#si no hubo error
        print("No hay error")
    finally:#siempre se ejecuta (habiendo errores o no)
        print("finalyyyyyyyyyyy")

funcionRecursiva()