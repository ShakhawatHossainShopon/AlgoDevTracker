entry_price = 100.0
shares = 10

def calculate_pnl(price):
    return (price - entry_price) * shares

prices = [90.0, 95.0, 100.0, 105.0, 110.0]

print("=" * 40)
print("FUNCTION & GRAPH COORDINATES")
print("=" * 40)
print("Entry Price: $", entry_price)
print("Shares Owned: ", shares)
print("-" * 40)
print("Input (x: Price)  -->  Output (y: PnL)")
print("-" * 40)

for p in prices:
    pnl = calculate_pnl(p)
    print(f"x = ${p:<6.1f}  -->  y = ${pnl:>+6.1f}")

print("=" * 40)
