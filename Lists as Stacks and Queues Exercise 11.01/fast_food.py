from collections import deque

food = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy(): #ili s while Orders:
    if food >= order:
        orders.popleft()
        food -= order
    else:
        print(f"Orders left:", *orders) # " ".join([str(x) for x in orders])
        break
else:
    print('Orders complete')