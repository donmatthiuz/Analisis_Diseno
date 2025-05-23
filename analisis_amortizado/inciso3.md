# Inciso 3

Considere una pila común y corriente cuyo tamaño nunca excede $k$. Luego de $k$ operaciones *push* y/o *pop* se efectúa un *backup* automático, copiando toda la pila. El costo de copiar $m$ elementos es $m$. Demuestre con el *accounting method* que cualquier secuencia de $n$ operaciones entre *push* y *pop* (con *backups* cada $k$ operaciones) costará $O(n)$. *Hint*: considere los costos asignados a estas operaciones en el ejemplo *multipop*.

* Se tiene una pila con capacidad máxima $k$.
* Cada $k$ operaciones (push/pop), se realiza un backup automático que copia toda la pila.
* Copiar una pila con $m$ elementos cuesta $m$.
* Queremos demostrar que una secuencia de $n$ operaciones cuesta $\mathcal{O}(n)$ amortizadamente.

## Solución con el Método Contable

### Costos Reales

* `push`: 1
* `pop`: 1
* `backup`: $m$ (donde $m$ es el número de elementos actuales en la pila al momento del backup)

### Costos Amortizados Propuestos

* `push`: 3 (1 por el push, 1 de crédito para futuro `pop`, 1 de crédito para backup)
* `pop`: 0 (consume crédito dejado por el `push`)
* `backup`: 0 (pagado con créditos acumulados)

### Justificación de Créditos

#### 1. Push

* Cada `push` deposita:

  * 1 crédito para su eventual `pop` (como en ejemplo `multipop`)
  * 1 crédito adicional que se usará en el backup, para pagar su costo de copia
* Como máximo hay $k$ elementos en la pila, habrá como mucho $k$ créditos para backup disponibles, suficientes para cubrir el costo del backup (que es $m \leq k$)

#### 2. Pop

* Elimina un elemento de la pila
* Su costo real es 1, pero se paga con el crédito dejado por el `push`

#### 3. Backup

* Ocurre cada $k$ operaciones
* La pila tiene como máximo $k$ elementos, y cada uno tiene 1 crédito reservado para backup
* Por tanto, el costo total del backup $m$ está prepagado con los créditos acumulados

### Cálculo del Costo Total Amortizado

* Cada operación `push` cuesta amortizadamente 3
* Cada `pop` y cada `backup` cuesta 0 amortizadamente
* Como hay $n$ operaciones en total, el costo amortizado total es:

$$
\mathcal{O}(n)
$$

Mediante el método contable, asignando 3 unidades de costo a cada operación `push`, se logra cubrir:

* Su propio costo real (1)
* El costo de su `pop` futuro (1)
* Su participación en un `backup` futuro (1)

Así, el costo amortizado por operación es constante: $\mathcal{O}(1)$

Por tanto, el costo total de $n$ operaciones es $\mathcal{O}(n)$.
