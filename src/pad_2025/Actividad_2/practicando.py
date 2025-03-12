import pandas as pd
import os
import zipfile
import matplotlib as plt
import numpy as np
import openpyxl
from pathlib import Path 


class Actividad_2:
    def __init__(self):
        datos= [(1,0),]
        self.df= pd.DataFrame( data=datos, columns=["# ejercicio", "valor"])  

    def punto_4(self):
        matriz = np.zeros((4, 4), dtype=int)
        for i in range(4):
            for j in range(4):
                matriz[i, j] = i + j
            self.df["# ejercicio"] = 4
            self.df["valor"] = [matriz]
            self.df.to_csv("Actividad_2.csv", index=False)
        try:
            matriz_inversa = np.linalg.inv(matriz)
            self.df["# ejercicio"] = 4
            self.df["valor"] = [matriz, matriz_inversa ]
            self.df.to_csv("Actividad_2.csv", index=False)
        except np.linalg.LinAlgError:
            print("La matriz no tiene inversa (es singular).")

ingestion = Actividad_2()
ingestion.punto_4()
print("matriz, matriz_inversa, La matriz no tiene inversa (es singular):")






        


   
