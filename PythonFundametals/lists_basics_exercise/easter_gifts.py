gifts = input().split()

while True:
    command = input()
    if command == 'No Money':
        break
    command_list = command.split()
    current_command = command_list[0]
    current_gift = command_list[1]
    if current_command == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == current_gift:
                gifts[i] = "None"
    elif current_command == "Required":
        index = int(command_list[2])
        if 0 <= index < len(gifts):
            gifts[index] = current_gift
    else:
        gifts[-1] = current_gift

for gift in gifts:
    if gift == 'None':
        gifts.remove('None')

print(" ".join(gifts))
