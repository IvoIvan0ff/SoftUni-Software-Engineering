
for i in range(1000):
    num = float(input())
    if num < 0:
        print('Negative number!')
        break
    num = num * 2
    print(f'Result: {num:.2f}')
