money_needed = float(input())
balance = float(input())
days = 0
spend_qty = 0

while True:
    action = input()
    action_money = float(input())
    if action == 'spend':
        days += 1
        spend_qty += 1
        balance -= action_money
        if balance < 0:
            balance = 0
    elif action == 'save':
        days += 1
        balance += action_money
    if spend_qty  == 5:
        print("You can't save the money.")
        print(f'{spend_qty}')
        break
    if balance >= money_needed:
        print(f'You saved the money for {days} days.')
        break
