def add_and_subtract(first_num, second_num, third_num):
    def sum_numbers():
        return first_num + second_num

    def subtract():
        return (first_num + second_num) - third_num

    return (first_num + second_num) - third_num


num1 = int(input())
num2 = int(input())
num3 = int(input())

print(add_and_subtract(num1, num2, num3))
