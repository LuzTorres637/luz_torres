import pandas as pd
import os
import zipfile
import matplotlib as plt
import numpy as np
import openpyxl
from pathlib import Path 


class Actividad_2:
    def __init__(self):
        #self.ruta_Actividad_2="src/pad_2025/Actividad_2/"
        #self.ruta_actual = str(Path.cwd())
        #self.ruta_Actividad_2="{}/src/pad_2025/Actividad_2/".format(self.ruta_actual)
        #directorio = os.path.dirname(self.ruta_Actividad_2)
        #if not os.path.exists(self.ruta_xlsx):
                #os.makedirs(directorio, exists_ok=True)
        datos= [(1,0),(2,0)]
        self.df= pd.DataFrame( data=datos, columns=["# ejercicio", "valor"])  

#Introducción y cálculos con los arrays de NumPy
#Punto_1_Genera un array de NumPy con valores desde 10 hasta 29.
    #def punto_1(self):
        #array_10_29 = np.arange(10, 30)
        #self.df.iloc[1,1]= str(array_10_29)
        #self.df["# ejercicio"] = 1
        #self.df["valor"]= [array_10_29] * len(self.df)
        #self.df.to_csv("Actividad_2.csv", index= "false")
#ingestion = Actividad_2()
#ingestion.punto_1()
#print("array_10_29:")

#Punto_2_Calcula la suma de todos los elementos en un array de NumPy de tamaño 10x10, lleno de unos.
    #def punto_2(self):
        #array_unos = np.ones((10, 10))
        #suma_total = np.sum(array_unos)
        #self.df["# ejercicio"] = 2
        #self.df["valor"] = [array_unos, suma_total]
        #self.df.to_csv("Actividad_2.csv", index=False)
#ingestion = Actividad_2()
#ingestion.punto_2()
#print("array_unos, suma_total:")

#Punto_3_Dados dos arrays de tamaño 5, llenos de números aleatorios desde 1 hasta 10, realiza un producto elemento a elemento.
    #def punto_3(self):
        #array1 = np.random.randint(1, 10, 5)  
        #array2 = np.random.randint(1, 10, 5)
        #producto_elemento_a_elemento = array1 * array2
        #self.df["# ejercicio"] = 3
        #self.df["valor"] = [array1, array2, producto_elemento_a_elemento]
        #self.df.to_csv("Actividad_2.csv", index=False)
#ingestion = Actividad_2()
#ingestion.punto_3()
#print("array1, array2, producto_elemento_a_elemento:")

#Punto_4_Crea una matriz de 4x4, donde cada elemento es igual a i+j (con i y j siendo el índice de fila y columna, respectivamente) y calcula su inversa.
    #def punto_4(self):
        #matriz = np.zeros((4, 4), dtype=int)
        #for i in range(4):
            #for j in range(4):
                #matriz[i, j] = i + j
            #self.df["# ejercicio"] = 4
            #self.df["valor"] = [matriz]
            #self.df.to_csv("Actividad_2.csv", index=False)
     # Calcular la inversa de la matriz
        #try:
            #matriz_inversa = np.linalg.inv(matriz)
            #self.df["# ejercicio"] = 4
            #self.df["valor"] = [matriz, matriz_inversa ]
            #self.df.to_csv("Actividad_2.csv", index=False)
        #except np.linalg.LinAlgError:
            #print("La matriz no tiene inversa (es singular).")    
#ingestion = Actividad_2()
#ingestion.punto_4()
#print("matriz, matriz_inversa:")

#Punto_5_Encuentra los valores máximo y mínimo en un array de 100 elementos aleatorios y muestra sus índices.
    #def punto_5(self):
        #array_aleatorio = np.random.randint(0, 1000, 100)
        #valor_maximo = np.max(array_aleatorio)
        #indice_maximo = np.argmax(array_aleatorio)
        #valor_minimo = np.min(array_aleatorio)
        #indice_minimo = np.argmin(array_aleatorio)
        #self.df["# ejercicio"] = 5
        #self.df["valor"] = [array_aleatorio, valor_maximo, indice_maximo, valor_minimo,  indice_minimo]
        #self.df.to_csv("Actividad_2.csv", index=False)
#ingestion = Actividad_2()
#ingestion.punto_5()
#print("array_aleatorio, valor_maximo, indice_maximo, valor_minimo,  indice_minimo:")

#Punto_6_Crea un array de tamaño 3x1 y uno de 1x3, y súmalos utilizando broadcasting para obtener un array de 3x3.
    #def punto_6(self):
        #array_3x1 = np.array([[1], [2], [3]])
        #array_1x3 = np.array([[4, 5, 6]])
        #resultado = array_3x1 + array_1x3
        #self.df["# ejercicio"] = 6
        #self.df["valor"] = [array_3x1, array_1x3, resultado]
        #self.df.to_csv("Actividad_2.csv", index=False)
#ingestion = Actividad_2()
#ingestion.punto_6()
#print("array_3x1, array_1x3, resultado:")

#Punto_7_De una matriz 5x5, extrae una submatriz 2x2 que comience en la segunda fila y columna.
    #def punto_7(self):
            #matriz_5x5 = np.array([
                #[1, 2, 3, 4, 5],
                #[6, 7, 8, 9, 10],
                #[11, 12, 13, 14, 15],
                #[16, 17, 18, 19, 20],
                #[21, 22, 23, 24, 25]
            #])
            #submatriz_2x2 = matriz_5x5[1:3, 1:3]
            #self.df["# ejercicio"] = 7
            #self.df["valor"] = [matriz_5x5, submatriz_2x2]
            #self.df.to_csv("Actividad_2.csv", index=False)
#ingestion = Actividad_2()
#ingestion.punto_7()
#print("matriz_5x5, submatriz_2x2:")

#Punto_8_Crea un array de ceros de tamaño 10 y usa indexado para cambiar el valor de los elementos en el rango de índices 3 a 6 a 5.
    #def punto_8(self):
        #array_ceros = np.zeros(10, dtype=int)
        #array_ceros[3:7] = 5
        #self.df["# ejercicio"] = 8
        #self.df["valor"] = [array_ceros, array_ceros]
        #self.df.to_csv("Actividad_2.csv", index=False)
#ingestion = Actividad_2()
#ingestion.punto_8()
#print("array_ceros, array_ceros:")

#Punto_9_Dada una matriz de 3x3, invierte el orden de sus filas.
    #def punto_9(self):
        #matriz_3x3 = np.array([
                        #[1, 2, 3],
                        #[4, 5, 6],
                        #[7, 8, 9]
                    #])
        #matriz_invertida = matriz_3x3[::-1, :]
        #self.df["# ejercicio"] = 9
        #self.df["valor"] = [matriz_3x3, matriz_invertida]
        #self.df.to_csv("Actividad_2.csv", index=False)      
#ingestion = Actividad_2()
#ingestion.punto_9()
#print("matriz_3x3, matriz_invertida:")

#Punto_10_Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos que sean mayores a 0.5.
    def punto_10(self):
        array_aleatorio = np.random.rand(10)
        elementos_mayores = array_aleatorio[array_aleatorio > 0.5]
        self.df["# ejercicio"] = 10
        self.df["valor"] = [array_aleatorio, elementos_mayores]
        self.df.to_csv("Actividad_2.csv", index=False)      
ingestion = Actividad_2()
ingestion.punto_10()
print("array_aleatorio, elementos_mayores:")





    