class Party:
    people = []

    def __init__(self):
        pass


while True:
    name = input()
    if name == 'End':
        break
    Party.people.append(name)
print(f"Going: {', '.join(Party.people)}")
print(f"Total: {len(Party.people)}")
