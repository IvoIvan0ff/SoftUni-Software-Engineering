factor = int(input())
count = int(input())
i = 1
example_list = []

while len(example_list) < count:
    if i % factor == 0:
        example_list.append(i)
    i += 1

print(example_list)

