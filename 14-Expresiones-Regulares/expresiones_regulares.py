import re 

texto = '''Hola maestro como estas mi capitan, esta es la cadena 1. p 
Esta es la linea ababababbb225 linea de texto
Y esta es la final (linea 3) definitica mi capitan'''

# resultado = re.search("Hola",texto,flags=re.IGNORECASE)
# resultado = re.search("Hola",texto)

# \d busca dígitos numéricos del 0 al 9
resultado = re.findall(r"\d",texto)

# \D busca todo MENOS dígitos numéricos del 0 al 9
resultado = re.findall(r"\D",texto)

# \w busca carácteres alfanuméricos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w",texto)

# \W busca todo MENOS carácteres alfanuméricos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W",texto)

#\s busca espacios en blanco
resultado = re.findall(r"\s",texto)

#\S busca todo MENOS espacios en blanco
resultado = re.findall(r"\S",texto)

# . busca todo MENOS saltos de línea
resultado = re.findall(r'.',texto)

# \n busca saltos de línea
resultado = re.findall(r'\n',texto)

# /. cancela caracteres especiales, cancelando la función del punto y buscando puntos

resultado = re.findall(r'\.',texto)

# Armando una cadena que busque un numero, seguido de un texto, seguido de un espacio y un espacio en línea
resultado = re.findall(r'\d\.\s',texto)

# Buscando el principio de una línea
# ^ busca el comienzo de una línea
# flags=re.M activa la multilínea
resultado = re.findall(f'^Hola',texto)
resultado = re.findall(f'^Esta',texto, flags=re.M)

# $ busca el final de una línea
resultado = re.findall(f'capitan$',texto, flags=re.M)

# {n} busca n cantidad de veces el valor de la izquierda
resultado = re.findall(r'\d{3}\s',texto)

# {n.m} al menos n, como maximo m
resultado = re.findall(r'\d{1,4}',texto)

# Tambien tenemos conjuntos
resultado = re.findall(r'ab{2,4}',texto)

# Repitiendo el patrón ababab
resultado = re.findall(r'(ab){2,4}',texto)

# Con los corchetes funcionan las combinacioes aa ab ba bb
resultado = re.findall(r'[ab]{2,4}',texto)

# | busca una cosa o la otra
resultado = re.findall(r'\d{2,4}|Hola',texto)

print(resultado)