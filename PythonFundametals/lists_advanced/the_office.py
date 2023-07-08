employees_happiness = [int(x) for x in input().split()]
factor = int(input())
happy_ppl_counter = 0

new_employees_happiness = [(x * factor) for x in employees_happiness]
average_happiness = sum(new_employees_happiness) / len(new_employees_happiness)
for i in new_employees_happiness:
    if i >= average_happiness:
        happy_ppl_counter += 1
if happy_ppl_counter >= (len(new_employees_happiness) / 2):
    print(f"Score: {happy_ppl_counter}/{len(new_employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {happy_ppl_counter}/{len(new_employees_happiness)}. Employees are not happy!")
