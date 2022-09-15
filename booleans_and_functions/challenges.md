## Exercise 1: Coding Club Pitch

This was the code we used for our flyers. There is something slightly off about it. Copy and paste it into `main.py` and then try the following: 

1. Run the code.
2. Set `coding = True` on the first line. Run the code.
3. Set `coding = False` again. Remove the line `coding += 1`. Run the code. 
4. Replace the line `coding += 1` with `coding = True`. Run the code.

What does `False + 1` evaluate to?

``` python
coding = False

def coding_club_pitch(coding):
    if not coding:
        print("Don't worry, no experience is needed.")
        coding += 1
        coding_club_pitch(coding)
    else:
        print("Join the coding club!")
        print("Thurs and Fri after school in Room 752.")

coding_club_pitch(coding)
```

## Challenge 1: What's greatest?

Write a function that takes three numbers as arguments(A, B, and C) and returns the place of the number that is the greatest among the group. If A is greatest return "The first", if A and B are equal and greatest return "Multiple are greatest"

## Challenge 2: Mini Mad Libs

Write a function that takes 3 arguments and uses them in place of the words "blue", "fish", and "two" in the rhyme "one fish, two fish, red fish, blue fish"

## Challenge 3: In bounds

Write a function that takes a height and width of a graph and x and y values of a point. Return `True` if the x and y values are within the map, if they are off the map, return `False`

## Challenge 4: On the map

Travellers keep getting lost wandering in the middle of nowhere. Given a map of a certain height and width and certain x and y coordnates check if there is a town at those coornates. There are towns at every location where the x and y coordnates added together equal a number divisible by 5 and where either x or y is even. There are no towns beyond the height and width of the map.

```python
def on_the_map(width, height, x, y):
    # Write code here
    # return True if there is a town at (x,y)
    # return False if there is not a town at (x,y)
```

