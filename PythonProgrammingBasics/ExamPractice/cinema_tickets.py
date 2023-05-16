student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets = 0
current_movie = ''
movie_name = input()

while movie_name != 'Finish':
    available_seats = int(input())
    taken_seats = 0

    while True:
        bought_ticket = input()
        current_movie = movie_name

        if bought_ticket == 'student':
            student_tickets += 1
        elif bought_ticket == 'standard':
            standard_tickets += 1
        elif bought_ticket == 'kid':
            kids_tickets += 1
        elif bought_ticket == 'End':
            print(f"{current_movie} - {(taken_seats / available_seats * 100):.2f}% full.")
            break

        total_tickets += 1
        taken_seats += 1

        if taken_seats >= available_seats:
            print(f"{current_movie} - {(taken_seats / available_seats * 100):.2f}% full.")
            break

    movie_name = input()

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets * 100):.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets * 100):.2f}% standard tickets.")
print(f"{(kids_tickets / total_tickets * 100):.2f}% kids tickets.")
