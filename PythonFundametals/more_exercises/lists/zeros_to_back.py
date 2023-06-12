user_list = input().split(', ')

for j in range(len(user_list) - 1, -1, -1):
    numbers = int(user_list[j])
    user_list.pop(j)
    user_list.insert(j, numbers)
for i in range(len(user_list) - 1, -1, -1):
    if user_list[i] == 0:
        numbers = int(user_list[i])
        user_list.pop(i)
        user_list.append(numbers)
print(user_list)
