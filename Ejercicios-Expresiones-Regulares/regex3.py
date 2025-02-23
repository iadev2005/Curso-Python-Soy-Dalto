import re
text = "reeemplazando todas las vocales por el asterisco"
nuevo_texto = re.sub("[aeiou]","*",text)
print(nuevo_texto)