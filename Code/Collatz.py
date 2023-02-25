#Importamos las librerias que utilizaremos
import matplotlib.pyplot as plt # Libreria para graficar
import numpy as np # Libreria para hacer operaciones matematicas

def collatz(n): # Funcion que calcula el indice de collatz para un numero n
    lista = [] # lista donde se guardaran los numeros
    
    while n != 1: # Mientras n sea diferente de 1, se ejecutara el condicional
        lista.append(n) # Se agrega el valor de n a la lista
        
        if n % 2 == 0: # Si el residuo de n entre 2 es igual a 0, significa que n es par
          
            n = n / 2 # Si n es par, se divide entre 2
            
        else: # Si n no es par
          
            n = 3 * n + 1 # Si n es impar, se multiplica por 3 y se le suma 1
            
    lista.append(1) # Se agrega el valor de 1 a la lista
    return lista

def graficar():
    x = np.linspace(1, 1000, 1000) # Se crea una lista de 1000 numeros (puntos) entre 1 y 1000
    y = [] # Lista que guardara los valores de los indices de collatz
    
    for i in range(1, 1001): # Se calcula el indice de collatz para cada numero entre 1 y 1000
        y.append(len(collatz(i))) # Se agrega el valor del indice de collatz a la lista y
    plt.plot(x, y, 'b-') # Se grafica la curva de collatz (graficamos los puntos)
    
    plt.title('Grafica de Collatz') # Se grafica la curva y=x
    
    plt.xlabel('Numero') # Se agrega titulo al eje x
    
    plt.ylabel('Indice de Collatz') # Se agrega titulo al eje y
    
    plt.show() # Se muestra la grafica

if __name__ == '__main__': #
    graficar() # Se llama a la funcion graficar


    
