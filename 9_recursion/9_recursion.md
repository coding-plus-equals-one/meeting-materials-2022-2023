# Recursion

Recursion is an approach to solving problems. It involves calling a function that calls itself. 

A recursive function should have the following properties so that it does not result in an infinite loop:
1. A simple *base case* (or cases) — a terminating scenario that does not use recursion to produce an answer.
2. A set of rules, also known as *recurrence relation* that reduces all other cases towards the base case.

For some problems, we can use both iteration and recursion. For other problems, one approach makes more sense.

Here is how we can reverse a string with iteration. Note that we are using a `for` loop to traverse the string.
```python
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
```

Here is how we can reverse a string with recursion. Note that the `reverse` function calls itself.
```python
def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]
```

The bonus `canMeasureWater` problem in our club competition is one scenerio where it makes sense to use recursion. Here is the problem and the solution again:

You are given two jugs with capacities `jug1` and `jug2`. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly `target` liters using these two jugs. For `target` liters of water to be measurable, you must have `target` liters of water total contained within one or both buckets by the end.

Operations allowed:
- Fill any of the jugs completely up to their capacity.
- Empty any of the jugs completely.
- Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

``` python
def canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity):
    if jug1Capacity + jug2Capacity < targetCapacity:
        return False

    divisors = list(set([jug1Capacity, jug2Capacity]))

    def get_mod(a, b):
        value = a % b if a > b else b % a

        if value != 0 and value not in divisors:
            divisors.append(value)
            get_mod(value, a)
            get_mod(value, b)

    get_mod(jug1Capacity, jug2Capacity)

    for i in divisors:
        if targetCapacity % i == 0:
            return True

    return False
```