n = int(input())
left_sum = 0
right_sum = 0

for i in range(0, n):
    user_input = int(input())
    left_sum += user_input
for i in range(0, n):
    user_input = int(input())
    right_sum += user_input
if left_sum == right_sum:
    print(f'Yes, sum = {right_sum}')
else:
    print(f'No, diff = {abs(right_sum - left_sum)}')

