# f-strings, son maneras de incrustar expresiones dentro de cadenas de texto
# nombreCompleto= "Ignacio Aliendres" (Convención camelCase)
nombre_completo= "Ignacio Aliendres" # snake_case
# Concatenar con f-strings
bienvenida= f"Hola {nombre_completo} Como estas?"

# Operadores de pertenencia (in / not in)
print("cio" in bienvenida) # True
print("Ign" not in bienvenida) # False

# Concatenar con +
bienvenida= "Hola " + "Como estas?"
print(bienvenida)

# Entonces las variables son espacios donde almacenamos datos, en este caso estos son Datos Simples