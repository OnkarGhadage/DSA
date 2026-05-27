# 🚀 DSA Sheet & LeetCode Progress Tracker

This file documents my progress through the Apna College DSA sheet and my tracked LeetCode solutions.

---

## 📚 LeetCode Problem Index

| # | Title | Difficulty | Solution Link |
|---|---|---|---|
| 01 | [169. Majority Element](https://leetcode.com/problems/majority-element/) | 🟢 Easy | [Python 🐍](../Leetcode/Easy/0001-two-sum.py) |
| 02 | [2965. Find Missing and Repeated Values](https://leetcode.com/problems/find-missing-and-repeated-values/) | 🟢 Easy | [Python 🐍](../Leetcode/Easy/2965_Find_Missing_and_Repeated_Values.py) |
| 03 | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/) | 🟢 Easy | [Python 🐍](../Leetcode/Easy/88_Merge_Sorted_Array.py) |

---

## 📝 Detailed Notes & Approaches

### 1. 169. Majority Element 🟢
* **LeetCode Link:** [169. Majority Element](https://leetcode.com/problems/majority-element/)
* **Code:** [169_Majority_Element.py](../Leetcode/Easy/169_Majority_Element.py)
* **Approach:**  
    * Used a count variable for storing count the majority element will be confirmed by this variable. Maintain the variable for majority element cause we have to return the majority element.  
    * Iterate through list if count is 0 then reinitialize the variable to current element.  
    * Increment the count by 1 if current element is equal to variable and decrement by 1 if not equal.
* **Complexity:** Time: $O(n)$ | Space: $O(1)$

### 2. 2965. Find Missing and Repeated Values 🟢
* **LeetCode Link:** [2965. Find Missing and Repeated Values](https://leetcode.com/problems/find-missing-and-repeated-values/)
* **Code:** [2965_Find_Missing_and_Repeated_Values.py](../Leetcode/Easy/2965_Find_Missing_and_Repeated_Values.py)
* **Approach:**  
    * The grid is of n*n size so we calculated the total individual elements in the grid.  
    * By $n*(n+1)/2$ formula we calculated the original sum of 1 to n*n elements.  
    * Initialize actual_sum variable and when we iterate through grid we add every element to this variable.  
initialize dic for knowing the repeated element.  
    * Now we iterate through grid and store the everyelements frequence n the dic. (dic[j] = dic.get(j, 0) + 1).  And if the dic[j] == 2 then the repeated number is j.  
    * After loop ends calculate the missing number = original_sum - (actual_sum - repeated_number).  
return both numbers in one list.
* **Complexity:** Time: $O(n^2)$ | Space: $O(n^2)$

### 3. 88. Merge Sorted Array 🟢
* **LeetCode Link:** [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)
* **Code:** [88_Merge_Sorted_Array.py](../Leetcode/Easy/88_Merge_Sorted_Array.py)
* **Approach:**  
    * Its very intresting problem for two pointer
    * If n == 0 then return immediately. (optional)
    * In this we have to start execution from the end of lists. Initialize the last element in the end of entire nums1 list. and m and n are two pointers at the end of nums1 and nums2 lists.
    * which pointers element is greater in between m and n are assigned to last pointers element.
    * After while ends add one more while at the end we can have some elements remaining in the nums2 list. In reverse order add all remaining elements one by one in nums1 cause we have to do inplace sorting.
* **Complexity:** Time: $O(m + n)$ | Space: $O(1)$