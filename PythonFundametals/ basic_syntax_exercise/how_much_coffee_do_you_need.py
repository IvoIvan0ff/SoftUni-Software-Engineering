coffee_counter = 0
is_greater = False
while True:
    user_input = input()
    if user_input == 'END':
        break

    if user_input == 'coding':
        coffee_counter += 1
    elif user_input == 'dog':
        coffee_counter += 1
    elif user_input == 'cat':
        coffee_counter += 1
    elif user_input == 'movie':
        coffee_counter += 1

    if user_input == 'CODING':
        coffee_counter += 2
    elif user_input == 'DOG':
        coffee_counter += 2
    elif user_input == 'CAT':
        coffee_counter += 2
    elif user_input == 'MOVIE':
        coffee_counter += 2

    if coffee_counter > 5:
        print('You need extra sleep')
        is_greater = True
        break
if not is_greater:
    print(coffee_counter)
