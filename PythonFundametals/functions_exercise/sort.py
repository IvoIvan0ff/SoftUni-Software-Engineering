numbers_as_str = input().split()
numbers_as_int = []
for i in numbers_as_str:
    numbers_as_int.append(int(i))
numbers_as_int.sort()
print(numbers_as_int)
