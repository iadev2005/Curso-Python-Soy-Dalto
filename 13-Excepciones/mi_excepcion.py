class MiExepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante cometiste el siguiente error {err}")

# Lanzando mi propia excepcion
raise MiExepcion("Jsjsjsjsjs, persona poco culta")

try:
    raise MiExepcion("Jsjsjsjsjs, persona poco culta")
except:
    print("Como vas a cometer ese error")