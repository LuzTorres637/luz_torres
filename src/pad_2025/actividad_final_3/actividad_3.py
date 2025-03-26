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
        #self.ruta_csv = "{}csv/".format(self.ruta_actividad_final_3)
        print(self.ruta_actual) 
        
        datos = {
            "n ejercicio": [1,2,3,4,5,6,7,8,9,10,11,12],
            "resultado": [0,0,0,0,0,0,0,0,0,0,0,0]
        }
        self.df = pd.DataFrame(data=datos,columns=["n ejercicio", "resultado"])


    def punto_1(self):
        self.df.loc[0,"resultado"] = f"{array_10x10}, {suma}"
        print("Completo el punto 1 : ok")

 
    def punto_2(self):
        self.df.loc[1,"resultado"] = f"{array_10x10}, {suma}"
        print("Completo el punto 2 : ok")

    def punto_3(self):
        self.df.loc[2,"resultado"] = f"{array_10x10}, {suma}"
        print("Completo el punto 3 : ok")

    def punto_4(self):
        self.df.loc[3,"resultado"] = f"{array_10x10}, {suma}"
        print("Completo el punto 4 : ok")

    def punto_5(self):
        self.df.loc[4,"resultado"] = f"{array_10x10}, {suma}"
        print("Completo el punto 5 : ok")

    def punto_6(self):
        self.df.loc[5,"resultado"] = f"{array_10x10}, {suma}"
        print("Completo el punto 6 : ok")

    #def ejecutar (self):
        #self.punto_1()
        #self.punto_2()
        #self.punto_3()
        #self.punto_4()
        #self.punto_5()
        #self.punto_6()
        #self.punto_7()
        #self.punto_8()
        #self.punto_9()
        #self.punto_10()
        #self.punto_11()
        #self.punto_12()
        #self.df.to_csv("{}Actividad_3.csv".format(self.ruta_csv), index=False)

#ene = Actividad_3()
#ene.ejecutar()