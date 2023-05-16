prime_sum = 0
non_prime_sum = 0

while True:
    user_num = input()
    if user_num == 'stop':
        break
    user_num = int(user_num)
    if user_num < 0:
        print("Number is negative.")
        continue
    count = 0
    for i in range(1, user_num + 1):
        if user_num % i == 0:
            count += 1
    if count == 2:
        prime_sum += user_num
    else:
        non_prime_sum += user_num


print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {non_prime_sum}')
