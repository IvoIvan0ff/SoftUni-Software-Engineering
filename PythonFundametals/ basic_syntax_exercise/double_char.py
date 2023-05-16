while True:
    user_input = input()
    if user_input == 'End':
        break
    if user_input == 'SoftUni':
        continue
    new_string = ''
    for i in user_input:
        new_string += i * 2
    print(new_string)


