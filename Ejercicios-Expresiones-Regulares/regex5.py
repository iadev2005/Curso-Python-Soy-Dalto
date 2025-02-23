import re
text = "Este es un ejemplo de una pagina web: https://example.com y también podemos visitarla como https://example.org"
patron = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
resultado = re.findall(patron,text)
print(resultado)