fire = input().split('#')
water = int(input())
effort = 0
total_fire = 0
print("Cells:")
for i in fire:
    status = i.split(' = ')
    current_status = status[0]
    water_needed = int(status[1])
    if current_status == 'High' and (81 <= water_needed <= 125) and water_needed <= water:
        water -= water_needed
        effort += water_needed * 0.25
        total_fire += water_needed
        print(f'- {water_needed}')
    elif current_status == 'Medium' and (51 <= water_needed <= 80) and water_needed <= water:
        water -= water_needed
        effort += water_needed * 0.25
        total_fire += water_needed
        print(f'- {water_needed}')
    elif current_status == 'Low' and (1 <= water_needed <= 50) and water_needed <= water:
        water -= water_needed
        effort += water_needed * 0.25
        total_fire += water_needed
        print(f'- {water_needed}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
