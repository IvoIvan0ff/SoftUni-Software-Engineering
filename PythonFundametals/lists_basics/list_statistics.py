n = int(input())
positives = []
negatives = []
positives_sum = 0
negatives_sum = 0

for i in range(n):
    number = int(input())
    if number >= 0:
        positives.append(number)
        positives_sum += 1
    elif number < 0:
        negatives.append(number)
        negatives_sum += number
print(positives)
print(negatives)

print(f"Count of positives: {positives_sum}")
print(f'Sum of negatives: {negatives_sum}')
