import sys

n = int(input())
max_number = -sys.maxsize
total_sum = 0

for i in range(n):
    user_input = int(input())
    total_sum += user_input
    if user_input > max_number:
        max_number = user_input
total_sum = total_sum - max_number

if total_sum == max_number:
    print('Yes')
    print(f'Sum = {total_sum}')
else:
    print('No')
    print(f'Diff = {abs(total_sum - max_number)}')
