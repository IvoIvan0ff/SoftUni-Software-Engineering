budget = float(input())
ppl_qty = int(input())
ppl_clothing = float(input())

decoration = budget * 0.1

if ppl_qty > 150:
    ppl_clothing -= ppl_clothing * 0.1

total_sum = decoration + ppl_clothing * ppl_qty

if total_sum > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {abs(total_sum - budget):.2f} leva more.')
else:
    print('Action!')
    print(f'Wingard starts filming with {abs(total_sum - budget):.2f} leva left.')
