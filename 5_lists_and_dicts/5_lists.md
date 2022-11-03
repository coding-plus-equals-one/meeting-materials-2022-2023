# Lists
## A list is a sequence
Like a string, a list is a sequence of values. In a string, the values are characters; in a list, they can be any type. The values in a list are called elements.

There are several ways to create a new list. The simplest is to enclose the elements in square brackets:

```python
[10, 20, 30, 40]
['crunchy frog', 'ram bladder', 'lark vomit']
```

The first example is a list of four integers. The second is a list of three strings. The elements of a list don’t have to be the same type. The following list contains a string, a float, and (lo!) another list. A list within another list is nested.

```python
['coding', ["plus", "equals"], 1.0]
```

As you might expect, you can assign list values to variables:

```python
clubs = ['coding += 1', 'Mu Alpha Theta', 'Ultimate Frisbee']
people = ['Alex', 'Ethan', 'Ronan', 'Soolyn']
empty = []
```

## Accessing elements using the index
To access the elements of a list, use the bracket operator. The expression inside the brackets specifies the *index*. The first element is index 0, the second element is index 1, the third is index 2, and so on.

```python
clubs[0] # 'coding += 1'
```

Here are some rules:
- If you try to read or write an element that does not exist, you get an `IndexError`.
- If an index has a negative value, it counts backward from the end of the list.

You can assign new values to the list using its index.

```python
clubs[2] = 'Rocketry'
print(clubs) # ['coding += 1', 'Mu Alpha Theta', 'Rocketry']
```

Notice that `'Rocketry'` replaced `'Ultimate Frisbee'`.


## Traversing the list using a for loop

This works when you only need to read the elements of a list. 

```python
for person in people:
    print("Hi", person)
```

Another common method is to combine the built-in functions `range` and `len`:

```python
for i in range(len(people)):
    print("Hi", people[i])
```

When you want to write or update the elements, you need the indices. 

```python
num = [1, 2, 3]
for i in range(len(num)):
    num[i] = num[i]**2

print(num) # [1, 4, 9]
```

## List operations

The `+` operator concatenates lists:

```python
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

print(c) # [1, 2, 3, 4, 5, 6]
```

The `*` operator repeats a list a given number of times:

```python
print([0] * 4) # [0, 0, 0, 0]
print([1, 2, 3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]
```

You can also access a portion of the list using the slice operator. This is called splicing. The syntax is `[start:stop:step]`. Note that the element with the `stop` index is omitted. 

```python
num = [0, 1, 2, 3, 4, 5]
print(num[1:3])          # [1, 2]
print(num[2:5])          # [2, 3, 4]
print(num[:3])           # [0, 1, 2]
print(num[3:])           # [3, 4, 5]
print(num[:])            # [0, 1, 2, 3, 4, 5]
print(num[::2])          # [0, 2, 4]
print(num[::-1])         # [5, 4, 3, 2, 1, 0]
```

## List methods

Python provides methods that operate on lists. For example, `append` adds a new element to the end of a list:

```python
alpha = ['a', 'b', 'c']
alpha.append('d')
print(alpha) # ['a', 'b', 'c', 'd']
```

`extend` takes a list as an argument and appends all of the elements:

```python
alpha = ['a', 'b', 'c']
alpha.extend(['d', 'e', 'f'])
print(alpha)  # ['a', 'b', 'c', 'd', 'e', 'f']
```

`sort` arranges the elements of the list from low to high:

```python
num = [1, 4, 2, 5, 3]
num.sort()
print(num) # [1, 2, 3, 4, 5]
```

Note that most methods are void, and they modify the list in-place. This means that methods like `sort` will change `num`, but you'll be disappointed if you assign it to a variable like `num2 = num.sort()`. (Try it!) 

## Deleting elements

There are several ways to delete elements from a list. If you know the index of the element you want, you can use `pop`. 

```python
alpha = ['a', 'b', 'c', 'd', 'e', 'f']
alpha.pop(0)
print(alpha) # ['b', 'c', 'd', 'e', 'f']
```

If you know the element you want to remove (but not the index), you can use `remove`. 

```python
alpha = ['a', 'b', 'c', 'd', 'e', 'f']
alpha.remove('a') # ['b', 'c', 'd', 'e', 'f']
print(alpha)
```

To remove more than one element, you can use `del` with a slice index.

```python
alpha = ['a', 'b', 'c', 'd', 'e', 'f']
del alpha[1:5]
print(alpha) # ['a', 'f']
```

## Lists and strings

A string is a sequence of characters and a list is a sequence of values, but a list of characters is not the same as a string. To convert from a string to a list of characters, you can use list:

```python
s = 'spam'
t = list(s)
print(t) # ['s', 'p', 'a', 'm']
```

Because `list` is the name of a built-in function, you should avoid using it as a variable name.

The `list` function breaks a string into individual letters. If you want to break a string into words, you can use the split method:

```python
phrase = 'Beautiful is better than ugly.'
phrase_lst = phrase.split()
print(phrase_lst) # ['Beautiful', 'is', 'better', 'than', 'ugly.']
```

An optional argument called a delimiter specifies which characters to use as word boundaries. The following example uses a hyphen as a delimiter:

```python
s = 'spam-spam-spam'
t = s.split('-')
print(t) # ['spam', 'spam', 'spam']
```