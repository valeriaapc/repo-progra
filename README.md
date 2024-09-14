# Tarea 1 

## Parte Teórica

### • ¿Qué es un paradigma de programación?

Un paradigma de programación, son las formas de clasificar los lenguajes de programación en función de sus características, proporcionan un conjunto de principios y métodos para diseñar programas y resolver problemas computacionales. Como lo es el paradigma de programación orientada a objetos. 


### • ¿En qué se basa la programación orientada a objetos?

Se basa en crear una estructura molde llamada clase donde se especifican los atributos y métodos que tendrán nuestros objetos, cuyos objetos se podran crear y manipular de acuerdo a lo deseado.

### • ¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación big 𝑂?

Recursividad es un enfoque en el que una función se llama a sí misma para resolver un problema más pequeño del mismo tipo, pero puede tener un coste adicional de memoria. La iteración, en cambio, implica el uso de estructuras como bucles (for o while) para repetir una serie de instrucciones hasta cumplir una condición.

En términos de notación Big O, la complejidad de un algoritmo recursivo o iterativo depende del número de pasos y del crecimiento de la entrada. Un algoritmo recursivo que reduce el problema a la mitad en cada llamada puede tener una complejidad O(log n). Por otro lado, un bucle iterativo que recorre todos los elementos tiene una complejidad O(n).

### • Explicar la diferencia de rendimiento entre 𝑂(1) y 𝑂(𝑛)

O(1) tiene un tiempo de ejecución constante independientemente del tamaño de la entrada. En cambio, para O(n) el tiempo de ejecución crece de manera proporcional al tamaño de la entrada, por lo que tiene un comportamiento lineal. Por esta razón O(1) es más eficiente que O(n), ya que siempre toma el mismo timepo de ejecución y no depende del tamaño de los datos.

### • ¿Cómo se calcula el orden en un programa que funciona por etapas?

El orden de la complejidad total suele ser la suma de las complejidades de cada etapa. Si una etapa tiene una complejidad mayor que las otras, esta dominará la complejidad total y el programa se dirá que es de ese orden mayor. 

### • ¿Cómo se puede determinar la complejidad temporal de un algoritmo recursivo?

La función de complejidad de un algoritmo recursivo queda determinada por la función recurrente que lo caracterice.
Para determinarla, se debe obtener la función recursiva en forma de ecuación que describe cuántas veces se llama a sí misma y cómo crece el problema. Luego, usando técnicas como expansión de la recurrencia se puede obtener la complejidad en notación Big O.


## Parte Práctica

### Soluciones 

El código de solciones, tiene como objetivo calcular la cantidad de caminos posibles entre dos puntos en una PCB, simplificada como una grilla de tamaño NxM. El punto de inicio es A(0,0) que está en la esquina superior izquierda, y el punto de destino B(N−1,M−1) que está en la esquina inferior derecha. 

Una vez que la clase está iniciada, el primer método de solución, sol_1, utiliza una fórmula combinatoria para calcular cuántos caminos existen desde A hasta B. Dado que para llegar de A a B se necesitan realizar exactamente N−1 movimientos hacia abajo y M−1 movimientos hacia la derecha, el número de maneras de combinar estos movimientos es equivalente a una combinatoria de la forma C(N+M−2, M−1), que se calcula con la función math.comb().

Por otro lado, el método sol_2 es una solución recursiva para calcular el mismo número de caminos. El punto de partida es siempre A(0,0), y a través de llamadas recursivas, la solución realiza todos los posibles movimientos hacia abajo y hacia la derecha, y continúa hasta que alcanza el punto final B(N−1,M−1), momento en el cual se cuenta un camino. Si el algoritmo puede moverse hacia abajo o hacia la derecha, sigue llamando a sí mismo, acumulando el número de caminos.

### Tiempo de ejecución 

El código mide y compara el tiempo de ejecución de las dos soluciones (sol_1 y sol_2). Se crean dos listas (t_sol1 y t_sol2) para almacenar los tiempos de cada solución. Para cada tamaño de grilla, se instancia la clase caminos_pcb, y se mide el tiempo de ejecución de cada solución usando perf_counter(). Los tiempos se almacenan en las listas correspondientes. Finalmente, se grafican los tiempos de ejecución de ambas soluciones, se guarda el gráfico como un archivo SVG y se muestra en pantalla. El código permite comparar visualmente el rendimiento de las dos soluciones para diferentes tamaños de grilla.

Además, se realiza una función qeu recibe otra función para el timepo de ejecución. La función tiempo_ejecucion mide el tiempo de ejecución de cualquier función que le pases como argumento. Utiliza perf_counter() para registrar el tiempo de inicio y fin de la ejecución de la función proporcionada, luego almacena la duración en una lista t_func y la imprime. Se le puede pasar cualquiera de las soluciones, como pcb.sol_1, y así evitar repetir el mismo código varias veces. Este enfoque es más eficiente, porque si tuvieras 6 soluciones distintas, ya que solo hay que pasar cada función como argumento a tiempo_ejecucion, sin necesidad de escribir múltiples funciones repetitivas para medir el tiempo de cada una.

### Decorador 


El código utiliza un decorador tiempo_ejecucion para medir y almacenar el tiempo de ejecución de las funciones sol_1 y sol_2. Este decorador permite reutilizar la lógica de medición para cualquier función que se le pase, almacenando los tiempos en listas (t_sol1 y t_sol2). A la clase caminos_pcb que contiene dos soluciones, se le incluye el método cambiar_sol para alternar entre soluciones y calcular para ejecutar la solución seleccionada.

La función graficar_tiempo_solucion genera un gráfico de los tiempos de ejecución, guardándolo en formato SVG, con etiquetas y leyenda. La función usuario interactúa con el usuario para obtener los valores de N y M, y permite elegir la solución a usar, generando finalmente el gráfico de los tiempos de ejecución.El decorador permite que el código sea flexible, ya que permite agregar nuevas soluciones fácilmente decorándolas con @tiempo_ejecucion y añadiéndolas al método cambiar_sol.

