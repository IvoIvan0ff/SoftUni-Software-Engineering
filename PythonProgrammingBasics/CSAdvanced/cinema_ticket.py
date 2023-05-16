day = input()
result = ''

if day == 'Monday' or day == 'Tuesday' or day == 'Friday':
    result = 12
elif day == 'Wednesday' or day == 'Thursday':
    result = 14
else:
    result = 16

print(result)
