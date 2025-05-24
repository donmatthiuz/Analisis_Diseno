# Problema 5: Función de Potencial y Costos Amortizados

Tenemos una función de potencial $\Phi$ tal que $\Phi(D_i) \geq \Phi(D_0)$ para todo $i$, pero $\Phi(D_0) \neq 0$. Debemos definir una función $\Phi'$ tal que:
- $\Phi'(D_0) = 0$
- $\Phi'(D_i) \geq \Phi'(D_0)$ para todo $i \geq 1$
- Los costos amortizados obtenidos con $\Phi'$ sean los mismos que con $\Phi$

### Definición de la nueva función de potencial

Si definimos $\Phi'$ como:

$$\Phi'(D_i) = \Phi(D_i) - \Phi(D_0)$$

1. Condición inicial: $$\Phi'(D_0) = \Phi(D_0) - \Phi(D_0) = 0 \quad \checkmark$$

2. Condición de no negatividad: Para todo $i \geq 1$:
$$\Phi'(D_i) = \Phi(D_i) - \Phi(D_0)$$

Como sabemos que $\Phi(D_i) \geq \Phi(D_0)$ para todo $i$, entonces:
$$\Phi(D_i) - \Phi(D_0) \geq 0$$

Por lo tanto: $\Phi'(D_i) \geq 0 = \Phi'(D_0)$ para todo $i \geq 1$ $\quad \checkmark$

3. Equivalencia de costos amortizados:

El costo amortizado de la operación $i$ usando $\Phi$ es:
$$\hat{c_i} = c_i + \Phi(D_i) - \Phi(D_{i-1})$$

El costo amortizado de la operación $i$ usando $\Phi'$ es:
$$\hat{c_i'} = c_i + \Phi'(D_i) - \Phi'(D_{i-1})$$

Sustituyendo la definición de $\Phi'$:
$$\hat{c_i'} = c_i + [\Phi(D_i) - \Phi(D_0)] - [\Phi(D_{i-1}) - \Phi(D_0)]$$

$$\hat{c_i'} = c_i + \Phi(D_i) - \Phi(D_0) - \Phi(D_{i-1}) + \Phi(D_0)$$

$$\hat{c_i'} = c_i + \Phi(D_i) - \Phi(D_{i-1}) = \hat{c_i}$$

La función $\Phi'(D_i) = \Phi(D_i) - \Phi(D_0)$ satisface todas las condiciones requeridas y proporciona una función de potencial normalizada que es equivalente a la original para el análisis de costos amortizados.
