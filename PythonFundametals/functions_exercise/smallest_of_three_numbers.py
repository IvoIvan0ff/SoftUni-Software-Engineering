def smallest_number(first_num, second_num, third_num):

    if first_num < second_num and first_num < third_num:
        min_number = first_num
    elif second_num < first_num and second_num < third_num:
        min_number = second_num
    else:
        min_number = third_num

    return min_number


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(smallest_number(num1, num2, num3))
