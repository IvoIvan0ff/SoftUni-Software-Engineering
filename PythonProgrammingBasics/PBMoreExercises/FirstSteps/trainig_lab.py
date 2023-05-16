duljina = float(input())
shirochina = float(input())    # широчина

without_hall = shirochina - 1
desk_in_row = without_hall // 0.7
rows = duljina // 1.2
all_desk = (desk_in_row) * (rows)
possible_desk = all_desk - 3

print(possible_desk)

