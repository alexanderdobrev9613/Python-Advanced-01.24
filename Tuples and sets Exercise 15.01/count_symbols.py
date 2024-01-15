occurrences = {}

for letter in input():
    occurrences[letter] = occurrences.get(letter, 0) + 1

for letter, times in sorted(occurrences.items()): # (("a", 1), ("b", 3))
    print(f"{letter}: {times} time/s")