tabs_qty = int(input())
salary = int(input())

for i in range(tabs_qty):
    user_input = input()
    if user_input == 'Facebook':
        salary -= 150
    elif user_input == 'Instagram':
        salary -= 100
    elif user_input == 'Reddit':
        salary -= 50

if salary <= 0:
    print('You have lost your salary.')
else:
    print(salary)
    