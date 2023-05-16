bottles_qty = int(input())
detergent_qty = bottles_qty * 750

plates = 0
pots = 0
m1_lef = False
dishes_ = input()
dishwashing = 0

while dishes_ != 'End':
    dishes = int(dishes_)
    dishwashing += 1
    if dishwashing % 3 != 0:
        plates += dishes
        detergent_qty -= dishes * 5
    else:
        pots += dishes
        detergent_qty -= dishes * 15
    if detergent_qty <= 0:
        m1_lef = True
        break
    dishes_ = input()

if m1_lef:
    print(f'Not enough detergent, {abs(detergent_qty)} ml. more necessary!')

else:
    print("Detergent was enough!")
    print(f'{plates} dishes and {pots} pots were washed.')
    print(f'Leftover detergent {detergent_qty} ml.')
