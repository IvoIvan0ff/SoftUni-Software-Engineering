inheritance = float(input())
age = int(input())
ivancho_age = 18
money_spent_even = 0
money_spent_odd = 0

for i in range(1800, age + 1):
    if i % 2 == 0:
        inheritance -= 12000
    else:
        inheritance -= 12000 + ivancho_age * 50
    ivancho_age += 1

if inheritance >= 0:
    print(f'Yes! He will live a carefree life and will have {inheritance:.2f} dollars left.')
else:
    print(f'He will need {abs(inheritance):.2f} dollars to survive.')
