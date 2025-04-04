import math as mt
INFINITO = mt.inf
import time
import pandas as pd

def print_table(num, monedas, columnas, filas, tabla):
    print("\nTabla:")
    print("\t" + "\t".join(map(str, columnas)))
    for i, fila in enumerate(filas):
        valores = ["∞" if tabla[i][j] == INFINITO else str(tabla[i][j]) for j in range(num + 1)]
        print(fila + "\t" + "\t".join(valores))

def build_table(num, monedas, columnas, filas, tabla, usadas):

    columnas = [i for i in range(num + 1)]
    filas = ["Moneda " + str(m) for m in monedas]

    tabla = [[INFINITO] * (num + 1) for _ in range(len(monedas))]
    usadas = [[False] * (num + 1) for _ in range(len(monedas))]

    for i in range(len(monedas)):
        tabla[i][0] = 0
    
    return num, monedas, columnas, filas, tabla, usadas

def solution(num, monedas, tabla, usadas):
    for i in range(len(monedas)):
        for j in range(1, num + 1):
            xi = monedas[i]

            if xi > j:
                if i > 0:
                    tabla[i][j] = tabla[i - 1][j]
            else:
                sin_usar = tabla[i - 1][j] if i > 0 else INFINITO
                con_usar = tabla[i][j - xi] + 1 if tabla[i][j - xi] != INFINITO else INFINITO

                if con_usar < sin_usar:
                    tabla[i][j] = con_usar
                    usadas[i][j] = True
                else:
                    tabla[i][j] = sin_usar
    return num, monedas, tabla, usadas

def reconstruir_solucion(num, monedas, tabla, usadas):

    resultado = [0] * len(monedas)
    i = len(monedas) - 1
    j = num

    while j > 0 and i >= 0:
        if usadas[i][j]:
            resultado[i] += 1
            j -= monedas[i]
        else:
            i -= 1

    return resultado

def show_result(resultado,monedas):
    print("\nDistribución de monedas utilizadas:")
    for i, cantidad in enumerate(resultado):
        print(f"Moneda {monedas[i]}: {cantidad}")






def analisis_empirico():
    monedas = [1, 5, 10, 12, 25, 50]
    cambios = list(range(10, 301, 5))

    tiempos = []  
    resultados = [] 

    for cambio in cambios:
        start_time = time.time()

        tabla = []
        usadas = []
        num = cambio
        columnas = []
        filas = []
        

        num, monedas, columnas, filas, tabla, usadas = build_table(num, monedas, columnas, filas, tabla, usadas)
        num, monedas, tabla, usadas = solution(num, monedas, tabla, usadas)
        resultado = reconstruir_solucion(num, monedas, tabla, usadas)
        
        end_time = time.time()  
        runtime = end_time - start_time 

        tiempos.append(runtime) 
        resultados.append(resultado) 

        print(f"\nResultado final para el cambio: {cambio}")
        show_result(resultado, monedas)

    df = pd.DataFrame({
    'Cambio': cambios,
    'Tiempo de Ejecucion (segundos)': tiempos
    })

    
    df.to_excel("resultados_cambio_tiempo.xlsx", index=False)
    print("Archivo Excel guardado como 'resultados_cambio_tiempo.xlsx'")
    
    




if __name__ == "__main__":
    analisis_empirico()
    # monedas = []
    # tabla = []
    # usadas = []
    # num = 0
    # columnas = []
    # filas = []

    # num = int(input("Ingresa un número: "))
    # monedas = list(map(int, input("Ingresa las denominaciones de monedas separadas por comas: ").split(",")))

    # num, monedas, columnas, filas, tabla, usadas = build_table(num, monedas, columnas, filas, tabla, usadas)
    # num, monedas, tabla, usadas = solution(num, monedas, tabla, usadas)
    # print_table(num, monedas, columnas, filas, tabla)

    # resultado = reconstruir_solucion(num, monedas, tabla, usadas)

    # show_result(resultado,monedas)
    



