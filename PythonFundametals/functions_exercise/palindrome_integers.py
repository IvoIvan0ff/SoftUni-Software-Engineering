def is_palindrome(numbers):
    for i in numbers:
        if i == i[::-1]:
            print(True)
        else:
            print(False)


user_input = input().split(", ")
is_palindrome(user_input)
