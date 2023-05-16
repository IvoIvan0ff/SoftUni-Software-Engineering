sea_qty = int(input())
mountain_qty = int(input())
all_packages = sea_qty + mountain_qty
profit = 0

while True:
    package_name = input()
    if package_name == 'Stop':
        break
    if package_name == 'sea' and sea_qty != 0:
        profit += 680
        sea_qty -= 1
        all_packages -= 1
    elif package_name == 'mountain' and mountain_qty != 0:
        profit += 499
        mountain_qty -= 1
        all_packages -= 1
    if all_packages == 0:
        print(f'Good job! Everything is sold.')
        break

print(f'Profit: {profit} leva.')

