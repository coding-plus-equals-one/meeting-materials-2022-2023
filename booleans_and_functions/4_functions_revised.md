# Functions

Function review! 

Here is how we use functions:
1. We define the function.
   1. We give it a header.
   2. We give it a body.
2. We call the function.
   1. The function runs the code inside of it.
   2. The function returns a value.

Let's look at some examples.

**This function only returns a value.**

```python
def get_greeting(name):
    return "Hello, " + name + "!"

greeting = get_greeting("Ethan")
print(greeting)
```

1. The function is defined on lines 1-2
   1. The header is `def get_greeting(name):`
      1. `def` tells the code that we're defining a function
      2. The name of the function is `get_greeting`
      3. The function takes in one parameter called `name`
   2. The body is `return "Hello, " + name + "!"`
2. We called the function on line 4
   1. First, it runs the code inside of it. There are none.
   2. Then, it returns `"Hello, " + "Ethan" + "!"`. This gets assigned to the variable `greeting`. 
3. On line 5, we can do `print(greeting)` to confirm that there was a return value.

**This function only runs some code. It does not return a value.**

```python
def print_greeting(name):
    print("Hello, " + name + "!")

print_greeting("Ethan")
```

1. The function is defined on lines 1-2
   1. The header is `def print_greeting(name):`
   2. The body is `print("Hello, " + name + "!")`
2. We called the function on line 4
   1. First, it runs `print("Hello, " + name + "!")`. You should see "Hello, Ethan!" printed in the terminal.
   2. Since there isn't a return statement, it returns `None`. 
3. If you run the code below, you'll see that the variable `greeting` was assigned the value `None`.

```python
greeting = print_greeting("Ethan")
print(greeting) # None
```

**This function runs some code *and* returns a value**

```python
def greet(name):
    phrase = "Hello, " + name + "!"
    print(phrase)
    return phrase
```