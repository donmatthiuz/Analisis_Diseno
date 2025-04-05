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

print(coin_change_dac([1,25, 75], 100))