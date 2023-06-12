numbers = input().split()
removable_numbers = int(input())
numbers_as_int = []
final_list = []
for element in numbers:
    numbers_as_int.append(int(element))
for index in range(removable_numbers):
    numbers_as_int.remove(min(numbers_as_int))
for current_element in numbers_as_int:
    final_list.append(str(current_element))
print(", ".join(final_list))
