def increment(number, by=1):
    return number + by

result = increment(2,v1)
print(result)

print(increment(2,5))

def increment(number, by=1):
    return number + by

result = increment(2,v1)
print(result)

print(increment(2,5))


def multiply(*numbers):
    print(numbers)

multiply(2,3,4,5)

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= numbers
        print(numbers)

print(multiply(2, 3, 4, 5))