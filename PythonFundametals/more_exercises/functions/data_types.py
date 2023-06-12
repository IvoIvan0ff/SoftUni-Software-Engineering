def data_types(string, number):
    if string == 'int':
        number_as_int = int(number)
        number_as_int *= 2
        print(number_as_int)
    elif string == 'real':
        number_as_int = int(number)
        number_as_int *= 1.5
        print(f'{number_as_int:.2f}')
    else:
        print(f'${number}$')


first_input = input()
second_input = input()
data_types(first_input, second_input)
