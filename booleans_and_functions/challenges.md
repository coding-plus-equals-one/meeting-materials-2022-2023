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
