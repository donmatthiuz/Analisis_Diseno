import math as mt

monedas = []
tabla = []
usadas = []
INFINITO = mt.inf
num = 0
columnas = []
filas = []

def print_table():
    global num, monedas, columnas, filas, tabla
    print("\nTabla:")
    print("\t" + "\t".join(map(str, columnas)))
    for i, fila in enumerate(filas):
        valores = ["∞" if tabla[i][j] == INFINITO else str(tabla[i][j]) for j in range(num + 1)]
        print(fila + "\t" + "\t".join(valores))

def build_table():
    global num, monedas, columnas, filas, tabla, usadas

    num = int(input("Ingresa un número: "))
    monedas = list(map(int, input("Ingresa las denominaciones de monedas separadas por comas: ").split(",")))

    columnas = [i for i in range(num + 1)]
    filas = ["Moneda " + str(m) for m in monedas]

    tabla = [[INFINITO] * (num + 1) for _ in range(len(monedas))]
    usadas = [[False] * (num + 1) for _ in range(len(monedas))]

    for i in range(len(monedas)):
        tabla[i][0] = 0

def solution():
    global num, monedas, tabla, usadas
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

def reconstruir_solucion():
    global num, monedas, tabla, usadas

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

if __name__ == "__main__":
    build_table()
    solution()
    print_table()

    resultado = reconstruir_solucion()
    print("\nDistribución de monedas utilizadas:")
    for i, cantidad in enumerate(resultado):
        print(f"Moneda {monedas[i]}: {cantidad}")
