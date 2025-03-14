import pandas as pd
import os
import zipfile
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from pathlib import Path
from scipy.stats import gaussian_kde 



class Actividad_2:
    def __init__(self):
        self.ruta_Actividad_2="src/pad_2025/Actividad_2/"
        self.ruta_actual = str(Path.cwd())
        self.ruta_Actividad_2="{}/src/pad_2025/Actividad_2/".format(self.ruta_actual)
        directorio = os.path.dirname(self.ruta_Actividad_2)
        if not os.path.exists(self.ruta_actual):
                os.makedirs(directorio, exists_ok=True) 
        print(self.ruta_actual) 
        
        datos = {"# ejercicio": list(range(1,21)),
            "valor": [x*0 for x in range (1,21)]
        }            
        self.df= pd.DataFrame( data=datos, columns=["# ejercicio", "valor"])  

#Punto_1_Genera un array de NumPy con valores desde 10 hasta 29.
    def punto_1(self):
        array_10_29 = np.arange(10, 30)
        self.df.iloc[0,1]= str (array_10_29)
        self.df["# ejercicio"] = 1
        self.df.loc[0,"valor"]= str (array_10_29)
        
#Punto_2_Calcula la suma de todos los elementos en un array de NumPy de tamaño 10x10, lleno de unos.
    def punto_2(self):
        array_unos = np.ones((10, 10))
        suma_total = np.sum(array_unos)
        self.df["# ejercicio"] = 2
        self.df.loc[1,"valor"]= str(array_unos)
        self.df.loc[2,"valor"]= str(suma_total)
            
#Punto_3_Dados dos arrays de tamaño 5, llenos de números aleatorios desde 1 hasta 10, realiza un producto elemento a elemento.
    def punto_3(self):
        array1 = np.random.randint(1, 10, 5)  
        array2 = np.random.randint(1, 10, 5)
        producto_elemento_a_elemento = array1 * array2
        self.df["# ejercicio"] = 3
        self.df.loc[3, "valor"] = str(producto_elemento_a_elemento.tolist())
            
#Punto_4_Crea una matriz de 4x4, donde cada elemento es igual a i+j (con i y j siendo el índice de fila y columna, respectivamente) y calcula su inversa.
    def punto_4(self):
        matriz = np.zeros((4, 4), dtype=int)
        for i in range(4):
            for j in range(4):
                matriz[i, j] = i + j
            self.df["# ejercicio"] = 4
            self.df.loc[4,"valor"] = [matriz]
    # Calcular la inversa de la matriz
        try:
            matriz_inversa = np.linalg.inv(matriz)
            self.df["# ejercicio"] = 4
            self.df.loc[5,"valor"] = [matriz, matriz_inversa ]
        except np.linalg.LinAlgError:
            print("La matriz no tiene inversa (es singular).")    
          

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
    #def punto_10(self):
        #array_aleatorio = np.random.rand(10)
        #elementos_mayores = array_aleatorio[array_aleatorio > 0.5]
        #self.df["# ejercicio"] = 10
        #self.df["valor"] = [array_aleatorio, elementos_mayores]
        #self.df.to_csv("Actividad_2.csv", index=False)      
#ingestion = Actividad_2()
#ingestion.punto_10()
#print("array_aleatorio, elementos_mayores:")

#Punto_11_Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.
    #def __init__(self):
        #self.ruta_Actividad_2="src/pad_2025/Actividad_2/"
        #self.ruta_actual = str(Path.cwd())
        #self.ruta_Actividad_2="{}/src/pad_2025/Actividad_2/".format(self.ruta_actual)
        #directorio = os.path.dirname(self.ruta_Actividad_2)
        #if not os.path.exists(self.ruta_actual):
                #os.makedirs(directorio, exists_ok=True)
        #datos= [(1,0), (0,1)]
        #self.df= pd.DataFrame( data=datos, columns=["# ejercicio", "valor"])  
   #def punto_11(self):
        #array_1 = np.random.rand(100)
        #array_2 = np.random.rand(100)
        #plt.figure(figsize=(8, 6))  
        #plt.scatter(array_1, array_2)
        #plt.xlabel("Eje X")
        #plt.ylabel("Eje Y")
        #plt.title("Gráfico de dispersión de números aleatorios")
        #plt.savefig(self.ruta_Actividad_2 + "punto_11.png")
        #plt.show()     
#ingestion = Actividad_2()
#ingestion.punto_11()
#print("plt.show:")

#Punto_12_Genera un gráfico de dispersión las variables 𝑥 y 𝑦 = 𝑠𝑖𝑛(𝑥)+ ruido Gaussiano. Donde x es un array con númereos entre -2𝜋 𝑦 2𝜋. Grafica también los puntos 𝑦 = 𝑠𝑖𝑛(𝑥) en el mismo plot.
    #def punto_12(self):
        #x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
        #y_sin = np.sin(x)
        #ruido = np.random.normal(0, 0.3, 100)
        #y_ruido = y_sin + ruido
        #plt.figure(figsize=(10, 6))
        #plt.scatter(x, y_ruido, label='sin(x) + ruido', s=15)
        #plt.plot(x, y_sin, color='red', label='sin(x)')
        #plt.xlabel('x')
        #plt.ylabel('y')
        #plt.title('Gráfico de sin(x) con ruido')
        #plt.legend()
        #plt.savefig(self.ruta_Actividad_2 + "punto_12.png")
        #plt.grid(True)
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_12()
#print("plt.show:")

#Punto_13_Utiliza la función np.meshgrid para crear una cuadrícula y luego aplica la función z = np.cos(x) + np.sin(y) para generar y mostrar un gráfico de contorno.
    #def punto_13(self):
        #x = np.linspace(-5, 5, 100)
        #y = np.linspace(-5, 5, 100)
        #X, Y = np.meshgrid(x, y)
        #Z = np.cos(X) + np.sin(Y)
        #plt.figure(figsize=(8, 6))
        #contour = plt.contour(X, Y, Z, levels=20, cmap='viridis')  
        #plt.clabel(contour, inline=True, fontsize=8)
       # plt.xlabel('x')
        #plt.ylabel('y')
        #plt.title('Gráfico de contorno de z = cos(x) + sin(y)')
        #plt.colorbar() # Añadir barra de color
        #plt.grid(True)
        #plt.savefig(self.ruta_Actividad_2 + "punto_13.png")
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_13()
#print("plt.show:")

#Punto_14_Crea un gráfico de dispersión con 1000 puntos aleatorios y utiliza la densidad de estos puntos para ajustar el color de cada punto.
    #def punto_14(self):
        #x = np.random.normal(size=1000)
        #y = np.random.normal(size=1000)
        #xy = np.vstack([x, y])
        #z = gaussian_kde(xy)(xy)
        #idx = z.argsort()
        #x, y, z = x[idx], y[idx], z[idx]
        #plt.figure(figsize=(8, 6))
        #plt.scatter(x, y, c=z, s=50, cmap='viridis')
        #plt.xlabel('x')
        #plt.ylabel('y')
        #plt.title('Gráfico de dispersión con densidad de color')
        #plt.savefig(self.ruta_Actividad_2 + "punto_14.png")
        #plt.colorbar()
        #plt.grid(True)
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_14()
#print("plt.show:")

#Punto_15_A partir de la misma función del ejercicio 12, genera un gráfico de contorno lleno.
    #def punto_15(self):
       # x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
       # ruido = np.random.normal(0, 0.3, 100)  
        #y = np.sin(x) + ruido
        #X, Y = np.meshgrid(x, y)
        #Z = np.sin(X) + np.random.normal(0, 0.3, X.shape)      
        #plt.figure(figsize=(8, 6))
        #contourf = plt.contourf(X, Y, Z, levels=20, cmap='viridis')
       #plt.xlabel('x')
        #plt.ylabel('y')
        #plt.title('Gráfico de contorno lleno de z = cos(x) + sin(y)')
        #plt.colorbar(contourf)
        #plt.grid(True)
        #plt.savefig(self.ruta_Actividad_2 + "punto_15.png")
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_15()
#print("plt.show:")

#Punto_16_Añade etiquetas para el eje X (‘Eje X’), eje Y (‘Eje Y’) y un título (‘Gráfico de Dispersión’) a tu gráfico de dispersión del ejercicio 12 y crea leyendas para cada gráfico usando código LaTex.
    #def punto_16(self):
        #x, y = punto_12()
        #plt.figure(figsize=(8, 6))
        #plt.scatter(x, y_ruido, label=r'$\sin(x) + \mathrm{ruido}$', s=15)
        #plt.plot(x, y_sin, color='red', label=r'$\sin(x)$')
        #plt.xlabel(r'$\mathrm{Eje\ X}$')
        #plt.ylabel(r'$\mathrm{Eje\ Y}$')
        #plt.title(r'$\mathrm{Gráfico\ de\ Dispersión}$')
        #plt.legend()
        #plt.grid(True)
        #plt.savefig(self.ruta_Actividad_2 + "punto_16.png")
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_16()
#print("plt.show:")

#Punto_17_Crea un histograma a partir de un array de 1000 números aleatorios generados con una distribución normal.
    #def punto_17(self):
        #data = np.random.normal(size=1000)
        #plt.figure(figsize=(8, 6))
        #plt.hist(data, bins=30, edgecolor='black')
        #plt.xlabel('Valor')
        #plt.ylabel('Frecuencia')
        #plt.title('Histograma de distribución normal')
        #plt.grid(True)
        #plt.savefig(self.ruta_Actividad_2 + "punto_17.png")
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_17()
#print("plt.show:")

#Punto_18_Genera dos sets de datos con distribuciones normales diferentes y muéstralos en el mismo histograma.
    #def punto_18(self):
        #data1 = np.random.normal(loc=0, scale=1, size=1000)  
        #data2 = np.random.normal(loc=3, scale=1.5, size=1000)
        #plt.figure(figsize=(10, 6))
        #plt.hist(data1, bins=30, alpha=0.5, label='Distribución 1')
        #plt.hist(data2, bins=30, alpha=0.5, label='Distribución 2')
        #plt.xlabel('Valor')
        #plt.ylabel('Frecuencia')
        #plt.title('Histograma de dos distribuciones normales')
        #plt.legend()
        #plt.grid(True)
        #plt.savefig(self.ruta_Actividad_2 + "punto_18.png")
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_18()
#print("plt.show:")

#Punto_19_Experimenta con diferentes valores de bins (por ejemplo, 10, 30, 50) en un histograma y observa cómo cambia la representación.
    #def punto_19(self):
        #data = np.random.normal(size=1000)
        #bins_values = [10, 30, 50]
        #plt.figure(figsize=(12, 6))
        #for i, bins in enumerate(bins_values):
            #plt.subplot(1, 3, i + 1)  
           # plt.hist(data, bins=bins, edgecolor='black')
            #plt.xlabel('Valor')
            #plt.ylabel('Frecuencia')
            #plt.title(f'Histograma con {bins} bins')
            #plt.grid(True)
        #plt.savefig(self.ruta_Actividad_2 + "punto_19.png")
        #plt.tight_layout()  
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_19()
#print("plt.show:")

#Punto_20_Añade una línea vertical que indique la media de los datos en el histograma.
    #def punto_20(self):
        #data = np.random.normal(size=1000)        
       # media = np.mean(data)
        #plt.figure(figsize=(8, 6))
        #plt.hist(data, bins=30, edgecolor='black')
        #plt.axvline(media, color='red', linestyle='dashed', linewidth=2, label=f'Media: {media:.2f}')
        #plt.xlabel('Valor')
        #plt.ylabel('Frecuencia')
        #plt.title('Histograma con media')
        #plt.legend()
        #plt.savefig(self.ruta_Actividad_2 + "punto_20.png")
        #plt.grid(True)
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_20()
#print("plt.show:")    

#Punto_21_Crea histogramas superpuestos para los dos sets de datos del ejercicio 17, usando colores y transparencias diferentes para distinguirlos.
    #def punto_21(self):
        #data1 = np.random.normal(loc=0, scale=1, size=1000)  # Media 0, desviación estándar 1
        #data2 = np.random.normal(loc=3, scale=1.5, size=1000)  # Media 3, desviación estándar 1.5
        #plt.figure(figsize=(10, 6))
        #plt.hist(data1, bins=30, alpha=0.5, color='skyblue', label='Distribución 1')
        #plt.hist(data2, bins=30, alpha=0.5, color='salmon', label='Distribución 2')
        #plt.xlabel('Valor')
        #plt.ylabel('Frecuencia')
        #plt.title('Histogramas superpuestos de dos distribuciones normales')
        #plt.legend()
        #plt.savefig(self.ruta_Actividad_2 + "punto_21.png")
        #plt.grid(True)
        #plt.show()
#ingestion = Actividad_2()
#ingestion.punto_21()
#print("plt.show:")   

    def ejecutar(self):
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
        #self.punto_13()
        #self.punto_14()
        #self.punto_15()
        #self.punto_16()
        #self.punto_17()
        #self.punto_18()
        #self.punto_19()
        #self.punto_20()
        #self.punto_21()
        self.df.to_csv("Actividad_2.csv", index= "false")

ene = Actividad_2()
ene.ejecutar()