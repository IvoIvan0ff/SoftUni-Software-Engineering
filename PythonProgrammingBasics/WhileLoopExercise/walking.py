steps_total = 0

while True:
    steps = input()
    if steps == 'Going home':
        steps2 = int(input())
        steps_total += steps2
        break
    steps = int(steps)
    steps_total += steps
    if steps_total >= 10000:
        break

if steps_total >= 10000:
    print('Goal reached! Good job!')
    print(f'{abs(steps_total - 10000)} steps over the goal!')
else:
    print(f'{abs(steps_total - 10000)} more steps to reach goal.')


