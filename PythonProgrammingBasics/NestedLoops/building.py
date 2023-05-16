floor = int(input())
room = int(input())

for i in range(floor, 0, -1):
    for j in range(0, room):
        if i == floor:
            print(f'L{i}{j}', end=' ')
        if i % 2 == 0 and i != floor:
            print(f'O{i}{j}', end=' ')
        if i % 2 != 0 and i != floor:
            print(f'A{i}{j}', end=' ')
    print()
