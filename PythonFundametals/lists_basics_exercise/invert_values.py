numbers = input().split()
inverted_numbers = []

for element in numbers:
    current_number = -int(element)
    inverted_numbers.append(current_number)
print(inverted_numbers)
