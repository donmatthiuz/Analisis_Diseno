def count_nokia_combinations(n):

    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    

    vecinos = {
        '0': ['0','8'],  
        '1': ['1','2', '4'],
        '2': ['2','1', '3', '5'], 
        '3': ['3', '2', '6'],
        '4': ['4','1', '5', '7'],
        '5': ['5','2', '4', '6', '8'],
        '6': ['6','3', '5', '9'],
        '7': ['7','4', '8'],
        '8': ['8','5', '7', '9', '0'],
        '9': ['9','6', '8']
       
    }
    
    memo = {}
    
    def dp(digit, length):
        if (digit, length) in memo:
            return memo[(digit, length)]
        
        if length == 1:
            return 1
        
        count = 0
        for next_digit in vecinos[digit]:
            count += dp(next_digit, length - 1)
        
        # Store result in memoization table
        memo[(digit, length)] = count
        return count
    
   
    total_combinations = 0
    for digit in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        total_combinations += dp(digit, n)
    
    return total_combinations

def main():
   
    n = 2
    result = count_nokia_combinations(n)
    print(f"Number of possible combinations for n={n}: {result}")
    
   

if __name__ == "__main__":
    main()