# Importando el módulo (Por eso es buena práctica separar con "_" los nombres de los archivos)
# Si el módulo estuviera en otra carpeta
# import funciones_buenas.modulo_saludar as m_saludar
import modulo_saludar as m_saludar
# Si queremos importar solo una función de un módulo
# from modulo_saludar import saludar, otra_funcion as nombre_funcion
# Podemos llamar el módulo de otra manera
# Ahora saludar es un método
print(m_saludar.saludar("Ignacio"))
print(type(m_saludar))

# Para importar todo de un módulo (esto puede ser una mala práctica)
# from modulo_saludar import *
print(dir(m_saludar)) # Todo lo que podemos hacer con el módulo (propiedades)
print(m_saludar.__name__) # Nombre del módulo que estamos llamando
print(__name__) # Nombre del módulo actual