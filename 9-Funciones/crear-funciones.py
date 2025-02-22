# Creando una función simple
def saludar():
    print("Hola pelotudo")

# Ejecutando la función simple
saludar()

# Creando función con parámetros
def saludarNombre(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "reina"
        # print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")
    elif (sexo == "hombre"):
        adjetivo = "titan"
        # print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")
    else:
        adjetivo = "helicoptero apache"
        #print(f"Hola {nombre}, mi {adjetivo} ¿Como andas?")        
    print(f"Hola {nombre}, mi {adjetivo} Como andas?")    

saludarNombre("Ignacio", "hombre")    
saludarNombre("Maria", "MUJER")
saludarNombre("papu", "")

# Crear una función que nos retorne valores
def crear_contrasena_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contrasena = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    # return(contrasena)
    # Podríamos retornar una tupla por ejemplo
    return (contrasena,num)

# Desempaquetando la tupla
contrasena, valor_utilizado = crear_contrasena_random(98)
print(f"Tu contrasena nueva es {contrasena} y el valor utilizado fue {valor_utilizado}")