daily_money = float(input())
money_earned_daily = float(input())
money_spent = float(input())
present_price = float(input())

daily_money_save = 5 * daily_money
total_earned = 5 * money_earned_daily
total_save = daily_money_save + total_earned
total_sum = total_save - money_spent

if total_sum > present_price:
    print(f'Profit: {total_sum:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {abs(total_sum - present_price):.2f} BGN.')
