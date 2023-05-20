user_input = int(input())
tank_capacity = 255
liters_in_tank = 0

for i in range(user_input):
    liters_of_water = int(input())
    if (tank_capacity - liters_of_water) >= 0:
        tank_capacity -= liters_of_water
        liters_in_tank += liters_of_water
    else:
        print("Insufficient capacity!")
        continue
print(liters_in_tank)
