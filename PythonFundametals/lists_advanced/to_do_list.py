to_do_list = [0] * 10

while True:
    notes = input()
    if notes == 'End':
        break
    current_note = notes.split('-')
    index = int(current_note[0])
    task = current_note[1]
    to_do_list.pop(index - 1)
    to_do_list.insert(index - 1, task)

new_to_do_list = [s for s in to_do_list if s != 0]

print(new_to_do_list)
