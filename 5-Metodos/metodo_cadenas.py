cadena1 = "Hola soy Ignacio"
cadena2 = "77"
cadena3 = "Ignacio"

# dir devuelve la lista de atributos válidos del objeto pasado
print(dir(cadena1))

resultado = dir(cadena1)
print(resultado)

# upper() convierte todas las letras de la cadena a mayúsculas
resultado= cadena1.upper() # Así se ejecutan metódos de un objeto en Python
# dato.metodo()
print(resultado)

# lower() convierte todas las letras de la cadena a minúsculas
resultado = cadena1.lower()
print(resultado)

# capitalize() convierte la primera letra de la cadena a mayúscula
resultado = cadena1.capitalize()
print(resultado)

# find() busca la subcadena en la cadena y devuelve la posición en la que se encuentra
busqueda_find= cadena1.find("Ignacio")
print(busqueda_find) # Devuelve -1 si no encuentra un valor

# index() busca la subcadena en la cadena y devuelve la posición en la que se encuentra
busqueda_index = cadena1.index("Ignacio")
print(busqueda_index) # Devuelve una excepción si no encuentra un valor

# isnumeric() devuelve True si todos los caracteres de la cadena son números
es_numerico = cadena2.isnumeric()
print(es_numerico)

# Si es alfanumérico devuelve True (Solamente son validos los caracter de la A-Z)
es_alfanumerico = cadena3.isalpha()
print(es_alfanumerico)

# count() cuenta cuantas veces se repite una subcadena en la cadena
contar_coincidencias= cadena1.count("o")
print(contar_coincidencias) # SI no se encuentra pone 0

# len() devuelve la longitud de la cadena
longitud = len(cadena1)
print(longitud)

# startswith() devuelve True si la cadena empieza con la subcadena indicada
empieza_con = cadena1.startswith("Hola")
print(empieza_con)

# endswith() devuelve True si la cadena termina con la subcadena indicada
termina_con = cadena1.endswith("Ignacio")
print(termina_con)

# replace() reemplaza una subcadena por otra
reemplazar = cadena1.replace("Ignacio", "David")
print(reemplazar)

# Un ejemplo practico
cadena_ejm = "Hola,soy,Ignacio"
reemplazar = cadena_ejm.replace(",", " ")
print(reemplazar)

# split() divide la cadena en subcadenas a partir de un delimitador
# separa cadenas con el delimitador que le pasemos
# si no le pasamos nada, separa por espacios 
reemplazar = cadena_ejm.split(",")
print(reemplazar) # Crea una lista con las subcadenas

# Podriamos consultar esto por ejemplo
print(reemplazar[0])