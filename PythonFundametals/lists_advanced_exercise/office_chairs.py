rooms = int(input())
free_chairs = 0
total_chairs = 0
room_counter = 0
total_visitors = 0
for i in range(rooms):
    room_counter += 1
    current_room = input().split()
    chairs_qty = len(current_room[0])
    visitors = int(current_room[1])
    total_chairs += chairs_qty
    total_visitors += visitors
    if visitors > chairs_qty:
        print(f'{visitors - chairs_qty} more chairs needed in room {room_counter}')
if total_chairs >= total_visitors:
    print(f'Game On, {abs(total_chairs - total_visitors)} free chairs left')
