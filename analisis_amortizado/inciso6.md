# Inciso 6

Un *min-heap* binario es un árbol binario completo (todos sus niveles están llenos y sus hojas se llenan de izquierda a derecha) en donde cada nodo es menor que todos sus hijos. El *min-heap* tiene una operación de inserción llamada *insert*, pero consideremos además la función *extract-min*, que reemplaza la raíz por el último nodo del árbol y luego la intercambia con el menor de sus hijos. Supongamos que ambas operaciones tienen un tiempo de ejecución real $O(\log\_2 n)$. Provea una función de potencial según la cual el costo amortizado de *insert* sea $O(\log\_2 n)$ y el de *extract-min* sea $O(1)$. No olvide que el potencial siempre debe ser positivo (no necesariamente el cambio de potencial), y que el potencial inicial es idealmente cero. Demuestre que su función de potencial funciona.

*Hint:* primero considere la forma que tendrá el costo real de cada operación. Con esto en mente, escriba la fórmula de costo amortizado, usando valores en el cambio de potencial de forma que al sumarlo con el costo real se obtengan los costos amortizados deseados (claramente en uno de los casos el cambio de potencial debe resultar menor a $O(\log n)$; y en el otro caso debe ser negativo). ¿Qué característica(s) de un árbol binario completo se miden con un $\log\_2 \blacksquare$? ¿Cómo cambia(n) esta(s) característica(s) luego de un *insert* o un *extract-min*? Recuerde que el potencial debe extraerse de alguna propiedad *de la estructura de datos*.

## Función de Potencial Propuesta

Para un min-heap binario completo con n elementos, definimos la función de potencial:

**Φ(H) = Σᵢ₌₁ⁿ log₂(altura del nodo i + 1)**

Donde la altura de un nodo es la distancia máxima desde ese nodo hasta una hoja.

### Propiedades de la Función de Potencial

1. **Φ(H) ≥ 0**: Siempre positiva ya que log₂(altura + 1) ≥ 0 para cualquier nodo
2. **Φ(∅) = 0**: Un heap vacío tiene potencial cero
3. **Extrae información estructural**: El potencial refleja qué tan "desbalanceado" está el árbol

## Análisis de las Operaciones

### Operación INSERT

**Costo real**: O(log₂ n) - en el peor caso burbujea hasta la raíz

**Cambio de potencial**:
- Se añade un nuevo nodo como hoja (altura 0): +log₂(1) = 0
- Los nodos en el camino desde la nueva hoja hasta la raíz pueden cambiar su contribución al potencial
- En el peor caso, el cambio total es O(log₂ n)

**Costo amortizado**:
Cₐ(insert) = Cᵣ(insert) + ΔΦ = O(log₂ n) + O(log₂ n) = O(log₂ n)

### Operación EXTRACT-MIN

**Costo real**: O(log₂ n) - reemplaza raíz con última hoja y hace heapify-down

**Cambio de potencial**:
- Se elimina la raíz (altura h = ⌊log₂ n⌋): -log₂(h + 1) = -log₂(⌊log₂ n⌋ + 1)
- El último elemento se mueve a la raíz y burbujea hacia abajo
- La reducción del potencial por eliminar la raíz es significativa: -Ω(log log n)

**Costo amortizado**:
Cₐ(extract-min) = Cᵣ(extract-min) + ΔΦ = O(log₂ n) - Ω(log log n) = O(1)

## Demostración Formal

### Características del Árbol Binario Completo

En un árbol binario completo de n nodos:
- Altura total: h = ⌊log₂ n⌋
- Número de nodos en el nivel i: 2ⁱ (para i = 0, 1, ..., h-1)
- Altura de un nodo en el nivel i: h - i

### Cálculo del Potencial Total

Φ(H) = Σᵢ₌₀ʰ⁻¹ 2ⁱ · log₂(h - i + 1)

### Análisis del Extract-Min

Cuando extraemos el mínimo:

1. **Eliminación de la raíz**: 
   - Reducción: -log₂(h + 1) = -log₂(⌊log₂ n⌋ + 1)
   - Esta reducción es Ω(log log n)

2. **Reorganización**:
   - El costo de heapify-down es O(log₂ n)
   - Los cambios locales en el potencial son menores

3. **Balance final**:
   - Cₐ = O(log₂ n) - Ω(log log n) = O(1)

## Validación de la Función de Potencial

La función propuesta funciona porque:

1. **Captura la estructura**: Nodos más altos contribuyen más al potencial
2. **Extract-min libera potencial significativo**: Al eliminar la raíz (nodo de mayor altura)
3. **Insert añade potencial gradualmente**: Nuevas hojas tienen contribución mínima
4. **Mantiene invariantes**: El potencial siempre refleja el "costo estructural" del heap

## Conclusión

La función de potencial Φ(H) = Σᵢ₌₁ⁿ log₂(altura del nodo i + 1) demuestra que:

- **Insert**: Costo amortizado O(log₂ n)
- **Extract-min**: Costo amortizado O(1)

Esto se logra porque extract-min libera suficiente potencial (al eliminar el nodo de mayor altura) para compensar su costo real de O(log₂ n).
