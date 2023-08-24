def calculate_profit_percentage(selling_price, cost_price):
    return ((selling_price - cost_price) * 100) / cost_price

def calculate_leveraged_profit(profit, leverage):
    return profit * leverage

def calculate_average_price(currencies, prices):
    total_investment = sum(currencies[i] * prices[i] for i in range(len(currencies)))
    total_currencies = sum(currencies)
    return total_investment / total_currencies

def calculate_dca(periods, closing_prices):
    total_inverse_prices = sum(1 / price for price in closing_prices)
    return periods / total_inverse_prices

print("Welcome to the Dollar Cost Averaging Calculator!")

choice = input("What do you want to calculate?\n1. Profit Percentage and Leveraged Profit\n2. Average Price\n3. Dollar Cost Averaging\n")

if choice == "1":
    selling_price = float(input("Enter selling price: "))
    cost_price = float(input("Enter cost price: "))
    leverage = float(input("Enter leverage: "))
    
    profit = calculate_profit_percentage(selling_price, cost_price)
    leveraged_profit = calculate_leveraged_profit(profit, leverage)
    
    print("Profit Percentage:", profit)
    print("Leveraged Profit:", leveraged_profit)

elif choice == "2":
    num_currencies = int(input("Enter the number of currencies: "))
    
    currencies = []
    prices = []
    
    for _ in range(num_currencies):
        currency = float(input("Enter number of currencies: "))
        price = float(input("Enter price: "))
        currencies.append(currency)
        prices.append(price)
    
    avg_price = calculate_average_price(currencies, prices)
    total_investment = sum(currencies[i] * prices[i] for i in range(len(currencies)))
    
    print("Total Invested Amount:", total_investment)
    print("Average Price:", avg_price)

elif choice == "3":
    num_periods = int(input("Enter number of periods: "))
    
    closing_prices = []
    
    for _ in range(num_periods):
        price = float(input("Enter closing price: "))
        closing_prices.append(price)
    
    dca = calculate_dca(num_periods, closing_prices)
    
    print("Dollar Cost Averaging:", dca)

print("Thank you for using the Dollar Cost Averaging Calculator!")
