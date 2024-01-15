numbers = tuple([float(el) for el in input().split()])

repeated = {}

for number in numbers:
    if number not in repeated:
        repeated[number] = numbers.count(number)

for num, repetitions in repeated.items():
    print(f'{num} - {repetitions} times')
