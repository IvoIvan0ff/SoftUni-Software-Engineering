def perfect_number(user_number):
    sum = 0
    for i in range(1, user_number):
        if user_number % i == 0:
            sum += i
    if user_number == sum:
        return "We have a perfect number!"
    return "It's not so perfect."


user_number = int(input())
print(perfect_number(user_number))
