# Preguntas 11 - 13

## **Pregunta 11:**

**¿Por qué la elección de un pivote fuera del intervalo \[yi, yj] no influye en la probabilidad de que estos elementos sean comparados? ¿Cuántos elementos hay en el intervalo \[yi, yj]?**

**Respuesta:**

La elección de un pivote **fuera del intervalo \[yi, yj]** (es decir, menor que yi o mayor que yj) no afecta la posibilidad de que **yi y yj se comparen**, porque ambos seguirán en la misma sublista después de esa partición. Solo se separarán cuando el pivote elegido esté dentro del intervalo (es decir, que divida a yi y yj).

Dado que Quicksort es recursivo, solo se realiza la comparación **si ambos permanecen en la misma sublista hasta que uno de ellos sea elegido como pivote**. Así, el evento de comparación depende exclusivamente de que **ningún elemento del intervalo (yi, ..., yj)** sea elegido como pivote **antes** que yi o yj.

El número de elementos en el intervalo \[yi, yj] es:

$$
j - i + 1
$$

Por lo tanto, la **probabilidad de que yi y yj sean comparados** es:

$$
E[X_{ij}] = \frac{2}{j - i + 1}
$$

Esta probabilidad se deriva del hecho de que solo yi o yj deben ser seleccionados como pivote antes que cualquier otro elemento entre ellos.

## **Pregunta 12:**

**¿Será igual la cota del tiempo de ejecución para la versión no aleatorizada? ¿Por qué?**

**Respuesta:**

**No, no será igual en todos los casos.**

En la versión no aleatorizada, si siempre se elige un pivote en una posición fija (como el primer o último elemento), es posible construir entradas específicas que **siempre generen el peor caso**: sublistas altamente desbalanceadas. Esto lleva a un tiempo de ejecución de:

$$
O(n^2)
$$

En cambio, en la versión aleatorizada o con análisis probabilístico (asumiendo permutación aleatoria del input), se garantiza que en promedio el pivote estará cerca del centro del subarreglo, y por tanto, se logra un rendimiento de:

$$
E[X] = O(n \log n)
$$

Además, la aleatorización tiene la ventaja de **proteger al algoritmo contra entradas maliciosamente diseñadas** para forzar el peor caso, algo que no es posible en la versión determinista.

## **Pregunta 13:**

**¿Qué impacto tendrá sobre el tiempo de ejecución el revolver el input antes de proceder con el análisis probabilístico? Investigue sobre el tiempo de ejecución de los generadores de números pseudo-aleatorios.**

**Respuesta:**

Revolver el input (es decir, aleatorizarlo antes de aplicar Quicksort) transforma el análisis determinista en uno probabilístico. El impacto clave es que **reduce el riesgo de caer en el peor caso**, lo que estabiliza el rendimiento del algoritmo.

El costo adicional por aleatorizar es generalmente **lineal**, $O(n)$, usando algoritmos como **Randomize-In-Place**, que tiene tiempo esperado eficiente y no requiere ordenamiento. Además, revolver el input es equivalente (en distribución) a seleccionar pivotes aleatorios, por lo que se conserva el análisis probabilístico.

Sobre los **[generadores de números pseudoaleatorios](https://keepcoding.io/blog/generador-de-numeros-pseudoaleatorios/) (PRNG)**:

* Son algoritmos diseñados para producir secuencias de números que **simulan ser aleatorios**, pero que son generados de manera determinista a partir de una semilla inicial.
* Los más comunes, como `rand()` o `random()`, suelen estar basados en **métodos de congruencia lineal**, que permiten generar rápidamente un nuevo número pseudoaleatorio usando operaciones simples (suma, multiplicación y módulo).
* Debido a su simplicidad, la generación de cada número pseudoaleatorio requiere solo unas pocas instrucciones de máquina, lo cual significa que operan en **tiempo constante $O(1)$** o a lo sumo **logarítmico** en algunos casos menos comunes.
* Por tanto, **el costo de generar estos números es muy bajo** comparado con el resto del algoritmo Quicksort, cuyo tiempo total de ejecución esperado es $O(n \log n)$. Incluso si se generan $n$ números aleatorios, el costo agregado sigue siendo **lineal**, es decir, $O(n)$.

**Conclusión:** Revolver el input cuesta poco, pero **mejora significativamente** el comportamiento esperado del algoritmo, evitando el peor caso y garantizando un rendimiento estable.
