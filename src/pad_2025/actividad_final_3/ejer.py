from pathlib import Path
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import io
# from kagglehub import KaggleHub


class Actividad_3:
    def __init__(self):
        self.ruta_actividad_final_3="src/pad_2025/actividad_final_3/"
        self.ruta_actual = str(Path.cwd())
        self.ruta_actividad_final_3="{}/src/pad_2025/actividad_final_3/".format(self.ruta_actual)
        directorio = os.path.dirname(self.ruta_actividad_final_3)
        if not os.path.exists(self.ruta_actual):
                os.makedirs(directorio, exists_ok=True) 
        self.ruta_csv = "{}csv/".format(self.ruta_actividad_final_3)
        self.ruta_dataset = "{}Dataset/{}".format(self.ruta_actividad_final_3,"winemag-data-130k-v2.csv")
        print(self.ruta_actual) 
        
        datos = {
            "# ejercicio": list(range(1, 13)),
            #"valor": [x*0 for x in range(1, 13)]
            "detalle":["Crea un DataFrame frutas que luzca así","Crea un DataFrame ventas_frutas que coincida con el diagrama","Crea una variable utensilios con una Serie que tenga el siguiente aspecto","Descarga el dataset 'wine review' desde Kaggle y cárgalo en un DataFrame llamado review, tal y como se muestra en la figura","Visualiza las primeras filas del DataFrame","Utiliza el método .info() para averiguar cuántas entradas hay. ¿Cuántas encontraste?","¿Cuál es el precio promedio?","Cuál es el precio más alto pagado","Crea un DataFrame con todos los vinos de california Salida","Utiliza idxmax() para encontrar el índice del vino con el precio más alto y luego utiliza loc para obtener toda la información de ese vino específico","¿Cuáles son los tipos de uva más comunes en California?","¿Cuáles son los 10 tipos de uva más comunes en California?"],
            "resultado":[0,0,0,0,0,0,0,0,0,0,0,0],
        }
        self.df = pd.DataFrame(data=datos,columns=["# ejercicio", "detalle", "valor"])

#"n_punto": [1,2,3,4,5,6,7,8,9,10,11,12],
            
    def punto_1(self):
        frutas = pd.DataFrame ({
            "Granadilla": [20],
            "Tomates": [50]
            })
        self.df["valor"] =self.df["valor"].astype(object)
        self.df.to_csv("self.ruta_csv")
        self.df.loc[0,"valor"] = f"{frutas}"
        print("Completo el punto 1 : ok")