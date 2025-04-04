import math as mt


monedas = []
tabla = []
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
    global num, monedas, columnas, filas, tabla

    num = int(input("Ingresa un número: "))
    monedas = list(map(int, input("Ingresa las denominaciones de monedas separadas por comas: ").split(",")))

    columnas = [i for i in range(num + 1)]
    filas = ["Moneda " + str(m) for m in monedas]


    tabla = [[INFINITO] * (num + 1) for _ in range(len(monedas))]
    
    for i in range(len(monedas)):
        tabla[i][0] = 0

def solution():
    global num, monedas, tabla
    for i in range(len(monedas)):
        for j in range(1, num + 1):
            xi = monedas[i]

            if xi > j:
                elegido = INFINITO
                if i > 0:
                    elegido = tabla[i-1][j]
                
                tabla[i][j] = elegido
            else:
                elegido_actual = INFINITO
                elegido_antes = INFINITO
                devolver = INFINITO

                if i>0:
                    elegido_antes = tabla[i-1][j]

                if tabla[i][j - xi] != INFINITO:
                    elegido_actual = tabla[i][j - xi] + 1

                moneda_1 = elegido_antes
                moneda_2 = elegido_actual

                if moneda_1 > moneda_2:
                    devolver = moneda_2
                elif moneda_2 > moneda_1:
                    devolver = moneda_1
                tabla[i][j] = devolver

if __name__ == "__main__":
    build_table()
    solution()
    print_table()
