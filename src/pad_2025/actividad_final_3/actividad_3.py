from pathlib import Path
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
 


class Actividad_3:
    def __init__(self):
        self.ruta_actividad_final_3="src/pad_2025/actividad_final_3/"
        self.ruta_actual = str(Path.cwd())
        self.ruta_actividad_final_3="{}/src/pad_2025/actividad_final_3/".format(self.ruta_actual)
        directorio = os.path.dirname(self.ruta_actividad_final_3)
        if not os.path.exists(self.ruta_actual):
                os.makedirs(directorio, exists_ok=True) 
        #self.ruta_img = "{}img/".format(self.ruta_actividad_final_3)
        self.ruta_csv = "{}csv/".format(self.ruta_actividad_final_3)
        print(self.ruta_actual) 
        
        datos = {
            "# ejercicio": list(range(1, 12)),
            "valor": [x*0 for x in range(1, 12)]
        }
        self.df = pd.DataFrame(data=datos,columns=["# ejercicio", "valor"])


    def punto_1(self):
        frutas = pd.DataFrame ({
            "Granadilla": [20],
            "Tomates": [50]
            })
        self.df["valor"] =self.df["valor"].astype(object)
        self.df.loc[0,"valor"] = f"{frutas}"
        print("Completo el punto 1 : ok")
 
    def punto_2(self):
        ventas_frutas = pd.DataFrame ({
            "Granadilla": [20, 49],
            "Tomates": [50, 100], 
            }) 
        ventas_frutas.index= ["ventas2021", "ventas2022"]
        self.df["valor"] =self.df["valor"].astype(object)
        self.df.loc[1,"valor"] = f"{ventas_frutas}"
        print("Completo el punto 2 : ok")

    def punto_3(self):
        utensilios = pd.Series(
             [3,2,4,5], 
             index= ["Cuchara","Tenedor","Cuchillo","Plato"], 
             name="Cocina" 
             )
        pd.DataFrame ({"Unidades"})
        self.df["valor"] =self.df["valor"].astype(object)
        self.df.loc[2,"valor"] = f"{utensilios}"
        print("Completo el punto 3 : ok")

   

    #def punto_4(self):
       # self.df.loc[3,"resultado"] = f"{array_10x10}, {suma}"
        #print("Completo el punto 4 : ok")

    #def punto_5(self):
        #self.df.loc[4,"resultado"] = f"{array_10x10}, {suma}"
        #print("Completo el punto 5 : ok")

    #def punto_6(self):
        #self.df.loc[5,"resultado"] = f"{array_10x10}, {suma}"
        #print("Completo el punto 6 : ok")

    def ejecutar (self):
        #self.punto_1()
        #self.punto_2()
        self.punto_3()
        #self.punto_4()
        #self.punto_5()
        #self.punto_6()
        #self.punto_7()
        #self.punto_8()
        #self.punto_9()
        #self.punto_10()
        #self.punto_11()
        #self.punto_12()
        self.df.to_csv("{}Actividad_3.csv".format(self.ruta_csv), index=False)

ene = Actividad_3()
ene.ejecutar()