numbers = [int(i) for i in input().split(', ')]

positive = [str(j) for j in numbers if j >= 0]
negative = [str(k) for k in numbers if k < 0]
even = [str(s) for s in numbers if s % 2 == 0]
odd = [str(x) for x in numbers if x % 2 != 0]

print(f'Positive: {", ".join(positive)}')
print(f'Negative: {", ".join(negative)}')
print(f'Even: {", ".join(even)}')
print(f'Odd: {", ".join(odd)}')
