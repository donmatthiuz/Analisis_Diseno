# Inciso 6

Un *min-heap* binario es un árbol binario completo (todos sus niveles están llenos y sus hojas se llenan de izquierda a derecha) en donde cada nodo es menor que todos sus hijos. El *min-heap* tiene una operación de inserción llamada *insert*, pero consideremos además la función *extract-min*, que reemplaza la raíz por el último nodo del árbol y luego la intercambia con el menor de sus hijos. Supongamos que ambas operaciones tienen un tiempo de ejecución real $O(\log\_2 n)$. Provea una función de potencial según la cual el costo amortizado de *insert* sea $O(\log\_2 n)$ y el de *extract-min* sea $O(1)$. No olvide que el potencial siempre debe ser positivo (no necesariamente el cambio de potencial), y que el potencial inicial es idealmente cero. Demuestre que su función de potencial funciona.

*Hint:* primero considere la forma que tendrá el costo real de cada operación. Con esto en mente, escriba la fórmula de costo amortizado, usando valores en el cambio de potencial de forma que al sumarlo con el costo real se obtengan los costos amortizados deseados (claramente en uno de los casos el cambio de potencial debe resultar menor a $O(\log n)$; y en el otro caso debe ser negativo). ¿Qué característica(s) de un árbol binario completo se miden con un $\log\_2 \blacksquare$? ¿Cómo cambia(n) esta(s) característica(s) luego de un *insert* o un *extract-min*? Recuerde que el potencial debe extraerse de alguna propiedad *de la estructura de datos*.

## Función de Potencial Propuesta

Para un **min-heap binario completo** con $n$ elementos, definimos la función de potencial como:

$$
\Phi(H) = \sum_{i=1}^{n} \log_2(\text{altura del nodo } i + 1)
$$

Donde la **altura de un nodo** es la distancia máxima desde ese nodo hasta una hoja.

### Propiedades de la Función de Potencial

1. $\Phi(H) \geq 0$: Siempre positiva, ya que $\log_2(\text{altura} + 1) \geq 0$ para cualquier nodo.
2. $\Phi(\emptyset) = 0$: Un heap vacío tiene potencial cero.
3. Extrae información estructural: El potencial refleja qué tan "desbalanceado" está el árbol.

---

## Análisis de las Operaciones

### Operación INSERT

**Costo real:**

$$
C_r(\text{insert}) = \mathcal{O}(\log_2 n)
$$

**Cambio de potencial:**

- Se añade un nuevo nodo como hoja (altura 0): $\log_2(1) = 0$
- Los nodos en el camino a la raíz pueden cambiar su contribución

$$
\Delta\Phi = \mathcal{O}(\log_2 n)
$$

**Costo amortizado:**

$$
C_a(\text{insert}) = C_r + \Delta\Phi = \mathcal{O}(\log_2 n)
$$

---

### Operación EXTRACT-MIN

**Costo real:**

$$
C_r(\text{extract-min}) = \mathcal{O}(\log_2 n)
$$

**Cambio de potencial:**

- Eliminación de la raíz (altura $h = \lfloor \log_2 n \rfloor$):

$$
\Delta\Phi = -\log_2(h + 1) = -\log_2(\lfloor \log_2 n \rfloor + 1) = -\Omega(\log \log n)
$$

**Costo amortizado:**

$$
C_a(\text{extract-min}) = \mathcal{O}(\log_2 n) - \Omega(\log \log n) = \mathcal{O}(1)
$$

---

## Demostración Formal

### Características del Árbol Binario Completo

- Altura total: 

$$
h = \lfloor \log_2 n \rfloor
$$

- Número de nodos en el nivel $i$:

$$
2^i \quad \text{para } i = 0, 1, \dots, h-1
$$

- Altura de un nodo en el nivel $i$:

$$
h - i
$$

---

### Cálculo del Potencial Total

$$
\Phi(H) = \sum_{i=0}^{h-1} 2^i \cdot \log_2(h - i + 1)
$$

---

## Análisis del Extract-Min

1. **Eliminación de la raíz**:

$$
\Delta\Phi = -\log_2(h + 1) = -\Omega(\log \log n)
$$

2. **Reorganización:**

$$
C_r = \mathcal{O}(\log_2 n)
$$

3. **Costo amortizado:**

$$
C_a = \mathcal{O}(\log_2 n) - \Omega(\log \log n) = \mathcal{O}(1)
$$

---

## Validación de la Función de Potencial

- Captura la estructura: nodos más altos contribuyen más al potencial.
- `extract-min` libera suficiente potencial al eliminar la raíz.
- `insert` añade potencial gradualmente.
- Se mantiene la correlación entre potencial y "costo estructural" del heap.

---

## Conclusión

La función de potencial:

$$
\Phi(H) = \sum_{i=1}^{n} \log_2(\text{altura del nodo } i + 1)
$$

permite demostrar que:

- **INSERT**: $C_a = \mathcal{O}(\log_2 n)$
- **EXTRACT-MIN**: $C_a = \mathcal{O}(1)$

Esto se logra porque `extract-min` libera suficiente potencial acumulado (al eliminar la raíz del heap) para compensar su costo real de $\mathcal{O}(\log_2 n)$.
