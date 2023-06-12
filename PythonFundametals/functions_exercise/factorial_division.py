def factorial_first(first_number):
    first_total = first_number
    for i in range(1, first_number):
        first_total *= i
    return first_total


def factorial_second(second_number):
    second_total = second_number
    for i in range(1, second_number):
        second_total *= i
    return second_total


first_num = int(input())
second_num = int(input())
first_total = factorial_first(first_num)
second_total = factorial_second(second_num)

total_output = first_total / second_total
print(f'{total_output:.2f}')
