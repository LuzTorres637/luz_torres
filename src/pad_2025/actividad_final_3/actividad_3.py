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
             ["3 unidades","2 unidades","4 unidades","5 unidades"], 
             index= ["Cuchara","Tenedor","Cuchillo","Plato"],
             name ="Cocina"
             )
        self.df.loc[2,"valor"] = f"{utensilios}"
        print("Completo el punto 3 : ok")

#Descarga del dataset del Punto_4
    def download_dataset_zip(self):
        print("Descargando dataset desde Kaggle...")
        df = pd.read_csv(self.ruta_dataset)
        return df

    def punto_4(self):
        df = self.download_dataset_zip()
        primeras_filas = df.head()
        ultimas_filas = df.tail()
        resultado = f"Primeras filas:\n{primeras_filas}\n\nÚltimas filas:\n{ultimas_filas}"
        self.df.loc[3,"valor"] = f"{resultado}"
        try:
            df = pd.read_csv(self.ruta_dataset)
        except FileNotFoundError:
            print(f"Error: El archivo CSV no se encontró en la ruta: {self.ruta_dataset}")
        return None            
    print("Completo el punto 4 : ok")   

    def punto_5(self):
        df = self.download_dataset_zip()
        primeras_filas = df.head()
        resultado = f"{primeras_filas}" 
        self.df.loc[4,"valor"] = f"{resultado}"
        print("Completo el punto 5 : ok")
        
    def punto_6(self): 
        df = self.download_dataset_zip()
        buffer = io.StringIO()
        df.info(buf=buffer)
        entrada = buffer.getvalue()
        num_entries_line = [line for line in entrada.splitlines() if "RangeIndex" in line][0]
        num_entries = int(num_entries_line.split(":")[1].strip().split(" ")[0])
        resultado = f"{entrada}\nNúmero de entradas encontradas: {num_entries}"
        self.df.loc[5,"valor"] = f"{resultado}"
        print("Completo el punto 6 : ok")
        return num_entries
      
    def punto_7(self): 
        df = self.download_dataset_zip()
        precio_promedio = df["price"].mean()
        resultado = f"{precio_promedio}" 
        self.df.loc[6,"valor"] = f"{resultado}"
        print("Completo el punto 7 : ok")

    def punto_8(self): 
        df = self.download_dataset_zip()
        precio_maximo = df["price"].max()
        resultado = f"{precio_maximo}" 
        self.df.loc[7,"valor"] = f"{resultado}"
        print("Completo el punto 8 : ok")

    def punto_9(self):
        df = self.download_dataset_zip() 
        vinos_california = df[df["province"] == "California"].copy()
        resultado = f"{vinos_california}" 
        self.df.loc[8,"valor"] = f"{resultado}"
        print("Completo el punto 9 : ok")

    def punto_10(self): 
        df = self.download_dataset_zip()
        vinos_california = df[df["province"] == "California"]
        indice_max_precio_california = vinos_california["price"].idxmax()
        vino_mas_caro_california = vinos_california.loc[indice_max_precio_california]
        resultado = f"{indice_max_precio_california}\n{vino_mas_caro_california}" 
        self.df.loc[9,"valor"] = f"{resultado}"
        print("Completo el punto 10 : ok")

    def punto_11(self): 
        df = self.download_dataset_zip()
        vinos_california = df[df["province"] == "California"].copy()
        conteo_variedades = vinos_california["variety"].value_counts() 
        self.df.loc[10,"valor"] = f"{conteo_variedades}"
        print("Completo el punto 11 : ok")

    def punto_12(self): 
        df = self.download_dataset_zip()   
        vinos_california = df[df["province"] == "California"].copy()
        conteo_variedades = vinos_california["variety"].value_counts() 
        top_10_variedades = conteo_variedades.head(10)
        self.df.loc[11,"valor"] = f"{top_10_variedades}"
        print("Completo el punto 12 : ok")


    def ejecutar (self):
            #self.punto_1()
            #self.punto_2()
            #self.punto_3()
            self.punto_4()
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