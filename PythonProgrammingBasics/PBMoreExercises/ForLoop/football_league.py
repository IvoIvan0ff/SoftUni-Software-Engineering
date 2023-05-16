stadium_qty = int(input())
fans_qty = int(input())
p1, p2, p3, p4 = 0, 0, 0, 0

for i in range(fans_qty):
    user_input = input()
    if user_input == 'A':
        p1 += 1
    elif user_input == 'B':
        p2 += 1
    elif user_input == 'V':
        p3 += 1
    elif user_input == 'G':
        p4 += 1

p1_percentage = p1 / fans_qty * 100
p2_percentage = p2 / fans_qty * 100
p3_percentage = p3 / fans_qty * 100
p4_percentage = p4 / fans_qty * 100
capacity_percent = fans_qty / stadium_qty * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{capacity_percent:.2f}%')
