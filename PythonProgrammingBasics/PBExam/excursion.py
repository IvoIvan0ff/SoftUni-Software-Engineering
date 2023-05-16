ppl_qty = int(input())
nights_qty = int(input())
cards_qty = int(input())
tickets_qty = int(input())

nights_per_person = nights_qty * 20
cards_total = cards_qty * 1.6
tickets_total = tickets_qty * 6
nights_total = ppl_qty * nights_per_person

total_sum_person = nights_per_person + cards_total + tickets_total
total_sum = total_sum_person * ppl_qty
total_sum += total_sum * 0.25


print(f'{total_sum:.2f}')
