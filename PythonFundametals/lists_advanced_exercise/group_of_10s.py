numbers = input().split(', ')
numbers_as_int = [int(i) for i in numbers]
current_group = 10

while numbers_as_int:
    current_group_list = [i for i in numbers_as_int if i <= current_group]
    for i in range(len(numbers_as_int) -1, -1, -1):
        if numbers_as_int[i] in current_group_list:
            del numbers_as_int[i]

    print(f"Group of {current_group}'s: {current_group_list}")
    current_group += 10
    current_group_list = []
    