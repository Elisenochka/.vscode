import copy
r = [1, 2, 3]
r.append(r)
print(r)
[1, 2, 3, [...]]
p = copy.deepcopy(r)
print(p)
[1, 2, 3, [...]]
for i in r.pop():
    print(i)
print(str(r.pop()))
print(str(r.pop()))