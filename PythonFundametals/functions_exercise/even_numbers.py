def even_number(number):
    if number % 2 == 0:
        return True
    return False


number_list_as_str = input().split()
number_list_as_int = []
for each in number_list_as_str:
    number_list_as_int.append(int(each))

filtered = list(filter(even_number, number_list_as_int))
print(filtered)
