faro_list = input().split()
count_of_shuffles = int(input())

for count_of_shuffles in range(count_of_shuffles):
    final_deck = []
    half_list = len(faro_list) // 2
    right_part = faro_list[half_list:]
    left_part = faro_list[:half_list]
    for index in range(len(right_part)):
        final_deck.append(left_part[index])
        final_deck.append(right_part[index])
    faro_list = final_deck
print(final_deck)
