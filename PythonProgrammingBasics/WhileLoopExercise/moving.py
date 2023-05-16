width = int(input())
length = int(input())
hight = int(input())
total_space = width * length * hight
box_total_space = 0

while True:
    box_space = input()
    if box_space == 'Done':
        break
    box_space = int(box_space)
    box_total_space += box_space
    if box_total_space >= total_space:
        break

if box_total_space < total_space:
    print(f'{abs(total_space - box_total_space)} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(total_space - box_total_space)} Cubic meters more.')

