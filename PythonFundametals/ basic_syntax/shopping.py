budget = int(input())

while True:
    prices = input()
    if prices == 'End':
        print("You bought everything needed.")
        break
    prices = int(prices)
    budget -= prices
    if budget < 0:
        print('You went in overdraft!')
        break
