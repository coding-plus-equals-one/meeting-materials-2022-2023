# A note about LeetCode

LeetCode is a website is a website where people can practice solving coding problems. Getting started can be a bit intimidating, so here is a simple explanation. Let's use the [66. Plus One](https://leetcode.com/problems/plus-one/) problem as an example. 

## 66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

**Example 1:**
```
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
```

**Example 2:**
```
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
```

**Example 3:**
```
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
```

## How to test and submit your code

On the left side, you will see a screen where you can type in your code. First, go to the button above and pick Python 3. You will then see this appear on the screen:

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
```

Let's go through this one by one:
1. `class Solution:` is the class LeetCode provides for you. They use it to test the code on their own servers. 
2. `def plusOne(self, digits: List[int]) -> List[int]:` is the function that LeetCode provides for you. 
   1. The name of the function is `plusOne`
   2. `self` is an parameter needed for the `Solution` class. You can ignore it.
   3. `digits: List[int]` is a parameter that you will use. `digits` is the name of the parameter. `List[int]` specifies that the parameter is a list of integers.
   4. `-> List[int]` specifies the return value of the function. This function should return a list of integers.


If you want to first test your code in repl.it or VSCode, you can simplify this header:

```python
def plusOne(digits):
```

Then, write and test your code. Remember to return the final value! It is not necessary to print it out (although you might want to for testing purposes).

```python
def plusOne(digits):
    num = int("".join([str(d) for d in digits]))
    num += 1
    digits = [int(d) for d in str(num)]
    return digits
```

Finally, put your code back into the header that LeetCode provides for you.

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
         num = int("".join([str(d) for d in digits]))
         num += 1
         digits = [int(d) for d in str(num)]
         return digits
```

First press the Run Code button. If it passes the initial tests, press the Submit button. LeetCode will run even more tests on the code. You'll usually have to edit the code multiple times so that it passes.