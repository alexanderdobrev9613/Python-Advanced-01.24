from collections import deque

water = int(input())
name = input()
people = deque()

while name != 'Start':
    people.append(name)
    name = input()

command= input()
while command != 'End':
    data = command.split()
    if len(data) == 1:
        liters_requested = int(data[0])
        person = people.popleft()
        if water >= liters_requested:
            print(f'{person} got water')
            water -= liters_requested
        else:
            print(f'{person} must wait')
    elif len(data) == 2:
        _, liters_to_add = data # _ znachi promenliva koqto nqma da se izpolzva / liters_to_add = data[1]
        water += int(liters_to_add)
    command = input()

print(f'{water} liters left')
