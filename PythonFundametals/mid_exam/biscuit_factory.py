import math

biscuits_per_day_per_worker = int(input())
workers_count = int(input())
competing_factory_producing = int(input())
total_biscuits = 0
day_counter = 0
daily_production = biscuits_per_day_per_worker * workers_count

for i in range(30):
    day_counter += 1
    if day_counter % 3 == 0:
        total_biscuits += math.floor(daily_production * 0.75)
    else:
        total_biscuits += daily_production

difference = abs(competing_factory_producing - total_biscuits)
percentage_diff = (difference / competing_factory_producing) * 100

print(f"You have produced {total_biscuits} biscuits for the past month.")

if total_biscuits > competing_factory_producing:
    print(f"You produce {percentage_diff:.2f} percent more biscuits.")
else:
    print(f"You produce {percentage_diff:.2f} percent less biscuits.")
