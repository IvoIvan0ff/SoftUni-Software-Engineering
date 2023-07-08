user_input = input()
char_list = ['a', 'o', 'u', 'e', 'i']
new_string = [char for char in user_input if char.lower() not in char_list]

print("".join(new_string))



