# Si el modulo esta dentro de una carpeta en la misma ruta
import funciones_buenas.saludar as m_saludar
import sys
# Si el modulo no esta en la misma carpeta
# print (saludar.saludar("Ignacio"))
sys.path.append("C:/Users/ignac/Documents/Python/10-Modulos/funciones_buenas")
print(m_saludar.saludar("Ignacio"))
print(sys.builtin_module_names) # Para no crear un módulo existente
print(sys.path) # Rutas donde python busca los módulos
print(sys.modules) # Módulos que se han importado
