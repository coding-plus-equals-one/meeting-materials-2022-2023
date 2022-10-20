# Exercise 1: Check Parity
def get_parity(num):
  if (num % 2 == 0):
    return "Even"

  return "Odd"
print(get_parity(23))  # Odd
print(get_parity(92))  # Even

# Exercise 2: Count Vowels
def get_vowel_count(phrase):
  s = "aeiou"
  count = 0
  for char in s:
    for char2 in phrase:
      if char == char2:
        count += 1
  return count  
    


phrase = "supercalifragilisticexpialidocious"
vowel_count = get_vowel_count(phrase)
print(vowel_count)

# Exercise 3: Multiples of 3 or 5
def get_multiples_sum(num):
  total = 0
  if num < 0:
    return 0
  else:
    for i in range(0, num):
      if i % 3 == 0 or i % 5 == 0:
        total += i
  return total


multiples_sum = get_multiples_sum(1000)
print(multiples_sum)


# Challenge 1: Remove the Trolls!
def cleanse_text(phrase):
  s = "aeiouAEIOU"
  s2 = ""
  for char in phrase:
    vowel = 0
    for char2 in s:
      if char != char2:
        vowel += 1
    if vowel == 10:
      s2 += char
  return s2
    

print(cleanse_text("This website is for losers LOL!"))
  
      
      

# Challenge 2: Fizz Buzz

def fizz_buzz():
  s = ""
  for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
      s += "Fizz Buzz"
    elif (i % 3 == 0):
      s += "Fizz"
    elif (i % 5 == 0):
      s += "Buzz"
    else: 
      s += str(i)
    s += ", "

  print(s)

fizz_buzz()
      
    
  

# Challenge 3: Square Each Digit
def square_digits(num):
  s = ""
  num_string = str(num)
  num_length = len(num_string)
  for i in num_string:
    s += str(int(i)**2)

  return int(s)
    

  
print(square_digits(9119))
  

# Challenge 4: Make Bricks
def make_bricks(small, big, goal):
  

  while(goal > 0 and (small != 0 or big != 0)):
    strike = False
    
    if big > 0:
      goal -= 5
      big -= 1
      print(goal)
      if goal < 0:
        strike = True
        goal += 5
        big += 1
    
    elif small > 0:
      goal -= 1
      small -= 1
      print(goal)
    elif strike:
      break
  
  print(goal)

  if goal == 0:
    return True
  else:
    return False
  

print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))
print(make_bricks(1, 3, 14))
print(make_bricks(3, 1, 3))


