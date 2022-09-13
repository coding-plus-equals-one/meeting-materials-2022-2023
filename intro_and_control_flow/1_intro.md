# Introduction

In this document, we will cover `print()`, variables, functions, and data types (strings, integers, floats).

## Hello, World!

A long-held belief in the programming world has been that printing a _Hello, world!_ message to the screen as your first program in a new language will bring you luck. 

In Python, you can write the Hello World program in one line: 

``` python
print("Hello, world!")
```

## Variables

We can also store _values_ in _variables_. 

Here is an example:

``` python
message = "Goodnight, world!"
print(message)
```

`message` is the variable name, and it has a value of `"Goodnight, world!"`.

Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a number. It's also convention to make them lowercase.  Try to keep them short but descriptive.

Here are some quick examples:
- `message_1` and `_message` are acceptable variable names
- `message 1` will not work because there is a space
- `1_message` will not work because it starts with a number
- `Message` is an odd variable name, even though the code will still run

## Functions

We can define functions to reuse code. The function ends when it reaches a return statement or when it executes the last statement in the function. 

``` python
def get_greeting(name):
    return "Hello, " + name + "!"
```

The function `get_greeting` takes in the variable `name` and _returns_ a new string. We can store the return value in another variable. We can also print out this value.

``` python
greeting = get_greeting("Sal")
print(greeting)
```

If the function doesn't have a `return` statement, it automatically returns `None`. The function below calls the print statement inside it. But since it doesn't have a return statement,   

``` python
def get_greeting(name):
  print("Hello, " + name + "!")

greeting = get_greeting("Khan")
print(greeting) # None
```

## Data Types
### Strings

There are many different types of data types in Python. A _string_ is a series of characters. Anything inside quotes is considered a string.

``` python
"This is a string."
'This is also a string.'
```

This allows you to use apostrophes and quotes in your string.

``` python
"The language 'Python' is named after Monty Python, not the snake."
```

### Integers

Here is a short list of the operations you can do with integers:

| Symbol | Meaning  |
|--------|----------|
| +      | Add      |
| -      | Subtract |
| *      | Multiply |
| /      | Divide   |
| **     | Exponent |

You can also turn integers into strings using the `str()` method. Note that you can add strings together, but you can't add strings and integers together unless you turn the integer into a string.

``` python
age = 25
print("Happy " + str(age) + "th" + " birthday!")
```

### Floats

Python calls any number with a decimal point a _float_. For the most part, you can use decimals without worrying about how they behave.

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

### Modulo

A nifty operator is the modulus operator `%`. It returns the remainder when the computer divides one integer by another. For example, `4 % 2` is 0, and `5 % 11` is 1. We can use modulo to determine if a number is divisible by another (if a number is divisible, the remainder should be 0).

``` python
num = 10
if num % 5 == 0:
    print("It is divisible by 5!")
else:
    print("It is not divisible by 5.")
```

Note that `==` compares whether two values are equal. It is not the same as variable assignment, which uses `=`.

**Check challenges.md for the Exercise 1.**