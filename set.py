numbers = [1, 1, 2, 3, 4]
uniques = set(numbers)
second = {1, 4}
second.add(5)
#second.remove(5)
len(second)
print(uniques)


first = set(numbers)

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)

print(first[0])

if 1 in first:
    print("yes")

