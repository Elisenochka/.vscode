letters = ["a","b","c",]
matrix = [[0,1],[2,3]]
zeros =[0] *100
zeros = [0] * 5
combined = zeros + letters

numbers = list(range(20))
chars = list("hello world")
print(chars)
print(len(chars))

letters = ["a", "b","c","d"]
letters[0] = "A"
print(letters[0:3])
print(letters[0:])
print(letters[::2])

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])
print(numbers[::1])

numbers = [1, 2, 3]
first = numbers[0]
second = numbers[1]
third = numbers[2]

first, second, third = numbers
numbers = [1,2,4,4,4,4,4,4]
first, second, *other = numbers

print(first)
print(other)

def multiply(*numbers):
    k=1
    for i in numbers:
        k = k * i
    return k

print(multiply(1,2,3,4,5))

letters = ["a","b","c"]
for letter in enumerate(letters):
    print(letter)

items = (0, "a")
index, letter = items
for index, letter in enumerate(letters):
    print(index, letter)

letters.append("d")
print(letters)
letters.insert(0,"-")

letters.pop(0)
print(letters)

letters.remove("b")
del letters[0:3]
print(letters)
letters.clear()
print(letters)

letters = ["a","b","c"]
print(letters.count("d"))
if "d" in letters:
    print(letters.index("d"))

numbers = [3, 52, 3, 8, 6]
#numbers.sort(reverse = True)
print(numbers)
print(sorted(numbers, reverse = True)) #not modify

items = [
    ("product1", 10),
    ("product2", 7),
    ("product3", 12),
]


def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)


items = [
    ("product1", 10),
    ("product2", 7),
    ("product3", 12),
]


items.sort(key = lambda item:item[1])
print(items)

items = [
    ("product1", 10),
    ("product2", 7),
    ("product3", 12),
]

prices = []
for item in items:
    prices.append(item[1])
x = map(lambda item: item[1], items)

prices = list(map(lambda item:item[1], items))
print(x)
print(prices)

for item in x:
    print(item)

items = [
    ("product1", 10),
    ("product2", 7),
    ("product3", 12),
]

x = list(filter(lambda item: item[1] >=10, items))
print(x)


prices = list(map(lambda item: item[1], items))
#[item[1] expression for item in items]

prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1]>=10, items))

filtered = [item for item in items if item[1]>=10]

list0 = [1,2,3]
list1 = [10,20,30]

print(zip(list0,list1))
[(1,10), (2,20),(3,30)]

print(list(zip(list0,list1)))
print(list(zip("abc", list0)))

[1,2,3]

browsing_session =[]
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last=browsing_session.pop()
print(last)
print(browsing_session)
print("redirect", browsing_session[-1])
if not browsing_session:
    print("disable")




[1,2,3,4]

