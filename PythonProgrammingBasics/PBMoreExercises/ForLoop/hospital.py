n = int(input())
examined_patient = 0
unexamined = 0
doctors = 7

for i in range(1, n + 1):
    user_input = int(input())
    if i % 3 == 0:
        if unexamined > examined_patient:
            doctors += 1
    if user_input <= doctors:
        examined_patient += user_input
    else:
        unexamined += user_input - doctors
        examined_patient += doctors


print(f'Treated patients: {examined_patient}.')
print(f'Untreated patients: {unexamined}.')
