def main():
    # Pedir un número al usuario
    num = int(input("Ingresa un número: "))
    
    # Pedir diferentes monedas
    monedas = input("Ingresa las denominaciones de monedas separadas por comas: ")
    monedas = [int(m) for m in monedas.split(",")]
    
    # Crear la tabla
    columnas = [i for i in range(num + 1)]  # Números de 0 a num
    filas = ["Moneda " + str(m) for m in monedas]  # Etiquetas de fila con monedas
    
    # Generar la tabla manualmente
    tabla = [[0] * (num + 1) for _ in range(len(monedas))]
    
    # Imprimir la tabla
    print("\nTabla generada:")
    print("\t" + "\t".join(map(str, columnas)))
    for i, fila in enumerate(filas):
        print(fila + "\t" + "\t".join(map(str, tabla[i])))

if __name__ == "__main__":
    main()
