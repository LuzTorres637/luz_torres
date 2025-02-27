import json
import requests

class Entrega_actividad_1():
        def __init__(self):
            self.ruta_static="src/pad_2025/static/"

#leer api
        def leer_api(self,url):
            response = requests.get(url)
            return response.json()
            
#escribir un api
        def escribir_json(self,nombre_archivo="",datos=None):
            if nombre_archivo =="":
                    nombre_archivo="Entrega_actividad_1.json"
            if datos is None:
                  datos = "no hay datos"
            ruta_json = "{}/json/{}".format(self.ruta_static,nombre_archivo)
            with open(self.ruta_static+nombre_archivo, "w", encoding="utf-8") as f:
                  json.dump(datos,f,ensure_ascii=False, indent=4)
            return True
             

#1_instancia verificacion de ruta
ingestion = Entrega_actividad_1()
print("self.ruta_static")

#2_instancia leer api
ingestion = Entrega_actividad_1()
datos_json = ingestion.leer_api("https://chroniclingamerica.loc.gov//lccn/sn86069873/1900-01-05/ed-1/seq-3.json")
print("esta es la ruta statica :"",ingestion.ruta_static")
print("datos_json:",datos_json)

#3_instancia escribir api
ingestion = Entrega_actividad_1()
datos_json = ingestion.leer_api("https://chroniclingamerica.loc.gov//lccn/sn86069873/1900-01-05/ed-1/seq-3.json")
if ingestion.escribir_json(nombre_archivo="Entrega_actividad_1.json",datos=datos_json):
    print("datos_json:",datos_json)