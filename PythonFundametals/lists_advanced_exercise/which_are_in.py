first_sequence = input().split(', ')
second_sequence = input().split(', ')
final_list = []

for word in first_sequence:
    for el in second_sequence:
        if word in el:
            final_list.append(word)
            break

print(final_list)
