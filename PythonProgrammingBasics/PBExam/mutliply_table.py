n = int(input())

for i in range(1, int(str(n)[2]) + 1):
    for j in range(1, int(str(n)[1]) + 1):
        for k in range(1, int(str(n)[0]) + 1):
            print(f'{i} * {j} * {k} = {i * j * k};')
