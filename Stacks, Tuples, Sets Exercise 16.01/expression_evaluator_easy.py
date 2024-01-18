from collections import deque
from math import floor

expression = deque(input().split()) #["6", "3", -, ..."]
idx = 0

while idx < len(expression): # ili while len(expression) > 1
    element = expression[idx]

    if element == '*':
        for _ in range(idx - 1): #- 1 zashtoto everything but the symbol/operator
            expression.appendleft(int(expression.popleft()) * int(expression.popleft()))
    elif element == '/':
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) / int(expression.popleft()))
    elif element == '-':
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) - int(expression.popleft()))
    elif element == '+':
        for _ in range(idx - 1):
            expression.appendleft(int(expression.popleft()) + int(expression.popleft()))

    if element in "*/+-":
        del expression[1] # ako elementa e simvol/operator, iztrivame go
        idx = 1
    idx += 1

print(floor(int(expression[0])))