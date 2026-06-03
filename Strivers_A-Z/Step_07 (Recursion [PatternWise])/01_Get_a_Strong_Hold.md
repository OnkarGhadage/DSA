# Get a Strong Hold


### 1. 8. String to Integer (atoi) 🟠
* **LeetCode Link:** [8. String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi/)
* **Code:** [8_String_to_Integer_(atoi).py](../../Leetcode/Medium/8_String_to_Integer_(atoi).py)
* **Approach:** 
* **Complexity:** Time: $O(n)$ | Space: $O(1)$ (For iterative solution)
* **Complexity:** Time: $O(n)$ | Space: $O(n)$ (For recursive solution)

### 2. 50. Pow(x, n) 🟠
* **LeetCode Link:** [50. Pow(x, n)](https://leetcode.com/problems/powx-n/)
* **Code:** [50_Pow(x,n).py](../../Leetcode/Medium/50_Pow(x,n).py)
* **Approach:** 
    * write a helper fun
        * if x == 0: return 0
        * Base case - if n == 0: return 1
    * res = helper(x, n//2) **Recursion**
    * return res* res* x if n%2 else res*res
* **Complexity:** Time: $O(log n)$ | Space: $O(log n)$

### 3. 1922. Count Good Numbers 🟠
* **LeetCode Link:** [1922. Count Good Numbers](https://leetcode.com/problems/count-good-numbers/)
* **Code:** [1922_Count_Good_Numbers.py](../../Leetcode/Medium/1922_Count_Good_Numbers.py)
* **Approach:** 
    * MOD = 10**9 + 7
    * Used problem 50 helper function to find power just use MOD to avoid overflow
    * calculate number of even and odd places.
    * `even = ceil(n/2)`
    * `odd = n//2`
    * just return (helper(5, even)) * (helper(4, odd)) % MOD
* **Complexity:** Time: $O(log n)$ | Space: $O(log n)$

### 3. Sort a Stack 🟠
* **Problem Link:** [Sort a Stack](https://takeuforward.org/plus/dsa/problems/sort-a-stack?source=strivers-a2z-dsa-track)
* **Code:** [51_Sort_a_Stack.py](../Problem/Medium/51_Sort_a_Stack.py)
* **Complexity:** Time: $O(n^2)$ | Space: $O(n)$

### 4. Reverse a Stack 🟠
* **Problem Link:** [Reverse a Stack](https://takeuforward.org/plus/dsa/problems/reverse-a-stack?source=strivers-a2z-dsa-track)
* **Code:** [52_Reverse_a_Stack.py](../Problem/Medium/51_Sort_a_Stack.py)
* **Complexity:** Time: $O(n^2)$ | Space: $O(n)$