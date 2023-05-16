record = float(input())
distance = float(input())
time_for_1meter = float(input())

time_for_distance = distance * time_for_1meter
aditional_time = distance // 15
aditional_time_in_sec = aditional_time * 12.5
total_time = aditional_time_in_sec + time_for_distance
time_needed = total_time - record


if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")
