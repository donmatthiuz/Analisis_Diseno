# Proyecto 1 Analisis y Diseño de Algoritmos

## Integrantes

- Pedro Pablo Guzman
- Mathew Cordero Aquino

## Problema elegido.

**Problema de la devolucion de Monedas o Coin Change Problem**

### Definicion

Dada una cantidad específica de cambio a devolver y un número ilimitado de cada tipo de monedas, ¿cuál es la menor cantidad de monedas necesarias para alcanzar la cantidad de cambio especificada?


Se sabe que :

- Existen infinitas monedas de cada tipo

- Las monedas son potencias de k {k^0, k^1,.. ,k^n}
- Si no se cumple, el algoritmo no encontrara la solucion optima

### Fuentes


- cs. (2014). Problema de creación de cambios. Obtenido de Pagium: https://en-m-wikipedia-org.translate.goog/wiki/Change-making_problem?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
- Dumadag, J. (2019). Solving the Coin Change problem with Dynamic Programming. Obtenido de Medium: https://medium.com/@j.dumadag718/solving-the-coin-change-problem-with-dynamic-programming-2910ac075ddd 




## Algoritmos de Solucion

### DAC



### DP


En este usaremos un enfoque botton up, definiendo lo siguiente

- n monedas seran X1, X2 ... Xn
- cantidad a devolver c
- cambio(n,c) minimas monedas para devolver c usando X1, .....Xn
- Si Xn > c descartamos usar Xn
- cambio  = cambio (n-1,c)
- Si Xn< c podemos usar o no Xn
- Si usamos Xn cambio (n, c-Xn)+1
- Si no lo usamos cambio (n-1,c)
- Escogemos la minima cantidad

Ahora usaremos una tabla de tipo t[i, j] el numero de monedas es el valor de Xi para devolver la cantidad j de esas monedas.

- j = cambio a devolver
- i = tipo de monedas
- i,j = cantidad de monedas de cada valor

#### Fuentes:

- López, F. (2021). Programación Dinámica: Devolución de Cambio de Monedas. Obtenido de Youtube: https://www.youtube.com/watch?v=Sf4OKx1Wz9w


## Analisis Teorico

### DAC

### DP


## Analisis Empirico

### DAC

### DP


Podemos ver en el siguiente grafico el resultado de compilar 30 diferentes tipos de cambios para los tipos de monedas {1,5,10,12,25,50}

