n = int(input())
p1, p2, p3, p4, p5, p6 = 0, 0, 0, 0, 0, 0
points = 0

for i in range(n):
    user_input = int(input())
    if user_input <= 9 and user_input >= 0:
        points += user_input * 0.2
        p1 += 1
    elif 10 <= user_input <= 19:
        points += user_input * 0.3
        p2 += 1
    elif 20 <= user_input <= 29:
        points += user_input * 0.4
        p3 += 1
    elif 30 <= user_input <= 39:
        points += 50
        p4 += 1
    elif 40 <= user_input <= 50:
        points += 100
        p5 += 1
    elif user_input < 0 or user_input > 50:
        points /= 2
        p6 += 1

p1_percentage = p1 / n * 100
p2_percentage = p2 / n * 100
p3_percentage = p3 / n * 100
p4_percentage = p4 / n * 100
p5_percentage = p5 / n * 100
p6_percentage = p6 / n * 100

print(f'{points:.2f}')
print(f'From 0 to 9: {p1_percentage:.2f}%')
print(f'From 10 to 19: {p2_percentage:.2f}%')
print(f'From 20 to 29: {p3_percentage:.2f}%')
print(f'From 30 to 39: {p4_percentage:.2f}%')
print(f'From 40 to 50: {p5_percentage:.2f}%')
print(f'Invalid numbers: {p6_percentage:.2f}%')
