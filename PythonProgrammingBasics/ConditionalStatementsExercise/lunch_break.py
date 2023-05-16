import math

name = input()
time_lenght = int(input())
break_time = int(input())

time_for_lunch = break_time * 0.125
time_for_relax = break_time * 0.25
total_time = time_for_lunch + time_for_relax + time_lenght
time_left = math.ceil(break_time - total_time)
time_needed = math.ceil(total_time - break_time)


if total_time <= break_time:
    print(f"You have enough time to watch {name} and left with {time_left} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {time_needed} more minutes.")
