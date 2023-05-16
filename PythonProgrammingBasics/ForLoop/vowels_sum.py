n = input()
result = 0


for i in range(0, len(n)):
    char = n[i]
    if char == 'a':
        result += 1
    elif char == 'e':
        result += 2
    elif char == 'i':
        result += 3
    elif char == 'o':
        result += 4
    elif char == 'u':
        result += 5
print(result)
