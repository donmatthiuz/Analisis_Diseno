def coin_change_dnc(coins, S, memo=None):
    if memo is None:
        memo = {}  # Diccionario para memoización
    
    # Caso base: Si el cambio es 0, se necesitan 0 monedas
    if S == 0:
        return 0, []
    # Si el cambio es negativo, no es posible dar cambio
    if S < 0:
        return float('inf'), []


    min_coins = float('inf')
    best_combination = []

    # Intentamos todas las monedas disponibles
    for coin in coins:
        result, combination = coin_change_dnc(coins, S - coin, memo)
        if result != float('inf') and result + 1 < min_coins:
            min_coins = result + 1
            best_combination = combination + [coin]  # Agregamos la moneda usada

    memo[S] = (min_coins, best_combination)  # Guardamos en memoización
    return memo[S]

# Prueba
coins = [2,3]  # Denominaciones de monedas
S = 6  # Cambio requerido
min_count, used_coins = coin_change_dnc(coins, S)
print(f"Número mínimo de monedas: {min_count}")  
print(f"Monedas usadas: {used_coins}")  

