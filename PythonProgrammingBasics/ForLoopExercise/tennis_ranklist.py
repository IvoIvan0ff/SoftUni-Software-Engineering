import math

tournament_qty = int(input())
starting_points = int(input())
won_tournaments = 0
total_points = 0

for i in range(tournament_qty):
    user_input = input()
    if user_input == 'W':
        total_points += 2000
        won_tournaments += 1
    elif user_input == 'F':
        total_points += 1200
    elif user_input == 'SF':
        total_points += 720

average_points = total_points / tournament_qty
won_percentage = won_tournaments / tournament_qty * 100
starting_points += total_points

print(f'Final points: {starting_points:.0f}')
print(f'Average points: {math.floor(average_points):.0f}')
print(f'{won_percentage:.2f}%')
