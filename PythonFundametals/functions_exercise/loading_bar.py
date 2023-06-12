def loaded_percentage(number):
    if number == 100:
        return '100% Complete!\n[%%%%%%%%%%]'
    elif number < 100:
        loaded = number // 10
        return f'{number}% [{"%" * loaded}{"." * (10 - loaded)}]\nStill loading...'


percentage = int(input())
print(loaded_percentage(percentage))
