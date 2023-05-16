voucher = int(input())
ticket_qty = 0
others = 0


while True:
    purchase = input()
    if purchase == 'End':
        break

    if len(purchase) > 8:
        first_sum = (ord(purchase[0]))
        second_sum = (ord(purchase[1]))
        total_sum = first_sum + second_sum
        if voucher >= total_sum:
            ticket_qty += 1

    else:
        total_sum = ord(purchase[0])
        if voucher >= total_sum:
            others += 1

    if total_sum <= voucher:
        voucher -= total_sum
        total_sum = 0

    else:
        break

print(f'{ticket_qty}')
print(f'{others}')

