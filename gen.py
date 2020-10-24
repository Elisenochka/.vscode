from sys import getsizeof

values = [x * 2 for x in range(5)]
for x in values:
    print(x)

#generator object
values = (x * 2 for x in range(5))
print(values)
for x in values:
    print(x)

values = (x * 2 for x in range(1000))
print("gen:", getsizeof(values))
values = (x * 2 for x in range(100000))
print("gen:", getsizeof(values))
values = [x * 2 for x in range(1000)]
print("list:", getsizeof(values))
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))
print(len(values))