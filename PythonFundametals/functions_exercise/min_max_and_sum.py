number_as_str = input().split()
number_as_int = []
for number in number_as_str:
    number_as_int.append(int(number))

print(f"The minimum number is {min(number_as_int)}")
print(f"The maximum number is {max(number_as_int)}")
print(f"The sum number is: {sum(number_as_int)}")
