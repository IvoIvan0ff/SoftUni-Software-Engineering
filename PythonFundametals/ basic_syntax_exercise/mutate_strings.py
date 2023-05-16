string1 = input()
string2 = input()
last_printed_string = string1
new_string = ""
for i in range(len(string1)):
    left_side = string2[:i + 1]
    right_side = string1[i + 1:]
    new_string = left_side + right_side
    if new_string == last_printed_string:
        continue
    print(new_string)
    last_printed_string = new_string
