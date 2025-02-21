import json

class Ingestiones():
    def __init__(self):
        self.ruta_static="D:/2025/IUDIGITAL/1_TRIMESTRE/ANALITICA DE DATOS/Repositorios/luz_torres/src/pad_2025/static/"
      
##sjon 
    def leer_json(self):
        ruta_json = "{}json/datos_persona.json".format(self.ruta_static)
        with open(file=ruta_json,mode="r",encoding="utf-8") as f :
            datos = json.load(f)      
        return datos         
                      
inges = Ingestiones()
datos_json= inges.leer_json()          
print(datos_json)

#txt

def leer_txt(self):
    
        ruta_json = "{}txt/info.txt".format(self.ruta_static)
        datos=""
        with open(ruta_json,"r",encoding="utf-8") as f :
            datos = f.read()      
        return datos         
                      
inges = Ingestiones()
datos_txt = inges.leer_json()        
print(datos_txt)

#imprimir los dos

datos_txt = inges.leer_json()        
print(datos_txt)
print("**********")
datos_json= inges.leer_json()
print(datos_json)
