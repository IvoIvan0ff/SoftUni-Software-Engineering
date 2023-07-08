phones_list = input().split(', ')

while True:
    commands = input()
    if commands == 'End':
        break
    commands_list = commands.split(' - ')
    current_command = commands_list[0]
    phone = ''
    old_phone = ''
    new_phone = ''
    if current_command == 'Bonus phone':
        bonus_phone_list = commands_list[1].split(':')
        old_phone = bonus_phone_list[0]
        new_phone = bonus_phone_list[1]
    else:
        phone = commands_list[1]
    if current_command == 'Add':
        if phone not in phones_list:
            phones_list.append(phone)
    elif current_command == 'Remove':
        if phone in phones_list:
            phones_list.remove(phone)
    elif current_command == 'Bonus phone':
        if old_phone in phones_list:
            index = phones_list.index(old_phone)
            phones_list.insert(index + 1, new_phone)
    elif current_command == 'Last':
        if phone in phones_list:
            phones_list.remove(phone)
            phones_list.append(phone)
print(", ".join(phones_list))
