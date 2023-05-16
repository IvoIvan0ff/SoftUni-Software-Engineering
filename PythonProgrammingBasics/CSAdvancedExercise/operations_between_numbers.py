num1 = int(input())
num2 = int(input())
operator = input()

if operator == '+' or operator == '-' or operator == '*':
    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2

    if result % 2 == 0:
        type_number = 'even'
    else:
        type_number = 'odd'
    print(f'{num1} {operator} {num2} = {result} - {type_number}')

elif operator == '/' and num2 != 0:
    print(f'{num1} / {num2} = {(num1 / num2):.2f}')
elif operator == '%' and num2 != 0:
    print(f'{num1} % {num2} = {(num1 % num2)}')
if num2 == 0:
    print(f'Cannot divide {num1} by zero')
