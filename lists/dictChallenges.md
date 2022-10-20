# Challenges

## Challenge 1: Key replacement
Write a function that will take a dictionary, the old key, and a new key as inputs. Edit the dictionary in place such that the new key will replace the old key while still retaining the same value.

```python
a = {1:"first", 2:"second", 3:"third"}
keyReplace(a, 1, 0)
print(a) # {0:"first", 2:"second", 3:"third"}
```

## Challenge 2: value:key pairs
Write a function that takes a dictionary and returns a new dictionary that has the keys and values swapped.
```python
a = {1:"first", 2:"second", 3:"third"}
b = swap(a)
print(b) # {"first":1, "second":2, "third":3}
```

## Challenge 3: Patronage
Results are in, given a dictionary of voters names as keys and who they voted for as values, find the winner of the election and return a list of all the people who voted for them. If it is a tie return an empty list.
```python
a = {"James":"James", "George":"James", "Jesse":"Jesse", "Person A":"Person B", "Chansey":"Jesse", "Viney":"James", "Person B":"Person A"}
print(patronage(a)) # ["James", "George", "Viney"]
```

## Challenge 4: ??? pt. 1 ???
Write a function that takes arguments of a dictionary and three strings: `a, b, and c`, determine the number of times `c` appears in the values of `a` and `b` in the dictionary assuming `a` and `b` exist as keys in the dictionary
```python
wknss = {"a":"aabbbccc", "b":"c", "c":"ccaaa","d":"aabb"}
print(wknss_finder(wknss), "a", "b", "c") #  4
print(wknss_finder(wknss), "c", "d", "c") # 2
print(wknss_finder(wknss), "c", "d", "a") # 5 
```