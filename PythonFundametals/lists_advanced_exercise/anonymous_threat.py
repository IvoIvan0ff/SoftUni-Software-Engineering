initial_list = input().split("!")
while True:
    command = input()

    if command == "Go Shopping!":
        break

    current_command = command.split()
    action = current_command[0]
    item = current_command[1]

    if action == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)

    elif action == "Unnecessary":
        if item in initial_list:
            initial_list.remove(item)

    elif action == "Correct":
        new_item = current_command[2]
        if item in initial_list:
            initial_list[initial_list.index(item)] = new_item

    elif action == "Rearrange":
        if item in initial_list:
            initial_list.remove(item)
            initial_list.append(item)

print(", ".join(initial_list))
