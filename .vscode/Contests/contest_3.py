def two_candy_sum(total_amount, candy_prices):
    indexed_prices = list(enumerate(candy_prices, start=1))  # Keep original indices
    indexed_prices.sort(key=lambda x: x[1])  # Sort by price

    left = 0
    right = len(indexed_prices) - 1
    
    while left < right:
        current_sum = indexed_prices[left][1] + indexed_prices[right][1]
        
        if current_sum == total_amount:
            return (indexed_prices[left][0], indexed_prices[right][0])
        elif current_sum < total_amount:
            left += 1
        else:
            right -= 1
    
    return (-1, -1)

total_amount = int(input())
candy_prices = [int(price) for price in input().split()]

result = two_candy_sum(total_amount, candy_prices)
print(result[0], result[1])