name_actor = input()
academy_points = float(input())
n = int(input())

for i in range(n):
    rater_name = input()
    rater_points = float(input())
    rater_name_length = len(rater_name)
    rater_total_points = ((rater_name_length * rater_points) / 2)
    academy_points += rater_total_points
    if academy_points >= 1250.5:
        break
if academy_points > 1250.5:
    print(f'Congratulations, {name_actor} got a nominee for leading role with {academy_points:.1f}!')
else:
    print(f'Sorry, {name_actor} you need {(1250.5 - academy_points):.1f} more!')
