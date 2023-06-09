events = input().split('|')
total_energy = 100
total_coins = 100
is_factory_open = True

for i in events:
    event = i.split('-')
    type_of_event = event[0]
    event_value = int(event[1])
    if type_of_event == 'rest':
        current_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")
    elif type_of_event == 'order':
        if total_energy >= 30:
            total_coins += event_value
            total_energy -= 30
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            is_factory_open = False
            break
if is_factory_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
