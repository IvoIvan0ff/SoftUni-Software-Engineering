students = 0
standard = 0
kids = 0
total_qty = 0
is_over = False

while True:
    movie_name = input()
    free_seats = int(input())
    if movie_name == 'Finish':
        break
    counter = 0
    while True:
        ticket_type = input()
        if ticket_type == 'Finish':
            is_over = True
            break
        if ticket_type == 'End' or counter >= free_seats:
            break
        counter += 1
        total_qty += 1
        if ticket_type == 'student':
            students += 1
        elif ticket_type == 'standard':
            standard += 1
        else:
            kids += 1

    hall_percentage = counter / free_seats * 100
    print(f'{movie_name} - {hall_percentage:.2f}% full.')
    if is_over:
        break
students_percentage = students / total_qty * 100
standard_percentage = standard / total_qty * 100
kids_percentage = kids / total_qty * 100

print(f"Total tickets: {total_qty}")
print(f"{students_percentage:.2f}% student tickets.")
print(f"{standard_percentage:.2f}% standard tickets.")
print(f"{kids_percentage:.2f}% kids tickets.")

