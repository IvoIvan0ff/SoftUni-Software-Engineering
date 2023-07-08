strings = input().split()
searched_word = input()

palindromes = []

for word in strings:
    if word == "".join(reversed(word)):
        palindromes.append(word)

print(palindromes)
print(f"Found palindrome {palindromes.count(searched_word)} times")
