from functools import reduce

def operate(operator, *args):
    if operator == '+':
        return reduce(lambda x, y: x + y, args)
    if operator == '-':
        return reduce(lambda x, y: x - y, args)
    if operator == '*':
        return reduce(lambda x, y: x * y, args)
    if operator == '/':
        return reduce(lambda x, y: x / y, args)

#vmesto ifovete gore moje i:
# return reduce(lambda x,y: eval(f"{x}{operator}{y}"), args)

print(operate("+", 1, 2, 3))