lilly_age = int(input())
washing_price = float(input())
toy_price = int(input())

toys_qty = 0
savings = 0
money_for_bd = 10

for i in range(1, lilly_age + 1):
    if i % 2 == 0:
        savings += money_for_bd - 1
        money_for_bd += 10
    else:
        toys_qty += 1
money_from_toys = toys_qty * toy_price
total_money = savings + money_from_toys

if total_money >= washing_price:
    print(f'Yes! {abs(total_money - washing_price):.2f}')
else:
    print(f'No! {abs(total_money - washing_price):.2f}')
    