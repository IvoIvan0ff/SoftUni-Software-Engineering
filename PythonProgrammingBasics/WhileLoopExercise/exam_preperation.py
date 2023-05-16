failure_grade = int(input())
task_qty = 0
average = 0
fails = 0
task_real_name = ''

while True:
    task_name = input()
    if task_name == 'Enough':
        print(f'Average score: {average / task_qty:.2f}')
        print(f'Number of problems: {task_qty}')
        print(f'Last problem: {task_real_name}')
        break
    current_grade = int(input())
    task_qty += 1
    average += current_grade
    task_real_name = task_name
    if current_grade <= 4:
        fails += 1
        if fails >= failure_grade:
            print(f'You need a break, {failure_grade} poor grades.')
            break
