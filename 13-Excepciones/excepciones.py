def sumar_dos():
    
    while True:
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        try:
            resultado = int(a) + int(b)
        except ValueError as e:
            # print("Te pedi un numero gil, no te hagas el piola")
            # print(f"Error: {e}")
            # Para saber el nombre de la excepcion
            print(f"Error: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        else:
            break # Salimos del bucle while y retornamos el resultado
        finally:
            print("Manejo de Excepcion Finalizado")
    
    return resultado

print(sumar_dos())