x = 10
y = 11
print(x, " ", y)

z = [x, y]
y = z[0]
x = z[1]
print(x, " ", y)

x, y = y, x
print(x, " ", y)
