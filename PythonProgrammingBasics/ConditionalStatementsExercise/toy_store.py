trip_price = float(input())
puzzle_qty = int(input())
doll_qty = int(input())
bears_qty = int(input())
minions_qty = int(input())
trucks_qty = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minions_price = 8.20
truck_price = 2
discount = 0.25
rent = 0.1

total_puzzle_price = puzzle_price * puzzle_qty
total_doll_price = doll_price * doll_qty
total_bears_price = bear_price * bears_qty
total_minions_price = minions_qty * minions_price
total_trucks_price = truck_price * trucks_qty

total_qty = puzzle_qty + doll_qty + bears_qty + minions_qty + trucks_qty
total_price = total_puzzle_price + total_doll_price + total_bears_price + total_minions_price + total_trucks_price

if total_qty >= 50:
    total_price -= total_price * discount
rental_price = total_price * rent
profit = total_price - rental_price

if profit >= trip_price:
    print(f"Yes! {profit  - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - profit:.2f} lv needed.")
