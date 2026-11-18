balance = 10000
max_risk = 100
buy_price = 100
stop_loss = 95
take_profit = 112

loss_per_share = buy_price - stop_loss
shares_to_buy = max_risk / loss_per_share

profit_per_share = take_profit - buy_price
reward_risk_ratio = profit_per_share / loss_per_share
is_trade_approved = reward_risk_ratio >= 2.0

position_value = shares_to_buy * buy_price
margin_rate = 0.10
required_margin = position_value * margin_rate
is_account_safe = balance >= required_margin

print("Account Balance: $", balance)
print("Max Loss Allowed: $", max_risk)
print("Loss Per Share: $", loss_per_share)
print("Shares to Buy:", shares_to_buy)
print("-" * 40)
print("Potential Profit Per Share: $", profit_per_share)
print("Reward-to-Risk Ratio:", reward_risk_ratio)
print("Is Trade Approved (RR >= 2.0)?", is_trade_approved)
print("-" * 40)
print("Total Position Value: $", position_value)
print("Required Margin (10%): $", required_margin)
print("Is Account Safe (Balance >= Margin)?", is_account_safe)
