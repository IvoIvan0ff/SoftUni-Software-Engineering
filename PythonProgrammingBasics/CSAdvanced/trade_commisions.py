town = input()
sales = float(input())
result = ''

if town == 'Sofia':
    if 0 <= sales <= 500:
        result = sales * 0.05
        print(f'{result:.2f}')
    elif 500 < sales <= 1000:
        result = sales * 0.07
        print(f'{result:.2f}')
    elif 1000 < sales <= 10000:
        result = sales * 0.08
        print(f'{result:.2f}')
    elif sales > 10000:
        result = sales * 0.12
        print(f'{result:.2f}')
    else:
        result = 'error'
        print(result)
elif town == 'Varna':
    if 0 <= sales <= 500:
        result = sales * 0.045
        print(f'{result:.2f}')
    elif 500 < sales <= 1000:
        result = sales * 0.075
        print(f'{result:.2f}')
    elif 1000 < sales <= 10000:
        result = sales * 0.1
        print(f'{result:.2f}')
    elif sales > 10000:
        result = sales * 0.13
        print(f'{result:.2f}')
    else:
        result = 'error'
        print(result)
elif town == 'Plovdiv':
    if 0 <= sales <= 500:
        result = sales * 0.055
        print(f'{result:.2f}')
    elif 500 < sales <= 1000:
        result = sales * 0.08
        print(f'{result:.2f}')
    elif 1000 < sales <= 10000:
        result = sales * 0.12
        print(f'{result:.2f}')
    elif sales > 10000:
        result = sales * 0.145
        print(f'{result:.2f}')
    else:
        result = 'error'
        print(result)
else:
    result = 'error'
    print(result)


