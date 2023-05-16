# Read User Input

fuel_type = input()
fuel_qty = float(input())
club_card = input()

gasoline_price = 2.22
diesel_price = 2.33
gas_price = 0.93
total_discount = 0
# Logic

if club_card == 'Yes':
    gasoline_price = 2.04
    diesel_price = 2.21
    gas_price = 0.85

if 20 <= fuel_qty <= 25:
    total_discount = 0.08
elif fuel_qty > 25:
    total_discount = 0.1

if fuel_type == 'Gas':
    total_price = (fuel_qty * gas_price) - ((fuel_qty * gas_price) * total_discount)
elif fuel_type == 'Gasoline':
    total_price = (fuel_qty * gasoline_price) - ((fuel_qty * gasoline_price) * total_discount)
elif fuel_type == 'Diesel':
    total_price = (fuel_qty * diesel_price) - ((fuel_qty * diesel_price) * total_discount)

# Output

print(f'{total_price:.2f} lv.')
