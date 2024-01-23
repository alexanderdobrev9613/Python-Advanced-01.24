numbers = [string.split() for string in input().split("|")] #[[7, 88], [4, 5, 6], ...]
print(*[' '.join(sub_list) for sub_list in numbers[::-1] if sub_list])