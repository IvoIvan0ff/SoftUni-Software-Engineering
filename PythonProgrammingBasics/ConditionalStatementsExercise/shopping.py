budget = float(input())
gpu_qty = int(input())
cpu_qty = int(input())
ram_qty = int(input())

gpu_price = 250
gpu_total_price = gpu_price * gpu_qty
cpu_price = gpu_total_price * 0.35
ram_price = gpu_total_price * 0.1
cpu_total_price = cpu_price * cpu_qty
ram_total_price = ram_price * ram_qty
total_price = gpu_total_price + cpu_total_price + ram_total_price
if gpu_qty > cpu_qty:
    total_price -= total_price * 0.15
leftover = abs(budget - total_price)

if total_price <= budget:
    print(f"You have {leftover:.2f} leva left!")
else:
    print(f"Not enough money! You need {leftover:.2f} leva more!")
