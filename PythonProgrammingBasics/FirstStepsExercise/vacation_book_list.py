
pages_qty = int(input())
pages_per_hr = int(input())
days = int(input())

time_for_reading = pages_qty // pages_per_hr
hrs_per_day = time_for_reading // days
print(hrs_per_day)
