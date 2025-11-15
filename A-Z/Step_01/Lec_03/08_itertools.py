# Permutations
from itertools import permutations
arr = [1,2,3]
print("Permutations: ",*permutations(arr,2))

# Combinations
from itertools import combinations
print("Combinations: ",*combinations(arr,2))

# Product
from itertools import product
A = [1,2]
B = ['a', 'b']
print("Product: ",*product(A,B))

# Combinations with rep
from itertools import combinations_with_replacement
print("Combinations_with_repl: ",*combinations_with_replacement(arr,2))

# accumulate
from itertools import accumulate
nums = [1, 2, 3, 4]
print(list(accumulate(nums))) # Sum
# ----OR----
import operator
print(list(accumulate(nums, operator.mul)))  # product

