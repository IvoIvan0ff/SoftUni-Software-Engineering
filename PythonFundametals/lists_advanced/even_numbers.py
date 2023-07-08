numbers_as_string = input().split(', ')

numbers_as_int = [int(x) for x in numbers_as_string]

even_number = [numbers_as_int.index(i) for i in numbers_as_int if i % 2 == 0]

print(even_number)
