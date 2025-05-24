# Respuestas a las Preguntas

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

---

## 2. Pila con _multipop_ y _multipush_

### ¿Se mantiene el costo amortizado `O(1)` por operación?
**Sí**, bajo las siguientes condiciones:  
1. **Costo real de _multipush(k, A)_**: `k` (equivalente a `k` operaciones _push_ individuales).  
2. **Método del potencial**:  
   - **Función potencial**: `Φ = número de elementos en la pila`.  
   - **Cálculo de costos amortizados**:  
     - **_push_**:  
       - Costo real: `1`.  
       - Cambio en potencial: `+1`.  
       - Costo amortizado: `1 + 1 = 2`.  
     - **_multipush(k)_**:  
       - Costo real: `k`.  
       - Cambio en potencial: `+k`.  
       - Costo amortizado: `k + k = 2k`.  
     - **_multipop(k)_**:  
       - Costo real: `min(k, tamaño_pila)`.  
       - Cambio en potencial: `-k`.  
       - Costo amortizado: `0` (usando créditos almacenados).  

### Invariante clave
Cada elemento añadido "prepaga" un crédito para su eventual eliminación. Esto garantiza que:  
- Los créditos acumulados en _push/multipush_ cubren los costos de futuros _pop/multipop_.  
- El costo amortizado por operación (individual o múltiple) sigue siendo `O(1)`.  

---