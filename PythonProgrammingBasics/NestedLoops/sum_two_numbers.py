start_num = int(input())
end_num = int(input())
magic_num = int(input())
counter = 0
is_found = False

for i in range(start_num, end_num + 1):
    for j in range(start_num, end_num + 1):
        counter += 1
        if i + j == magic_num:
            is_found = True
            print(f'Combination N:{counter} ({i} + {j} = {magic_num})')
            break
    if is_found:
        break
else:
    print(f'{counter} combinations - neither equals {magic_num}')
    