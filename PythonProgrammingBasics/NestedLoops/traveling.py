while True:
    destination = input()
    if destination == 'End':
        break
    price = float(input())
    current_savings = 0

    while current_savings < price:
        current_savings += float(input())

    print(f'Going to {destination}!')

