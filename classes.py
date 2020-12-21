numbers = [1, 2]

# Class: blueprint for creating new objects
# Object: instance of a class

#Class: Human
# Objects: John, Mary, Jack


class Point:
    default_color = "red"
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x},{self.y})")

    def __str__(self):
        return f"({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


    @classmethod
    def zero(cls):
        return cls(0,0)


Point.default_color = "yellow"
mypoint = Point(1,2)
print(mypoint.default_color)
print(Point.default_color)

print(mypoint.x)
print(mypoint.y)
mypoint.z = 3
print(mypoint.z)
mypoint.draw()

yourpoint = Point(3,4)
yourpoint.draw()
print(yourpoint.default_color)
print(type(mypoint))
print(isinstance(mypoint, Point))
print(isinstance(mypoint, int))

zeropoint = Point(0,0)
zeropoint = Point.zero()
Point.zero()

onemorepoint = Point(1,2)

print(mypoint == onemorepoint)

print(mypoint + yourpoint + onemorepoint)
