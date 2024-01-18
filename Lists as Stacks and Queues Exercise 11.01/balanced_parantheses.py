from collections import deque

parenthesis = deque(input())
open_parenthesis = deque()

while parenthesis:
    current_parenthesis = parenthesis.popleft()

    if current_parenthesis in "([{":
        open_parenthesis.append(current_parenthesis)
    elif not open_parenthesis:
        print("NO")
        break
    else:
        valid_pair = open_parenthesis.pop() + current_parenthesis
        if valid_pair not in "{}()[]":
            print("NO")
            break

else:
    print("YES")