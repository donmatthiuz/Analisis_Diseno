def largestCross(matriz):
    n = len(matriz)

    
    left = [[0]*n for _ in range(n)]
    right = [[0]*n for _ in range(n)]
    top = [[0]*n for _ in range(n)]
    bottom = [[0]*n for _ in range(n)]

    
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                left[i][j] = (left[i][j-1] if j > 0 else 0) + 1
                top[i][j] = (top[i-1][j] if i > 0 else 0) + 1

    # Llenar right y bottom
    for i in range(n-1, -1, -1):
        for j in range(n-1, -1, -1):
            if matriz[i][j] == 1:
                right[i][j] = (right[i][j+1] if j < n-1 else 0) + 1
                bottom[i][j] = (bottom[i+1][j] if i < n-1 else 0) + 1

    # Encontrar la cruz más grande
    max_cross = 0
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 1:
                size = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                if size >=2:
                  max_cross = max(max_cross, 4 * (size - 1) + 1)  # cada brazo más el centro

    return max_cross

# Ejemplo de uso:
matriz_17 = [
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 1 , 1 ] ,
[ 1 , 0 , 1 , 0 , 1 , 1 , 1 , 0 , 1 , 1 ] ,
[ 1 , 1 , 1 , 0 , 1 , 1 , 0 , 1 , 0 , 1 ] ,
[ 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 ] ,
[ 1 , 1 , 1 , 0 , 1 , 1 , 1 , 1 , 1 , 1 ] ,
[ 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 0 ] ,
[ 1 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 1 ] ,
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 1 , 1 ] ,
[ 1 , 1 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 1 ] ,
[ 1 , 0 , 1 , 1 , 1 , 1 , 0 , 1 , 0 , 0 ]
]


matriz_0 = [
[ 1 , 1 , 1 , 1 , 1 , 1 ] ,
[ 1 , 0 , 1 , 1 , 0 , 1 ] ,
[ 0 , 1 , 1 , 0 , 0 , 1 ] ,
[ 1 , 1 , 1 , 1 , 1 , 1 ] ,
[ 1 , 0 , 0 , 1 , 0 , 1 ] ,
[ 1 , 0 , 1 , 1 , 0 , 0 ]
]
print(largestCross(matriz_17))  # Debería imprimir 17
