entry_price = 100.0
shares = 10

def calculate_pnl(current_price):
    return (current_price - entry_price) * shares

test_price_1 = 110.0
test_price_2 = 90.0

print("Entry Price: $", entry_price)
print("Shares Owned:", shares)
print("PnL at $ 110.0: $", calculate_pnl(test_price_1))
print("PnL at $ 90.0: $", calculate_pnl(test_price_2))
