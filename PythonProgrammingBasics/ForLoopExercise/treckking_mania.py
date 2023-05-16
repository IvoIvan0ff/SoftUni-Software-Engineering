group_qty = int(input())
total_ppl = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(group_qty):
    ppl_in_group = int(input())
    total_ppl += ppl_in_group
    if ppl_in_group <= 5:
        p1 += ppl_in_group
    elif 6 <= ppl_in_group <= 12:
        p2 += ppl_in_group
    elif 13 <= ppl_in_group <= 25:
        p3 += ppl_in_group
    elif 26 <= ppl_in_group <= 40:
        p4 += ppl_in_group
    else:
        p5 += ppl_in_group

p1_percentage = p1 / total_ppl * 100
p2_percentage = p2 / total_ppl * 100
p3_percentage = p3 / total_ppl * 100
p4_percentage = p4 / total_ppl * 100
p5_percentage = p5 / total_ppl * 100

print(f'{p1_percentage:.2f}%')
print(f'{p2_percentage:.2f}%')
print(f'{p3_percentage:.2f}%')
print(f'{p4_percentage:.2f}%')
print(f'{p5_percentage:.2f}%')
