# Inciso 4

Suponga que al contador binario de los ejemplos se le agrega la operación *reset* que busca y convierte todos los $1$ en $0$, uno por uno a partir del bit menos significativo. Demuestre con el *accounting method* que cualquier secuencia de $n$ operaciones entre *increment* y *reset* toma un tiempo de ejecución de $O(n)$. Considere que el contador inicia desde $0$ y que cada revisión y cada modificación de un bit toma $\Theta(1)$. *Hint*: ¿hasta qué bit del número binario debe llegar *reset* en cualquier momento, y cómo podemos asegurar que todos los bits que *reset* modifique tengan crédito para pagar por su reseteo?

## Planetamiento

El contador hace esto nuevo

- Suma 1 con icrement
- Vuelve todos a 0 con reset.

Cada revision de un bit toma de tiempo $\Theta(1)$.


Las operaciones hacen lo siguiente


### Increment:

- Cambia algunos bits de 1 a 0 (los menos significativos) y un bit de 0 a 1

- Costo : 1 + número de 1s consecutivos desde la derecha


### Reset:

- Recorre desde el bit menos significativo
- Cambia los bits están en 1 a 0 osea los resetea.

- Costo: Numeros de 1s hasta la derecha

## Solucion 

En el accountng metod ponemos por decirlo asi creditos al costo de las operaciones. 

Las operaciones de reset seran gratis esto quiere decir que operaciones anteriores pagarn su costo.

Asignar creditos:

- Si incrementamos ponemos 1 credito por incremento. Esto significa que tomaria todo lo de la cadena en cambiar osea O(k + 1)

- Ahora asignamos 2 creditos a increment esto porque 1 para recubrir el reseteo y 1 para el cambio. 

- Para reset realmente ya lo pagamos por lo que no pagamos nada, ya que ese bit cuando fue puesto en 1. Entonces los creditos depositados que tomamos del increment los usamos.

### Demostracion

El costo amortizado total es $\leq$ 2n

Ahora con el metodo de accounting sabemos que 

$$Costo Real Total≤Costo Amortizado Total$$

Y como habiamos visto antes que lo que constaba cada operacion reemplazamos

$$Costo Amortizado Total \leq 2⋅(Numero De Increment) + 0(Numero de Reset)$$


$$Costo Amortizado Total \leq 2⋅(n) + 0(n)$$

$$Costo Amortizado Total \leq 2⋅(n)$$

Como el costo es menor a 2n entonces podemos decir que el costo es lineal por ende

$$O(n)$$


Esto se da gracias  a que el reset llega hasta el primer 0, ya no hay más 1s consecutivos desde la derecha.

Con ello podemos asegurar que el credito de cada bit este dado, porque el increment deposita créditos (1 crédito por cada bit que pone en 1) y el reset solo los gasta