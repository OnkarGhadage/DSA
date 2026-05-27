from collections import Counter

List = [1,2,7,2,9,1,5,7,2,0,1,7,9,3] # Random list with repeat values

ct = Counter(List) # Count the number freq
print(ct)
print(sorted(ct)) # Sorted by the keys are sorted
print(sorted(ct.values())) # Sorted by the values are sorted
print(sorted(ct.items())) # Sorted by the keys are sorted

for i,j in sorted(ct.items(), key = lambda x: (-x[1],x[0])):    # Sorted by the values and full dict is in k:v pair
    print(i,j)

print(ct.most_common(2)) # Most common elements
