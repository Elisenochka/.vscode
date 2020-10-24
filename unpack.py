numbers = [1,2,3]
print(numbers)
print(*numbers)
print(1,2,3)

values = list(range(5))
values = [*range(5)]
print(values)

values = [*range(5), *"Hello"]

first = [1,2]
second = [3]
values = [*first, *second]

first = {"x":1}
seconf = {"x": 10, "y": 2}
combined = {**first, **second, "z": 3}