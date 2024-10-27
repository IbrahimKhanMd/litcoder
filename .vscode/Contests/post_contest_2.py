from itertools import product

def get_valid_combinations(budget, stocks):
    valid_combinations = []
    for quantities in product(range(6), repeat=len(stocks)):
        total_price = sum(q * price for q, (_, price) in zip(quantities, stocks))
        if total_price == budget:
            valid_combinations.append(quantities)
    return valid_combinations

def main():
    try:
        # Get the budget and number of stocks directly from user input
        budget = int(input())
        if budget <= 0:
            print("Invalid Input")
            return
        
        n = int(input())
        stocks = []
        
        # Loop through the provided stock information
        for _ in range(n):
            stock_input = input().split()
            name = " ".join(stock_input[:-1])
            try:
                price = int(stock_input[-1])
                if price <= 0:
                    print("The stock prices should be at least greater than 0")
                    return
                elif price > budget:
                    print("One of the stock prices is higher than the target price")
                    return
                stocks.append((name, price))
            except ValueError:
                print("Invalid Input")
                return

        valid_combinations = get_valid_combinations(budget, stocks)

        if valid_combinations:
            for combination in valid_combinations:
                print("".join(map(str, combination)))
            print(len(valid_combinations))
        else:
            print(0)
    
    except ValueError:
        print("Invalid Input")

main()