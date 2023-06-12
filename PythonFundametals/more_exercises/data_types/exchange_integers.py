a = int(input())
b = int(input())

a_temp = a
b_temp = b

a = b_temp
b = a_temp

print(f'Before:\na = {a_temp}\nb = {b_temp}\nAfter:\na = {a}\nb = {b}')
