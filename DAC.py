import time
import csv
import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import Polynomial
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Algoritmo DAC 
def coin_change_dac(coins, S):
    if S == 0:
        return 0, []
    if S < 0:
        return float('inf'), []
    
    min_coins = float('inf')
    best_combination = []
    for coin in coins:
        result, combination = coin_change_dac(coins, S - coin)
        if result != float('inf') and result + 1 < min_coins:
            min_coins = result + 1
            best_combination = combination + [coin]
    
    return min_coins, best_combination

# Análisis de rendimiento con regresiones
def analyze_dac_runtime():
    coins = [1, 5, 10, 12, 25, 50]
    
    S_values = list(range(5, 66, 5)) 
    times = []
    
    print("Midiendo tiempos de ejecución para cada valor de S...")
    print("S\tTiempo (segundos)")
    print("-" * 25)
    
    # Medir tiempos de ejecución
    for S in S_values:
        start_time = time.time()
        coin_change_dac(coins, S)
        end_time = time.time()
        elapsed = end_time - start_time
        times.append(elapsed)
        print(f"{S}\t{elapsed:.6f}")
    
    # Guardar resultados en CSV
    with open("coin_change_dac_times.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["S", "Time (seconds)"])
        for S, t in zip(S_values, times):
            writer.writerow([S, t])
    
    print("\nCalculando regresiones...")
    
    # Preparamos los datos para la regresión exponencial
    X = np.array(S_values).reshape(-1, 1)
    y = np.array(times)
    
    # 3. Ajuste de regresión exponencial
    # Filtramos los valores no positivos para logaritmos
    positive_indices = [i for i, t in enumerate(times) if t > 0]
    S_values_exp = [S_values[i] for i in positive_indices]
    times_exp = [times[i] for i in positive_indices]
    
    if len(times_exp) > 0:
        log_times = np.log(times_exp)
        X_exp = np.array(S_values_exp).reshape(-1, 1)
        exp_reg = LinearRegression()
        exp_reg.fit(X_exp, log_times)
        
        # Parámetros de la regresión exponencial
        a = np.exp(exp_reg.intercept_)
        b = exp_reg.coef_[0]
        
        # Predicciones para todos los valores originales
        y_exp_pred = [a * np.exp(b * x) for x in S_values]
        
        # Calcular R² solo para los valores positivos
        log_pred = exp_reg.predict(X_exp)
        y_exp_pred_positive = [np.exp(p) for p in log_pred]
        r2_exp = r2_score(times_exp, y_exp_pred_positive)
    else:
        a, b, r2_exp = 0, 0, 0
        y_exp_pred = [0] * len(S_values)
    
    # Graficar solo regresión exponencial
    plt.figure(figsize=(12, 8))
    
    plt.scatter(S_values, times, color="blue", label="Datos reales")
    plt.plot(S_values, y_exp_pred, color="purple", label="Regresión exponencial")
    
    # Añadir ecuación y R² al gráfico
    equation_text = f"y = {a:.4f} · e^({b:.4f}x)"
    r2_text = f"R² = {r2_exp:.4f}"
    plt.annotate(equation_text + "\n" + r2_text, 
                xy=(0.05, 0.95), 
                xycoords='axes fraction',
                bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=0.8),
                fontsize=12)
    
    plt.xlabel("S")
    plt.ylabel("Tiempo (segundos)")
    plt.title("Tiempo de ejecución vs. S para algoritmo DAC (Regresión exponencial)")
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig("coin_change_dac_regressions.png")
    plt.show()
    
    # Imprimir resultados de las regresiones
    print("\nResultados de las regresiones:")
    print("-" * 50)
    
    
    # Regresión exponencial
    if len(times_exp) > 0:
        print(f"\n3. Regresión exponencial (y = a * e^(bx)):")
        print(f"   a = {a:.6f}")
        print(f"   b = {b:.6f}")
        print(f"   R² = {r2_exp:.6f}")
    


# Ejecutar el análisis
if __name__ == "__main__":
    print("Analizando rendimiento del algoritmo DAC para el problema de cambio de monedas...")
    analyze_dac_runtime()
    print("\nAnálisis completado.")


