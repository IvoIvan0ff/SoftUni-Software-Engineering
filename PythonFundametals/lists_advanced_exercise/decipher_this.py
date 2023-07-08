houses = [int(x) for x in input().split('@')]
len_neighborhood = len(houses)
index = 0
jump_command = input()
while jump_command != 'Love!':
    index += int(jump_command.split()[1])
    if index >= len_neighborhood:
        index = 0
    if houses[index] > 2:
        houses[index] -= 2
    else:
        if houses[index] != 0:
            houses[index] -= 2
            text = 'has'
        else:
            text = 'already had'
        print(f"Place {index} {text} Valentine's day.")
    jump_command = input()

print(f"Cupid's last position was {index}.")
failed_houses = sum(1 for x in houses if x != 0)

if failed_houses:
    print(f"Cupid has failed {failed_houses} places.")
else:
    print("Cupid has failed {houseCount} places.")
