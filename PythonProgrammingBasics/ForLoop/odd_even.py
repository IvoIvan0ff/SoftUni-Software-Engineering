n = int(input())
total_sum_odd = 0
total_sum_even = 0
for i in range(n):
    user_input = int(input())
    if i % 2 == 0:
        total_sum_even += user_input
    else:
        total_sum_odd += user_input
if total_sum_even == total_sum_odd:
    print('Yes')
    print(f'Sum = {total_sum_odd}')
else:
    print('No')
    print(f'Diff = {abs(total_sum_odd - total_sum_even)}')
