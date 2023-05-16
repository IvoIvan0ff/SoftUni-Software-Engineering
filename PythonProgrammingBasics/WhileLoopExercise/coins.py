coins = 0
user_input = float(input())

while user_input - 2 >= 0:
    user_input -= 2
    user_input = round(user_input, 2)
    coins += 1
while user_input - 1 >= 0:
    user_input -= 1
    user_input = round(user_input, 2)
    coins += 1
while user_input - 0.5 >= 0:
    user_input -= 0.5
    user_input = round(user_input, 2)
    coins += 1
while user_input - 0.2 >= 0:
    user_input -= 0.2
    user_input = round(user_input, 2)
    coins += 1
while user_input - 0.1 >= 0:
    user_input -= 0.1
    user_input = round(user_input, 2)
    coins += 1
while user_input - 0.05 >= 0:
    user_input -= 0.05
    user_input = round(user_input, 2)
    coins += 1
while user_input - 0.02 >= 0:
    user_input -= 0.02
    user_input = round(user_input, 2)
    coins += 1
while user_input - 0.01 >= 0:
    user_input -= 0.01
    user_input = round(user_input, 2)
    coins += 1
print(coins)

