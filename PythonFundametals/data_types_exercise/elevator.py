number_of_people = int(input())
capacity = int(input())
courses = 0
people_left = 0

courses += number_of_people // capacity
people_left += number_of_people % capacity
if people_left > 0:
    courses += 1
print(courses)
