# Reading Code
Learning how to read code is important, especially when you work with other people on larger projects. Research shows that programmers spend about 60% of their time reading code. As you read more code, you'll get better at coding too!

## Problem 1: Squares of a Sorted Array
Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Example 1:**
```
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
```

**Example 2:**
```
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
```

**Constraints:**
```
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
```

**Solution:**

Note that this solution involves list comprehension. Try refactoring the code so that it doesn't have list comprehension.

```python
def sortedSquares(nums: List[int]) -> List[int]:
        return sorted([i**2 for i in nums])
```

## Problem 2: Find Numbers with Even Number of Digits
Given an array `nums` of integers, return how many of them contain an even number of digits.


**Example 1:**
```
Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
```

**Example 2:**
```
Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
```

**Constraints:**
```
1 <= nums.length <= 500
1 <= nums[i] <= 10^5
```

**Solution:**
Note that this solution uses list comprehension. Try refactoring the code so that it doesn't use list comprehension.

```python
def findNumbers(nums: List[int]) -> int:
    return sum([len(str(i)) % 2 == 0 for i in nums])
```

## Problem 3: Max Consecutive Ones

Given a binary array *nums*, return the maximum number of consecutive 1's in the array.

**Example 1**
```
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
```

**Example 2:**
```
Input: nums = [1,0,1,1,0,1]
Output: 2
```

**Constraints:**
```
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
```

**Solution**

Note that this solution uses recursion. I recommend tracing the code.

```python
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    def count(lst, max_):
        if len(lst) == 0:
            return max_

        total = 0
        i = 0

        while len(lst) > i and lst[i] == 1:
            total += 1
            i += 1

        if total > max_:
            max_ = total

        return count(lst[i + 1 :], max_)
    return count(nums, 0)
```
