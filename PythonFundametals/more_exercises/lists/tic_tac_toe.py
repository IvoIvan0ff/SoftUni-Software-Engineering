first_line = input().split()
second_line = input().split()
third_line = input().split()
for i in range(len(first_line)):
    if (first_line[0] == second_line[0] and second_line[0] == third_line[0]) and first_line[0] == '1':
        print("First player won")
    if (first_line[1] == second_line[1] and second_line[1] == third_line[1]) and first_line[0] == '1':
        print("First player won")
    if (first_line[2] == second_line[2] and second_line[2] == third_line[2]) and first_line[0] == '1':
        print("First player won")
