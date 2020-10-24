#name -> contact

point = {"x": 1, "y": 2}
point = dict(x = 1, y = 2)
print(point["x"])
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point[a])
print(point.get("a", 0))
del point["x"]
print(point)


for key in point:
    print(key, point[key])



for x in point.items():
    print(x)

for key, value in point.items():
    print(key, value)

values = []
for x in range(5):
    values.append(x * 2)

print(values)

values = [x * 2 for x in range(5)]

values = {x: x * 2 for x in range(5)}
print(values)