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

