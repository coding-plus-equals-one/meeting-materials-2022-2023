# Exercises from the Notes

## Exercise 1: Check Parity

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

``` python
def get_parity(num):
    pass # replace pass with your code
```

## Exercise 2: Count Vowels

Return the number (count) of vowels (a, e, i, o, u) in the given string. The input string will only consist of lower case letters and/or spaces.

``` python
def get_vowel_count(phrase):
    pass # replace pass with your code
```

## Exercise 3: Multiples of 3 or 5

Create a function called `multiples_sum` with a parameter called `num`. Find the sum of all the multiples of 3 or 5 below `num` and return it. Additionally, if `num` is negative, return 0. Remember to test the function!

``` python
def get_multiples_sum(num):
    pass # replace pass with your code
```

# Challenges

## Challenge 1: Remove the Trolls!

Trolls are attacking your comment section! A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat. Write a function that takes a string and return a new string with all vowels removed. For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

``` python
def cleanse_text(phrase):
    pass # replace pass with your code
```

## Challenge 2: Fizz Buzz
Fizz Buzz is a popular programming problem that purportedly filters out 99.5% of programming job candidates. Let's see how you guys fare. Here is how the problem goes:

Write a program that prints the numbers from 1 to 100. But for multiples of three, print “Fizz” instead of the number, and for the multiples of five, print “Buzz”. For numbers which are multiples of both three and five, print “FizzBuzz”.

Here is the pattern for the first 36 numbers:

1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, Fizz Buzz, 16, 17, Fizz, 19, Buzz, Fizz, 22, 23, Fizz, Buzz, 26, Fizz, 28, 29, Fizz Buzz, 31, 32, Fizz, 34, Buzz, Fizz, ...

Hint: use `end=", "` so that each print statement ends with a comma and a space instead of a newline.

``` python
print("1", end=", ")
print("2", end=", ")
```

## Challenge 3: Square Each Digit
Square every digit of a number and concatenate them. For example, if the input of the function is 9119, return 811181. Have the function accept an integer and return an integer.

``` python
def square_digits(num):
    pass # replace pass with your code
```

## Challenge 4: Make Bricks

We want to make a row of bricks that is _goal_ units long. We have a number of small bricks (1 unit each) and big bricks (5 units each). Return True if it is possible to make the goal by choosing from the given bricks. You can start with this function template:

``` python
def make_bricks(goal, small, big):
    pass # replace pass with your code
```

Here are some tests:
``` python
make_bricks(3, 1, 8)
>>> True
make_bricks(3, 1, 9)
>>> False
make_bricks(3, 2, 10)
>>> True
```
