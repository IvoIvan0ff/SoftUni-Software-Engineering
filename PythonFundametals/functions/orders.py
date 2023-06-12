def orders(product, quantity):

    if product == 'coffee':
        total_price = quantity * 1.5
    elif product == 'water':
        total_price = quantity * 1
    elif product == 'coke':
        total_price = quantity * 1.4
    else:
        total_price = quantity * 2

    return total_price


item = input()
qty = int(input())

total = orders(item, qty)
print(f'{total:.2f}')
