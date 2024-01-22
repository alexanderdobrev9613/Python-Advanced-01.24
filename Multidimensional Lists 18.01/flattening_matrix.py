row = int(input())

flattened = []
for i in range(row):
    row_data = [int(el) for el in input().split(', ')]
    flattened.extend(row_data) # kudeto extend razopakova i ednovremenno dobavq razopakovanite elementi ot list kum lista

#ako nqma extend:
# flattened = []
# for row in matrix:
#     for el in row:
#         flattened.append(el)

print(flattened)