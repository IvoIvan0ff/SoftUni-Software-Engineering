travel_list = input().split('||')
starting_fuel = int(input())
ammo_qty = int(input())
light_years_qty = 0
for each in travel_list:
    command = each.split()
    current_command = command[0]
    current_number = 0
    if len(command) > 1:
        current_number = int(command[1])
    if current_command == 'Travel':
        if starting_fuel >= current_number:
            starting_fuel -= current_number
            print(f"The spaceship travelled {current_number} light-years.")
        else:
            print("Mission failed.")
            break
    elif current_command == 'Enemy':
        if ammo_qty >= current_number:
            ammo_qty -= current_number
            print(f"An enemy with {current_number} armour is defeated.")
        elif starting_fuel >= current_number * 2:
            starting_fuel -= current_number * 2
            print(f"An enemy with {current_number} armour is outmaneuvered.")
        else:
            print("Mission failed.")
            break
    elif current_command == 'Repair':
        starting_fuel += current_number
        ammo_qty += current_number * 2
        print(f"Ammunitions added: {current_number * 2}.")
        print(f"Fuel added: {current_number}.")
    else:
        print("You have reached Titan, all passengers are safe.")

