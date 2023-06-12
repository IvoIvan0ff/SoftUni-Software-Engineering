number = int(input())
magic_word = input()
example_list = []
filtered_list = []

for i in range(number):
    user_input = input()
    example_list.append(user_input)
    if magic_word in user_input:
        filtered_list.append(user_input)

print(example_list)
print(filtered_list)
    