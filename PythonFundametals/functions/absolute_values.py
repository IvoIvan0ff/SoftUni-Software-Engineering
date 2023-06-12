numbers = input().split()
abs_numbers = []
for each in numbers:
    abs_numbers.append(abs(float(each)))

print(abs_numbers)