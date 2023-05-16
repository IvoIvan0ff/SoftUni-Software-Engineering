year_tax = int(input())

shoes = year_tax - (year_tax * 0.4)
suit = shoes - (shoes * 0.2)
ball = suit * 0.25
accesories = ball * 0.2

total_sum = shoes + suit + ball + accesories + year_tax
print(total_sum)
