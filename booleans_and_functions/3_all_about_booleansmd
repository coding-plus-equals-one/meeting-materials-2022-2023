# Booleans
## Definition
While the integers, floats, and strings have an unlimited number of possible values, Booleans only have two values: `True` and `False`. (Boolean is capitalized because the data type is named after mathematician George Boole.) 

Boolean values True and False don't have the quotes you place around strings, and they always start with a capital T or F, with the rest of the word in lowercase. 

## Comparison Operators
Here we should formally talk about comparison operators. They always evaluate to `True` or `False` depending on the values you give them.

| Operator | Meaning                  |
|----------|--------------------------|
| ==       | Equal to                 |
| !=       | Not equal to             |
| <        | Less than                |
| >        | Greater than             |
| <=       | Less than or equal to    |
| >=       | Greater than or equal to |

## `==` vs `=`
You might have noticed that the `==` operator (equal to) has two equal signs, while the `=` operator (assignment) has just one equal sign. It’s easy to confuse these two operators with each other. Just remember these points:
- The == operator (equal to) asks whether two values are the same as each other.
- The = operator (assignment) puts the value on the right into the variable on the left.

To help remember which is which, notice that the == operator (equal to) consists of two characters, just like the != operator (not equal to) consists of two characters.

## Back to `if` statements 
You already used Booleans when you worked with if-then statements! Take a look at the example code we used below.

``` python
age = 15

if age < 18:
    print("Sorry, the federal voting age is 18.")
elif age < 21:
    print("Sorry, the drinking age is 21.")
else:
    print("Wow, there's a lot you can do!")
```

We can actually figure out what each of the expressions evaluated to. Try adding these lines to the code above. 

```python
print(age < 18) # True
print(age < 21) # True
print(age != 15) # False
```

As you can see, the code ran the first time it hit a true statement. To be honest, we could've just replaced the entire code with Booleans too.

``` python
if True:
    print("Sorry, the federal voting age is 18.")
elif True:
    print("Sorry, the drinking age is 21.")
else:
    print("Wow, there's a lot you can do!")
```

But then we wouldn't be able to edit our `age` variable! It's better to have the code compute the right Boolean value for `age < 18`, so that the program will do different things. You'll learn how to take user input soon. 

# Boolean Operators

The three Boolean operators (`and`, `or`, and `not`) are used to compare Boolean values. Like comparison operators, they evaluate these expressions down to a Boolean value. 

## `and`
The `and` operator evaluates an expression to `True` if both Boolean values are `True`; otherwise, it evaluates to `False`.

```python
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
```

## `or`
On the other hand, the or operator evaluates an expression to `True` if either of the two Boolean values is `True`. If both are `False`, it evaluates to `False`.

```python
print(True or True) # True
print(True or False) # True
print(False or True) # True
print(False or False) # False
```

## `not`

Unlike `and` and `or`, the `not` operator operates on only one Boolean value (or expression). The `not` operator simply evaluates to the opposite Boolean value.

```python
print(not True) # False
print(not False) # True
print(not not not not True) # True
```

**Check challenges.md for the Exercise 1.**
