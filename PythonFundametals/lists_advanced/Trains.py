def add(people):
    wagons_list[-1] += people
    return wagons_list


def insert(index, people):
    wagons_list[index] += people
    return wagons_list


def leave(index, people):
    wagons_list[index] -= people
    return wagons_list


wagons = int(input())
wagons_list = []
for i in range(wagons):
    wagons_list.append(0)

while True:
    command = input()
    if command == 'End':
        break
    current_command = command.split()
    action = current_command[0]
    if action == 'add':
        people_joining = int(current_command[1])
        add(people_joining)
    if action == 'insert':
        current_index = int(current_command[1])
        people_joining = int(current_command[2])
        insert(current_index, people_joining)
    if action == 'leave':
        current_index = int(current_command[1])
        people_joining = int(current_command[2])
        leave(current_index, people_joining)

print(wagons_list)
