# Challenges

## Challenge 1: Two Beggars And Gold
In the field, two beggars A and B found some gold at the same time. They all wanted the gold, and they decided to use simple rules to distribute gold:

1. They divided gold into *n* piles. 
2. They took turns to take away a pile of gold from the far left or the far right.
3. The beggar always chooses the bigger pile.
4. If the both sides are equal, take the left pile.

Given an integer array `golds`, and assuming that A always takes first, calculate the final amount of gold obtained by A and B. Return a two-element array `[A_amount, B_amount]`.

```
Example
For golds = [4,2,9,5,2,7], the output should be [14,15].

Left-most pile is 4, 
Right-most pile is 7, 
A takes 7

Left-most pile is 4, 
Right-most pile is 2, 
B takes 4

Left-most pile is 2, 
Right-most pile is 2, 
A takes 2

Left-most pile is 9, 
Right-most pile is 2, 
B takes 9

Left-most pile is 5, 
Right-most pile is 2, 
A takes 5

Then, there is only 1 pile left, 
B takes 2

A: 7 + 2 + 5 = 14
B: 4 + 9 + 2 = 15
```

## Challenge 2: English beggars

Given an array of values and an amount of beggars, return an array with the sum of what each beggar brings home, assuming they all take regular turns, from the first to the last. For example: `[1,2,3,4,5]` for 2 beggars will return a result of `[9,6]`, as the first one takes `[1,3,5]`, the second collects [`2,4]`. The same array with 3 beggars would have in turn have produced a better out come for the second beggar: `[5,7,3]`, as they will respectively take `[1,4]`, `[2,5]` and `[3]`.

## Challenge 3: Josephus 

This is based on a tale by ancient historian Josephus. According to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege. Refusing to surrender to the enemy, they instead opted for mass suicide with a twist: they formed a circle and proceeded to kill one man every three, until one last man was left (and he it was supposed to kill himself to end the act). As Josphus lived to tell the tale, you may have correctly guessed that they didn't exactly follow through the original idea. 

### Part 1: Survivor 

Assume that *n* people are put into a circle and that they are eliminated in steps of *k* elements. Create a function called `josephus_survivor(n, k)` that returns the survivor. You may assume that both n and k will always be >=1.

```
Example
josephus_survivor(7,3) # 7 people, one every 3 is eliminated
[1,2,3,4,5,6,7]        # initial sequence
[1,2,4,5,6,7]          # 3 is counted out
[1,2,4,5,7]            # 6 is counted out
[1,4,5,7]              # 2 is counted out
[1,4,5]                # 7 is counted out
[1,4]                  # 5 is counted out
[4]                    # 1 is counted out, 
                       # 4 is the last element - the survivor!
```

### Part 2: Permutation

Create a function called `josephus_permutation(n, k)` that returns a Josephus permutation. More information is on the [Josephus Problem](https://en.wikipedia.org/wiki/Josephus_problem) wikipedia page.

```
Example
josephus_permutation(7,3) # final result is [3,6,2,7,5,1,4]
[1,2,3,4,5,6,7]           # initial sequence
[1,2,4,5,6,7]             # 3 is counted out and goes into the result [3]
[1,2,4,5,7]               # 6 is counted out and goes into the result [3,6]
[1,4,5,7]                 # 2 is counted out and goes into the result [3,6,2]
[1,4,5]                   # 7 is counted out and goes into the result [3,6,2,7]
[1,4]                     # 5 is counted out and goes into the result [3,6,2,7,5]
[4]                       # 1 is counted out and goes into the result [3,6,2,7,5,1]
[]                        # 4 is counted out and goes into the result [3,6,2,7,5,1,4]
```
