import pandas as pd
import os
import zipfile
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from pathlib import Path 


class Actividad_2:
    def __init__(self):
        self.ruta_Actividad_2="src/pad_2025/Actividad_2/"
        self.ruta_actual = str(Path.cwd())
        self.ruta_Actividad_2="{}/src/pad_2025/Actividad_2/".format(self.ruta_actual)
        directorio = os.path.dirname(self.ruta_Actividad_2)
        if not os.path.exists(self.ruta_actual):
                os.makedirs(directorio, exists_ok=True)

        datos= [(1,0), (0,1)]
        self.df= pd.DataFrame( data=datos, columns=["# ejercicio", "valor"])  

    def punto_4(self):
        array_1 = np.random.rand(100)
        array_2 = np.random.rand(100)
        #self.df["# ejercicio"] = 4
        #self.df["valor"] = [[array_1], [array_2]]
        #self.df.to_csv("Actividad_2.csv", index=False)
        plt.figure(figsize=(8, 6))  
        plt.scatter(array_1, array_2)
        plt.xlabel("Eje X")
        plt.ylabel("Eje Y")
        plt.title("Gráfico de dispersión de números aleatorios")
        plt.savefig(self.ruta_Actividad_2 + "punto_4.png")
        plt.show()
          
ingestion = Actividad_2()
ingestion.punto_4()
print("plt.show:")






        


   
