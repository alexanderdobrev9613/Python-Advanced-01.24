from collections import deque

# pump_data = []
# for _ in range(int(input())):
#     pump_data.append([int(x) for x in input().split()])

pumps_data = deque([[int(x) for x in input().split()] for _ in range(int(input()))]) # [[1,5], [10, 3], [5, 9]

pumps_data_copy = pumps_data.copy()
gas_in_tank = 0
index = 0

while pumps_data_copy:
    petrol, distance = pumps_data_copy.popleft() #naprimer petrol 5  distance 1 / 10, 3 / 5, 9

    gas_in_tank += petrol

    if gas_in_tank >= distance:
        gas_in_tank -= distance
    else:
        pumps_data.rotate(-1) #obrushta
        pumps_data_copy = pumps_data.copy()
        index += 1 #zashtoto veche pochvame ot dr benzinostanciq
        gas_in_tank = 0

print(index)