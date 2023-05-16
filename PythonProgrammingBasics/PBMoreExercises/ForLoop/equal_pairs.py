n = int(input())
num1 = int(input())
num2 = int(input())

number_sum = num1 + num2

diff = 0
max_diff = 0

for i in range(n - 1):
    num1 = int(input())
    num2 = int(input())
    current_sum = num1 + num2

    if current_sum != number_sum:
        diff = abs(current_sum - number_sum)
        number_sum = current_sum
    if diff > max_diff:
        max_diff = diff
if diff == 0:
    print(f'Yes, value={number_sum}')
else:
    print(f'No, maxdiff={max_diff}')
