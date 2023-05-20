user_input = int(input())

while True:
    user_input += 1
    year_length = len(str(user_input))
    double_digits = len(set(str(user_input)))
    if year_length == double_digits:
        print(user_input)
        break
    else:
        continue
