def odd_even_sum(integer):
    odd_sum = 0
    even_sum = 0
    for index in integer:
        single_number = int(index)
        if single_number % 2 == 0:
            even_sum += single_number
        elif single_number % 2 != 0:
            odd_sum += single_number

    return odd_sum, even_sum


current_number = input()
sum_of_odd_digits, sum_of_even_digits = odd_even_sum(current_number)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
