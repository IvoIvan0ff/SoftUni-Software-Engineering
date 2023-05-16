students_qty = int(input())
average_grade = 0
p1, p2, p3, p4 = 0, 0, 0, 0

for i in range(students_qty):
    user_input = float(input())
    if user_input >= 5:
        p1 += 1
        average_grade += user_input
    elif 4.00 <= user_input <= 4.99:
        p2 += 1
        average_grade += user_input
    elif 3 <= user_input <= 3.99:
        p3 += 1
        average_grade += user_input
    elif user_input < 3:
        p4 += 1
        average_grade += user_input

p1_percentage = p1 / students_qty * 100
p2_percentage = p2 / students_qty * 100
p3_percentage = p3 / students_qty * 100
p4_percentage = p4 / students_qty * 100
average_grade /= students_qty

print(f'Top students: {p1_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {p2_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {p3_percentage:.2f}%')
print(f'Fail: {p4_percentage:.2f}%')
print(f'Average: {average_grade:.2f}')
