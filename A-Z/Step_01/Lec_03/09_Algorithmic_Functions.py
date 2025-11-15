# sorted()
List1 = [6,2,9,4,1,8]
print(sorted(List1))   # Sorted
List2 = ['aaa','aaaa','a']
print(sorted(List2, key=len))   # Sorted the string list with key length of string

# min, max, sum()
print(min(List1))
# This fun also have key attribute

# any() all()
print(any([1>2,1<2]))
print(all([1>2,1<2]))

# map()

# filter()
print(list(filter(lambda x: x%2 == 0,List1)))

# zip()
print(list(zip(List1,List2)))

# enumerate()

# lambda()
square = lambda x: x * x
print(square(5))

# List Comprehensions
Square = [square(i) for i in List1]
print(Square)

# Dict/Set Comprehensions