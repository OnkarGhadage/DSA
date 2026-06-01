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