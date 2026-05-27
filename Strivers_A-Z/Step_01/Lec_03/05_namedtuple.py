from collections import namedtuple

Point = namedtuple("Name",'x y')
# Point = namedtuple("Point", ['x','y'])

p1 = Point(10,20)
print(p1)
print(p1.x)
print(p1.y)
print(p1[0])
print(p1[1])