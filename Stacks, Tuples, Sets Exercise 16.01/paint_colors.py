from collections import deque

words = deque(input().split()) #d yel blu e low redd

colors = {'red', 'yellow', 'blue', 'purple', 'orange', 'green'}

requested_colors = {
    "orange": {'red', 'yellow'},
    "purple": {'blue', 'red'},
    "green": {'yellow', 'blue'}
}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ''

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]): # 'd' 'redd' -> '', 'red'
            if el:
                words.insert(len(words) // 2, el)

for color in set(requested_colors.keys()).intersection(result):
    # requested_colors.keys() -> {orange, gree, purple}.intersection(["orange", "red", "yellow"]) -> {orange}
    if not requested_colors[color].issubset(result):
        result.remove(color) # moje i s discard

print(result)
