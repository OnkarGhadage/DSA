import bisect

# Binary search

arr = [1,3,3,5,7,9]
print(arr)
print()

print(bisect.bisect_left(arr,3)) # Index to insert x so all elements before it are > x
print(bisect.bisect_right(arr,3)) # Index to insert x so all elements before it are <= x
print()

bisect.insort(arr,4) # Insert 4 while the array remain sorted
print(arr)
print()

#insort_left - _   Similar to bisect_l/r
#insort_right -

