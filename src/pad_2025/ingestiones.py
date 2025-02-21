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

#leer varios

def leer_varios_txt(self,nombre=""):
    
        ruta_txt = "{}txt/{}".format(self.ruta_static,nombre)
        datos=""
        with open(ruta_txt,"w",encoding="utf-8") as f :
            datos = f.read()      
        return datos         
                      
nombre_archivo ="info copy.txt"
datos_txt = inges.leer_varios_txt(nombre_archivo)        
print(datos_txt)

#imprimir los tres

datos_txt = inges.leer_json()        
print(datos_txt)
print("**********")
datos_json= inges.leer_json()
print(datos_json)
print("**********")
nombre_archivo ="info copy.txt"
datos_txt = inges.leer_varios_txt(nombre_archivo)        
print(datos_txt)

#funciones para leer

def leer_cualquier_excel(self,nombre)
    pass
def leer_cualquier_csv(self,nombre)
    pass
def leer_bd(self,nombre_bd="",servidor="",puerto=0000):
    pass
def leer_api(self,url=""):
    pass
def leer_html(self,url=""):
    pass

#imprimir

def escribir_txt(self,nombre,datos):
    
        ruta_txt = "{}.txt".format(nombre)
        datos=""
        with open(ruta_txt,"w",encoding="utf-8") as f :
            #f.write(datos)  
            f.writable (datos)   
              
                      
inges.escribir_txt(nombre="archivo_txt",datos=datos_txt) 

