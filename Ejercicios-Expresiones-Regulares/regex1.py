import re
text = "The quick brown fox jumps over the lazy dog"
# Busca que empieze con The, cualquier cosa que no sea un alto en linea (puede encontrar 0 o más)
# luego carácteres que no sean espacios en línea, tiene que haber un dog y debe estar al final
x = re.search("^The.*dog$",text)
if x:
    print("SI")
else:
    print("NO")