number_of_electrons = int(input())
shell_list = []


for i in range(number_of_electrons):
    current_electrons = 2 * ((i + 1) ** 2)
    shell_list.append(current_electrons)
    number_of_electrons -= current_electrons
    if number_of_electrons == 0:
        break
    if current_electrons > number_of_electrons > 0:
        shell_list.append(number_of_electrons)
        break

print(shell_list)
