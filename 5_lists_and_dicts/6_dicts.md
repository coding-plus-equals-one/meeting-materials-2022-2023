# Dicts (Dictionaries)
## A dictionary is a sequence
Dictionaries are like lists but with indexes set by the creator of the dict rather than just 0, 1, 2, 3. The values in a dict are stored as key:value pairs where the key acts as the index. Both the key and the value can be any value.

There are several ways to create a new dict. The simplest is to enclose the key:value pairs inside curly braces:

```python
{"key0":"value0", "key1":"value1", "key2":"value2"}
{1:False, 1.52:"cattle", True:234, "string":1.242}
```

The first example is a dict of four key:value pairs that are all strings. The second is a dict with mismatched types. The key:value pairs don’t have to be the same type. You can have repeated values but not repeated keys.

```python
{"hats":"sphere", "hats":"axe", "castle":"axe"}
{"hats":"axe", "castle":"axe"}
```

The first dict will become the second dict when the code is run. Repeated keys will use the last instance of the key. The repeated value is allowed.

Alternatively you can use `dict()` to create dictionaries in two other ways.

```python
dict(hats="value", cats="hats") # {"hats":"value", "cats":"hats"}
dict([(1, 4), ("key", "value"), ("thing", 3)]) # {1:4, "key":"value", "thing":3}
```

Another way to quickly create a dictionary where all the values are the same is `dict.fromkeys()`. This will take 2 arguments. The first is an iterable (usualy a list) that contains keys. The second is the value. If there is no second value, it will default to `None`.

```python
dict.fromkeys([1,2,3], "nums") # {1:"nums", 2:"nums", 3:"nums"}
dict.fromkeys([5,6,7]) # {5:None, 6:None, 7:None}
```

As you might expect, you can assign dictionaries to variables:

```python
officers = {"John":"Java", "Elvin":"Java", "Chloe":"Python"}
days = {0:"sunday", 1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday"}
empty = dict()
```

## Accessing elements with keys
To access the values of a dictionary, use the bracket operator. The expression inside the brackets specifies the *key*. The key will access the value it corresponds to.

```python
officers["John"] # "Java"
days[2] # "tuesday"
```

Here are some rules:
- If you try to read an element that does not exist, you will get a `KeyError`.
- If you try to edit or assign to a key that does not exist, that key:value pair will be created and put at the end of the dict.

You can assign new key:value pairs or edit existing ones in the dictionary using a key.

```python
officers["Davidson"] = "Java"
print(officers) # {"John":"Java", "Elvin":"Java", "Chloe":"Python", "Davidson":"Java"}

days[1] = "ethanday"
print(days) # {0:"sunday", 1:"ethanday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday"}
```

Notice that the key `"Davidson"` was added with value `"Java"` and `"ethanday"` replaced `"monday"`.

Alternatively, you can use the `.get()` and `.setdefault()` methods instead in order to avoid errors.

`.get()` has two arguments. The first argument is the key you want to access. The second argument is the value you want to return if the key doesn't exist. The second argument is optional and defaults to `None`.

```python
x = officers.get("Davidson", "Not a real officer") # "Java"
y = officers.get("Washington", "Not a real officer") # "Not a real officer"
z = officers.get("Monroe") # None
```

`.setdefault()` works in the same way as `.get()` but will add the first and second arguments as a key:value pair if the key doesn't exist
```python
x = officers.setdefault("Davidson", "spheres") # "Java"
y = officers.setdefault("Ronan", "Python") # "Python"
z = officers.setdefault("Monroe") # None
print(officers) # {"John":"Java", "Elvin":"Java", "Chloe":"Python", "Davidson":"Java", "Ronan":"Python", "Monroe":None}
```

## Viewing the keys and values of a dict


 The `.keys()`, `.values()`, and `.items()` methods return an iterable of type `dict_values`. A dict_values object can be turned into a list with `list(dict_values)` or iterated with a loop. They do not natively have indexing.

```python
aDict = {0:"cherry tree", 1:"hats", 2:"sphere"}
keys = aDict.keys() # dict_values([0, 1, 2])
vals = aDict.values() # dict_values(["cherry tree", "hats", "sphere"])
items = aDict.items() # dict_values([(0, "cherry tree"), (1, "hats"), (2, "sphere")])
```

## Traversing the dict using a for loop

To iterate through all the keys in a dictionary you can use either of the following. 
Note: you cannot edit the keys of a dictionary by editing the value of key

```python
a = {"k0":"v0", "k1":"v1", "hats":14}
for key in a:
    print(key)

for key in a.keys():
    print(key)

# both produce
# k0
# k1
# hats
```

To iterate through all the values in a dictionary you can use any of the following. Note: you can only edit the values with the last of the three methods
```python
for val in a.values():
    print(val)

# v0
# v1
# 14

for key, val in a.items():
    print(key, "-", val)

for key in a:
    print(key, "-", a[key])

# both produce
# k0 - v0
# k1 - v1
# hats - 14
```

## Dict methods

Python provides methods that operate on dicts. For example, `.update()` adds new key:value pairs to the end of a dict:

```python
alpha = {"a":0, "b":1, "c":2}
alpha.update({"d":3, "e":4})
print(alpha) # {"a":0, "b":1, "c":2, "d":3, "e":4}
```

`.clear()` removes all the pairs from a dict:

```python
num = {1:1, 2:4, 3:9, 4:16}
num.clear()
print(num) # {}
```


Note that these methods are void, and they modify the dict in-place. This means that methods like `.update()` will change `alpha`, but you'll be disappointed if you assign it to a variable like `alpha2 = alpha.update()`. (Try it!) 


`.copy()` will copy and return a dictionary that isn't tethered to the original;
```python
a = {"one":"fish", "two":"fish", "red":"fish", "blue":"fish"}
b = a
c = a.copy()
a["blue"] = "cat"
print(a) # {"one":"fish", "two":"fish", "red":"fish", "blue":"cat"}
print(b) # {"one":"fish", "two":"fish", "red":"fish", "blue":"cat"}
print(c) # {"one":"fish", "two":"fish", "red":"fish", "blue":"fish"}
```

## Deleting elements

There are several ways to delete pairs from a dict. If you know the key of the pair you want to remove, you can use `.pop()`. The value will be returned, optionally to prevent an error in the case the key does not exist you can add a second argument as well as the key to return should there be no pair with that key.

```python
abcs = {'a':0, 'b':1, 'c':2}
x = abcs.pop('b')
y = abcs.pop('e', -1)
print(abcs) # {'a':0, 'c':2}
print(x) # 1
print(y) # -1
```

To remove the most recently added/pair at the end of the dictionary you can use `.popitem()`. The key:value pair will be returned as a tuple of (key, value)

```python
abcs = {'a':0, 'b':1, 'c':2}
x = abcs.popitem()
print(abcs) # {'a':0, 'b':1}
print(x) # ('c', 2)
```

Another option is to use `del()`, this is dangerous however as it can lead to key errors if the key does not exist

```python
abcs = {'a':0, 'b':1, 'c':2}
del(abcs['a'])
# del(abcs['z']) # causes an error
print(abcs) # {'b':1, 'c':2}
```
