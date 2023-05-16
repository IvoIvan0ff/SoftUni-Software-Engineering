number = int(input())

for n in range(number):
    number2 = int(input())
    if number2 % 2 != 0:
        print(f"{number2} is odd!")
        break
else:
    print("All numbers are even.")
