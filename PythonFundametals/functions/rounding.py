numbers = input().split()
numbers_as_float = []
rounded_numbers = []
for each in numbers:
    numbers_as_float.append(float(each))

for element in numbers_as_float:
    rounded_numbers.append(round(element))

print(rounded_numbers)
