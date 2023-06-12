def calculations(operator, first_num, second_num):
    result = 0
    if operator == 'multiply':
        result = first_num * second_num
    elif operator == 'divide':
        result = first_num // second_num
    elif operator == 'add':
        result = first_num + second_num
    elif operator == 'subtract':
        result = first_num - second_num

    return result

command = input()
number1 = int(input())
number2 = int(input())

print(calculations(command, number1, number2))
