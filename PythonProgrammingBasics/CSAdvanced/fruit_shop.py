fruit = input()
day = input()
qty = float(input())
result = 'error'

if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or\
        day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        result = qty * 2.5
        print(f'{result:.2f}')
    elif fruit == 'apple':
        result = qty * 1.2
        print(f'{result:.2f}')
    elif fruit == 'orange':
        result = qty * 0.85
        print(f'{result:.2f}')
    elif fruit == 'grapefruit':
        result = qty * 1.45
        print(f'{result:.2f}')
    elif fruit == 'kiwi':
        result = qty * 2.7
        print(f'{result:.2f}')
    elif fruit == 'pineapple':
        result = qty * 5.5
        print(f'{result:.2f}')
    elif fruit == 'grapes':
        result = qty * 3.85
        print(f'{result:.2f}')
    else:
        print(result)
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        result = qty * 2.7
        print(f'{result:.2f}')
    elif fruit == 'apple':
        result = qty * 1.25
        print(f'{result:.2f}')
    elif fruit == 'orange':
        result = qty * 0.9
        print(f'{result:.2f}')
    elif fruit == 'grapefruit':
        result = qty * 1.6
        print(f'{result:.2f}')
    elif fruit == 'kiwi':
        result = qty * 3
        print(f'{result:.2f}')
    elif fruit == 'pineapple':
        result = qty * 5.6
        print(f'{result:.2f}')
    elif fruit == 'grapes':
        result = qty * 4.2
        print(f'{result:.2f}')
    else:
        print(result)
else:
    print(result)
