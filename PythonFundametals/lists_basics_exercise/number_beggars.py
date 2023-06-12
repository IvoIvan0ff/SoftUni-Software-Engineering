money_for_beggars = input().split(', ')
beggars_qty = int(input())
money_as_number = []

for element in money_for_beggars:
    money_as_number.append(int(element))
starting_index = 0
final_sum = []
while starting_index < beggars_qty:
    sum_for_current_beggar = 0
    for current_index in range(starting_index, len(money_as_number), beggars_qty):
        sum_for_current_beggar += money_as_number[current_index]
    final_sum.append(sum_for_current_beggar)
    starting_index += 1
print(final_sum)
