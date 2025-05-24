## 1. Contador binario con operaciones _Increment_ y _Decrement_

### Worst-case scenario realista
Una secuencia alternada de operaciones _Increment_ y _Decrement_ que maximicen los cambios de bits.  
**Ejemplo concreto**:  
Alternar entre valores binarios con todos los bits en 1 y todos en 0 (e.g., `0111...1` ↔ `1000...0`).  
- Cada operación requiere voltear **hasta `k` bits** (no necesariamente todos, pero en este ejemplo sí).  

### Cota superior del tiempo de ejecución
- **Costo por operación**: `O(k)` (volteo de hasta `k` bits).  
- **Para `n` operaciones**: `O(nk)`.  

### Explicación detallada
- **Análisis tradicional (solo _Increment_)**:  
  Costo amortizado de `O(1)` por operación, ya que cada bit se voltea ≤ 1 vez en promedio.  
- **Con _Decrement_**:  
  Los bits pueden cambiar repetidamente (1 → 0 → 1...), invalidando el análisis amortizado clásico.  
- **Caso realista**:  
  En el ejemplo propuesto, cada operación altera `k` bits, resultando en `O(nk)` operaciones totales.  