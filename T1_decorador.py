import numpy as np
import matplotlib.pyplot as plt
import math
from time import perf_counter

#4. Decorador

#Listas para almacenar los tiempos
t_sol1 = []
t_sol2 = []

def tiempo_ejecucion(func):
    def fun(*args , **kwargs):
        tiempo_inicio = perf_counter()
        resultado = func(*args , **kwargs)
        tiempo_total = perf_counter() - tiempo_inicio
        
        #Guardar el tiempo en cada solución 
        if func.__name__ == 'sol_1':
            t_sol1.append(tiempo_total)
        elif func.__name__ == 'sol_2':
            t_sol2.append(tiempo_total)
        
        return resultado
    return fun


#Aplicar decorador en la clase

class caminos_pcb:
    #Inicializar los valores y agregra solucion que se desea
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M
        #Sol1 por defecto
        self.sol_elegida = self.sol_1  #Por defecto usar la solución 1

    #Solución 1 
    @tiempo_ejecucion
    def sol_1(self) -> int:
        return math.comb(self.N + self.M - 2, self.M - 1)

    #Solución 2 
    @tiempo_ejecucion
    def sol_2(self, i=0, j=0) -> int:
        if i == self.N - 1 and j == self.M - 1:
            return 1
        
        caminos = 0
        if i + 1 < self.N:
            caminos += self.sol_2(i + 1, j)
        if j + 1 < self.M:
            caminos += self.sol_2(i, j + 1)

        return caminos
    
    
    #Cambiar entre las soluciones
    def cambiar_sol(self, metodo: str) -> None:
        if metodo == 'sol_1':
            self.sol_elegida = self.sol_1
        elif metodo == 'sol_2':
            self.sol_elegida = self.sol_2
    
        #Se pueden agregar soluciones  futuras en este espacio     

    def calcular(self) -> int:
        if self.sol_elegida == self.sol_2:
            return self.sol_elegida(0, 0)  #Parámetros iniciales
        else:
            return self.sol_elegida()
    

#Graficar los tiempos de ejecución de la solución elegida
def graficar_tiempo_solucion(metodo: str):
    if metodo == 'sol_1':
        plt.plot(t_sol1, label="Solución 1")
    elif metodo == 'sol_2':
        plt.plot(t_sol2, label="Solución 2")
    
    plt.legend()
    plt.title('Tiempo de ejecución de la solución')
    plt.xlabel('Cantidad de ejecuciones')
    plt.ylabel('Tiempo')
    plt.savefig('Tiempo de ejecución de la solución', format='svg')
    plt.show()   
    

#Input para el usuario
def usuario():
    #Número de caminos
    #Pedir tamaño de PCB
    N = int(input("Introduce el valor de N (alto) para la placa PCB: "))
    M = int(input("Introduce el valor de M (ancho) para la placa PCB: "))
    pcb = caminos_pcb(N, M)
    
    #Pedir solución deseada
    metodo = input("Elige una solución ('sol_1'  o 'sol_2'): ").strip()
    pcb.cambiar_sol(metodo)
    resultado = pcb.calcular()
    print(f"El número de caminos es: {resultado}")
    
    #Tiempo de ejecución de solución escogida
    for i in range(1, 11):  
        pcb = caminos_pcb(i, i)
        pcb.cambiar_sol(metodo)
        resultado = pcb.calcular()
    graficar_tiempo_solucion(metodo)
    

#Hacer fucnionar input al usuario
if __name__ == "__main__":
    usuario()