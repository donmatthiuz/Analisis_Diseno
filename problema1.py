def count_nokia_combinations(n):
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    

    vecinos = {}
    rows, cols = len(keypad), len(keypad[0])
    for i in range(rows):
        for j in range(cols):
            key = keypad[i][j]
            if key.isdigit():
                vecinos[key] = [key]
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols and keypad[ni][nj].isdigit():
                        vecinos[key].append(keypad[ni][nj])
    
    valores_calculados = {}
    
    def algoritmo_solucion(digit, length):
        if (digit, length) in valores_calculados:
            return valores_calculados[(digit, length)]
        
        if length == 1:
            return 1
        
        count = 0
        for siguiente_digito in vecinos[digit]:
            count += algoritmo_solucion(siguiente_digito, length - 1)
        
        valores_calculados[(digit, length)] = count
        return count
    
    total_combinations = 0
    for digit in '0123456789':
        total_combinations += algoritmo_solucion(digit, n)
    
    return total_combinations


n = 2
result = count_nokia_combinations(n)
print(f"El numero de combinaciones para n={n} el resultado es: {result}")


n = 10
result = count_nokia_combinations(n)
print(f"El numero de combinaciones para n={n} el resultado es: {result}")
