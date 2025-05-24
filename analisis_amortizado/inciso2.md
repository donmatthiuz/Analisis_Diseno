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