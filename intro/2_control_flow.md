# Control Flow

Control flow statements help us control the order that the code executes. Sometimes we want only the code to run if a given condition is true. Other times, we want the one part of the code to run multiple times. 

## `if`, `elif`, and `else`

These statements run one piece of code if a certain condition is true.

``` python
age = 15

if age < 18:
    print("Sorry, the federal voting age is 18.")
elif age < 21:
    print("Sorry, the drinking age is 21.")
else:
    print("Wow, there's a lot you can do!")
```

The first condition that is true is `age < 18`. Thus, the program runs `print("Sorry, the federal voting age is 18.")`. Notice that the elif branch doesn't run, even though `age < 21` is also true. That's because the `if` branch came first.

## for loops
The `for` loops and the `range()` method usually appear hand-in-hand.

A `for` loop iterates through any sequence. A string is a sequence of characters. Try running this: 

``` python
message = 'Hello! Goodbye?'
for char in message:
    print(char)
```

**Check challenges.md for the Exercise 2.**

## range() method

`range()` generates a sequence of numbers, and it has the _parameters_ `min_value` and `max_value`. Its syntax is `range(, max_value)`. If there is only one parameter, `min_value` defaults to zero.

Try running these pieces of code in test.py:

``` python
for i in range(6):
    print(i)
```
``` python
for i in range(1, 6):
    print(i)
```

**Check challenges.md for the Exercise 3.**
