table = set()

for _ in range(int(input())):
    for el in input().split(): # input().split() -> list of strings ["Ce", "O", "H"]
        table.add(el)

print(*table, sep='\n')