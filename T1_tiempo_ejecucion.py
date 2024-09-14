import numpy as np
import matplotlib.pyplot as plt
import math
from time import perf_counter

#Creación de soluciones
class caminos_pcb:
    #Inicializar los valores de N y M  de la PCB
    def __init__(self, N: int, M: int) -> None:
        self.N = N
        self.M = M

    #Solución 1 usando una combinatoria
    def sol_1(self) -> int:
        #A(0,0) y B(N−1,M−1) (N−1 movimientos hacia abajo y M−1 movimientos hacia la derecha)
        # número de maneras de elegir M-1 posiciones en una secuencia de N+M-2 movimientos es una combinatoria de la forma:
        return math.comb(self.N + self.M - 2, self.M - 1)


    #Solución 2 con método recursivo.
    def sol_2(self, i=0, j=0) -> int:

        #A(0,0) y B(N−1,M−1) (N−1 movimientos hacia abajo y M−1 movimientos hacia la derecha)
        #Caso base: Llega de A a B y se cuenta como 1 camino
        if i == self.N - 1 and j == self.M - 1:
            return 1

        #Iniciar conteo de numero de caminos
        caminos = 0
        #Si no está en la ultima fila, se mueve hacia abajo
        if i + 1 < self.N:
            caminos += self.sol_2(i + 1, j)
        #Si no está en la ultima columna, se mueve hacia la derecha
        if j + 1 < self.M:
            caminos += self.sol_2(i, j + 1)

        #Devuelve número de caminos posibles cuando ya se encuentra en la ultima fila y columna
        return caminos

#pcb = caminos_pcb(4, 4)
#print("Caminos combinatorios:", pcb.sol_1())
#print("Caminos recursivos", pcb.sol_2())

#1. Tiempo de ejecución
#Listas para almacenar los tiempos
t_sol1 = []
t_sol2 = []


for i in range(1, 10):  
    pcb = caminos_pcb(i, i)  

    #Tiempo ejecución sol_1
    tiempo_inicio = perf_counter()
    pcb.sol_1()  
    tiempo_total = perf_counter() - tiempo_inicio
    t_sol1.append(tiempo_total)  

    #Tiempo ejecución sol_2
    tiempo_inicio = perf_counter()
    pcb.sol_2()  
    tiempo_total = perf_counter() - tiempo_inicio
    t_sol2.append(tiempo_total)  

print("Tiempos sol_1:", t_sol1)
print("Tiempos sol_2:", t_sol2)

#Graficar 
plt.plot(t_sol1, label=r"sol1")
plt.plot(t_sol2, label=r"sol2")
plt.legend()
plt.title('Tiempo de ejecución de soluciones')
plt.xlabel('Cantidad de ejecuciones')
plt.ylabel('Tiempo')

#Guardar el gráfico como SVG
plt.savefig('Tiempo de ejecución de soluciones', format='svg')
plt.show()


#2. Función de tiempo 

def tiempo_ejecucion(func): 
    t_func = []
    for i in range(1):  
        pcb = caminos_pcb(i, i)  

        #Tiempo ejecución sol_1
        tiempo_inicio = perf_counter()
        func()
        tiempo_total = perf_counter() - tiempo_inicio
        t_func.append(tiempo_total)
    
    return print("Tiempo de ejecución:", t_func)
    
#tiempo_ejecucion(pcb.sol_1)