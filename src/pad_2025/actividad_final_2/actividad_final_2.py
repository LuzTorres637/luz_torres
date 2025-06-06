from pathlib import Path
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
 


class Actividad_2:
    def __init__(self):
        self.ruta_actividad_final_2="src/pad_2025/actividad_final_2/"
        self.ruta_actual = str(Path.cwd())
        self.ruta_actividad_final_2="{}/src/pad_2025/actividad_final_2/".format(self.ruta_actual)
        directorio = os.path.dirname(self.ruta_actividad_final_2)
        if not os.path.exists(self.ruta_actual):
                os.makedirs(directorio, exists_ok=True) 
        self.ruta_img = "{}img/".format(self.ruta_actividad_final_2)
        self.ruta_csv = "{}csv/".format(self.ruta_actividad_final_2)
        print(self.ruta_actual) 
        
        datos = {
            "# ejercicio": list(range(1, 22)),
            "valor": [x*0 for x in range(1, 22)]
        }
        self.df = pd.DataFrame(data=datos,columns=["# ejercicio", "valor"])

#Genera un array de NumPy con valores desde 10 hasta 29.
    def punto_1(self, inf=10, sup=29):   
        array_10_29 = np.arange(inf,sup)
        self.df["valor"] =self.df["valor"].astype(object) 
        self.df.loc[0,"valor"] = str(array_10_29)
        print("Completo el punto 1 : ok")

#Calcula la suma de todos los elementos en un array de NumPy de tamaño 10x10, lleno de unos.    
    def punto_2(self):
        array_10x10 = np.ones((10,10))
        suma = np.sum(array_10x10)
        self.df.loc[1,"valor"] = f"{array_10x10}, {suma}"
        print("Completo el punto 2 : ok")
        
#Dados dos arrays de tamaño 5, llenos de números aleatorios desde 1 hasta 10, realiza un producto elemento a elemento.
    def punto_3(self):
        array_5_1 = np.random.randint(1,10,5)
        array_5_2 = np.random.randint(1,10,5)
        producto_elemento_a_elemento = array_5_1 * array_5_2
        self.df.loc[2,"valor"] =  f"{array_5_1}, {array_5_2}, {producto_elemento_a_elemento}"
        print("Completo el punto 3 : ok")

#Crea una matriz de 4x4, donde cada elemento es igual a i+j (con i y j siendo el índice de fila y columna, respectivamente) y calcula su inversa.
    def punto_4(self):
        matriz = np.zeros((4, 4), dtype=int)
        for i in range(4):
            for j in range(4):
                matriz[i,j] = i+j
                    # Calcular la inversa de la matriz
        try:
            matriz_inversa = np.linalg.inv(matriz)
            self.df["# ejercicio"] = 4
            #self.df["valor"] = [matriz, matriz_inversa ]
            self.df.loc[3,"valor"] = f"{matriz}, {matriz_inversa},"
        except np.linalg.LinAlgError:
            self.df.loc[3,"valor"] = f"{matriz}, {'La matriz no tiene inversa (es singular)'}"
        print("Completo el punto 4 : ok")

#Encuentra los valores máximo y mínimo en un array de 100 elementos aleatorios y muestra sus índices.
    def punto_5(self):
        array_aleatorio = np.random.rand(100)
        valor_maximo = np.max(array_aleatorio)
        indice_maximo = np.argmax(array_aleatorio)
        valor_minimo = np.min(array_aleatorio)
        indice_minimo = np.argmin(array_aleatorio)
        self.df.loc[4, "valor"] = f"{array_aleatorio}, {valor_maximo}, {indice_maximo}, {valor_minimo}, {indice_minimo}"
        print("Completo el punto 5 : ok")

#Crea un array de tamaño 3x1 y uno de 1x3, y súmalos utilizando broadcasting para obtener un array de 3x3.
    def punto_6(self):
        array_3x1 = np.random.randint(1,10,3).reshape(3,1)
        array_1x3 = np.random.randint(1,10,3).reshape(1,3)
        suma = array_3x1 + array_1x3
        self.df.loc[5,"valor"] = f"{array_3x1}, {array_1x3}, {suma}"
        print("Completo el punto 6 : ok") 
          
#De una matriz 5x5, extrae una submatriz 2x2 que comience en la segunda fila y columna.
    def punto_7(self):
        matriz = np.random.randint(0, 100, (5, 5))
        submatriz = matriz[1:3, 1:3]
        self.df.loc[6,"valor"] = f"{matriz}, {submatriz}"
        print("Completo el punto 7 : ok")

#Crea un array de ceros de tamaño 10 y usa indexado para cambiar el valor de los elementos en el rango de índices 3 a 6 a 5.
    def punto_8(self):
        array_ceros = np.zeros(10)
        array_ceros[3:7] = 5
        self.df.loc[7,"valor"] = str (array_ceros)
        print("Completo el punto 8 : ok") 

#Dada una matriz de 3x3, invierte el orden de sus filas.
    def punto_9(self):
        matriz = np.random.randint(0, 100, (3, 3))
        matriz_invertida = matriz[::-1]
        self.df.loc[8,"valor"] = f"{matriz}, {matriz_invertida}"
        print("Completo el punto 9 : ok")

#Dado un array de números aleatorios de tamaño 10, selecciona y muestra solo aquellos que sean mayores a 0.5.
    def punto_10(self):
        array_aleatorio = np.random.rand(10)
        array_mayores_05 = array_aleatorio[array_aleatorio > 0.5]
        self.df.loc[9,"valor"] = f"{array_aleatorio}, {array_mayores_05}"
        print("Completo el punto 10 : ok")

#Genera dos arrays de tamaño 100 con números aleatorios y crea un gráfico de dispersión.
    def punto_11(self,num=100):
        x = np.random.rand(num)
        y = np.random.rand(num)
        plt.scatter(x,y)
        ruta = "{}punto_11.png".format(self.ruta_img)
        plt.savefig(ruta)
        self.df.loc[10,"valor"] = f"{x}, {y}, {ruta}"
        print("Completo el punto 11 : ok")

#Genera un gráfico de dispersión, donde las variables 𝑥 y 𝑦 = 𝑠𝑖𝑛(𝑥)+ ruido Gaussiano. Donde x es un array con númereos entre -2𝜋 𝑦 2𝜋. Grafica también los puntos 𝑦 = 𝑠𝑖𝑛(𝑥) en el mismo plot.
    def punto_12(self,num=100):
        x = np.linspace(-2*np.pi, 2*np.pi, num)
        y = np.sin(x) + np.random.normal(0, 0.1, num)
        y_sin = np.sin(x)
        plt.scatter(x, y)
        plt.plot(x, np.sin(x), color="red")
        ruta = "{}punto_12.png".format(self.ruta_img)
        plt.savefig(ruta)
        ##plt.show()
        self.df.loc[11,"valor"] = str(ruta)
        print("Completo el punto 12 : ok")

#Utiliza la función np.meshgrid para crear una cuadrícula y luego aplica la función z = np.cos(x) + np.sin(y) para generar y mostrar un gráfico de contorno.
    def punto_13(self):
        x, y = np.meshgrid(np.linspace(-2*np.pi, 2*np.pi, 100), np.linspace(-2*np.pi, 2*np.pi, 100))
        z = np.cos(x) + np.sin(y)
        plt.contour(x, y, z)
        ruta = "{}punto_13.png".format(self.ruta_img)  
        plt.savefig(ruta)
        #plt.show()
        self.df.loc[12,"valor"] = str(ruta)
        print("Completo el punto 13 : ok")

#Crea un gráfico de dispersión con 1000 puntos aleatorios y utiliza la densidad de estos puntos para ajustar el color de cada punto.
    def punto_14(self):
        x = np.random.rand(1000)
        y = np.random.rand(1000)
        plt.scatter(x, y, c=x*y, cmap="viridis", alpha=0.5)
        plt.colorbar()
        ruta = "{}punto_14.png".format(self.ruta_img)
        plt.savefig(ruta)
        #plt.show()
        self.df.loc[13,"valor"] = str(ruta)
        print("Completo el punto 14 : ok")

#A partir de la misma función del punto_12, genera un gráfico de contorno lleno.
    def punto_15(self):
        x, y = np.meshgrid(np.linspace(-2*np.pi, 2*np.pi, 100), np.linspace(-2*np.pi, 2*np.pi, 100))
        z = np.cos(x) + np.sin(y)
        plt.contour(x, y, z, levels=20)
        plt.colorbar()
        ruta = "{}punto_15.png".format(self.ruta_img)
        plt.savefig(ruta)
        #plt.show()
        self.df.loc[14,"valor"] = str(ruta)
        print("Completo el punto 15 : ok")

#Añade etiquetas para el eje X (‘Eje X’), eje Y (‘Eje Y’) y un título (‘Gráfico de Dispersión’) a tu gráfico de dispersión del ejercicio 12 y crea leyendas para cada gráfico usando código LaTex
    def punto_16(self):
        x = np.linspace(-2*np.pi, 2*np.pi, 100)
        y = np.sin(x) + np.random.normal(0, 0.1, 100)
        y_sin = np.sin(x)
        plt.scatter(x, y, label=r"$y = \sin(x) + \text{ruido gaussiano}$")
        plt.plot(x, y_sin, color="red", label=r"$y = \sin(x)$")
        plt.xlabel(r"$\text{Eje X}$")
        plt.ylabel(r"$\text{Eje Y}$")
        plt.title(r"$\text{Gráfico de Dispersión}$")
        plt.legend()
        ruta = "{}punto_16.png".format(self.ruta_img)
        plt.savefig(ruta)
        #plt.show()
        self.df.loc[15,"valor"] = str(ruta)
        print("Completo el punto 16 : ok")

#Crea un histograma a partir de un array de 1000 números aleatorios generados con una distribución normal
    def punto_17(self):
        x = np.random.normal(0, 1, 1000)
        plt.hist(x, bins=30, alpha=0.5, color="blue", edgecolor="black")
        ruta = "{}punto_17.png".format(self.ruta_img)
        plt.savefig(ruta)
        #plt.show()
        self.df.loc[16,"valor"] = str(ruta)
        print("Completo el punto 17 : ok")
    
#Genera dos sets de datos con distribuciones normales diferentes y muéstralos en el mismo histograma
    def punto_18(self):
        x = np.random.normal(0, 1, 1000)
        y = np.random.normal(1, 1, 1000)
        plt.hist(x, bins=30, alpha=0.5, color="blue", edgecolor="black", label="x")
        plt.hist(y, bins=30, alpha=0.5, color="red", edgecolor="black", label="y")
        plt.legend()
        ruta = "{}punto_18.png".format(self.ruta_img)
        plt.savefig(ruta)
        #plt.show()
        self.df.loc[17,"valor"] = str(ruta)
        print("Completo el punto 18 : ok")
    
#Experimenta con diferentes valores de bins (por ejemplo, 10, 30, 50) en un histograma y observa cómo cambia la representación
    def punto_19(self):
        x = np.random.normal(0, 1, 1000)
        plt.hist(x, bins=10, alpha=0.5, color="blue", edgecolor="black", label="10")
        plt.hist(x, bins=30, alpha=0.5, color="red", edgecolor="black", label="30")
        plt.hist(x, bins=50, alpha=0.5, color="green", edgecolor="black", label="50")
        plt.legend()
        ruta = "{}punto_19.png".format(self.ruta_img)
        plt.savefig(ruta)
        #plt.show()    
        self.df.loc[18,"valor"] = str(ruta) 
        print("Completo el punto 19 : ok")
    
#Añade una línea vertical que indique la media de los datos en el histograma
    def punto_20(self):
        x = np.random.normal(0, 1, 1000)
        plt.hist(x, bins=30, alpha=0.5, color="blue", edgecolor="black")
        plt.axvline(np.mean(x), color="red", linestyle="--", label="Media")
        plt.legend()
        ruta = "{}punto_20.png".format(self.ruta_img)
        plt.savefig(ruta)
        #plt.show()
        self.df.loc[19,"valor"] = str(ruta)
        print("Completo el punto 20 : ok")

#Crea histogramas superpuestos para los dos sets de datos del ejercicio 17, usando colores y transparencias diferentes para distinguirlos
    def punto_21(self):
        x = np.random.normal(0, 1, 1000)
        y = np.random.normal(1, 1, 1000)
        plt.hist(x, bins=30, alpha=0.5, color="blue", edgecolor="black", label="x")
        plt.hist(y, bins=30, alpha=0.5, color="red", edgecolor="black", label="y")
        plt.legend()
        ruta = "{}punto_21.png".format(self.ruta_img)
        plt.savefig(ruta)
        #plt.show()
        self.df.loc[20,"valor"] = str(ruta)
        print("Completo el punto 21 : ok")
    


    def ejecutar (self):
        self.punto_1()
        self.punto_2()
        self.punto_3()
        self.punto_4()
        self.punto_5()
        self.punto_6()
        self.punto_7()
        self.punto_8()
        self.punto_9()
        self.punto_10()
        self.punto_11()
        self.punto_12()
        self.punto_13()
        self.punto_14()
        self.punto_15()
        self.punto_16()
        self.punto_17()
        self.punto_18()
        self.punto_19()
        self.punto_20()
        self.punto_21()
        self.df.to_csv("{}Actividad_2.csv".format(self.ruta_csv), index=False)

ene = Actividad_2()
ene.ejecutar()