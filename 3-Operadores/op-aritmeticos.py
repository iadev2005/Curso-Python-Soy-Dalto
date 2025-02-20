# Suma y Resta (+ y -)
suma= 12 + 5
resta= 12 - 5

# Multiplicación y División (* y /)
multi= 12 * 5
div= 12 / 5

# Potenciación (Exponente) (**)
exponente= 12 ** 5

# División baja (//)
div_baja= 12 // 5

# Resto o Módulo
resto= 12 % 5

# Para obtener el tipo de dato
tipo_de_dato= type(["Hola maestro", 55, 23]) # Lista
tipo_de_dato= type(("Hola maestro", 55, 23)) # Tupla
tipo_de_dato(div_baja) # Devuelve entero redondeado hacia abajo
# print(tipo_de_dato)

resultado= f"""Suma:{suma}
Resta:{resta}
Multiplicacion:{multi}
Division:{div}
Potenciacion:{exponente}
Division (baja):{div_baja}
Resto:{resto}"""

print(resultado)