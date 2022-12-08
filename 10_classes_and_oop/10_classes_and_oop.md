# Classes and OOP

Types like Strings, Lists, and Dictionaries are classes that create objects of that type. In Python you can create your own classes with their own functions and information.

Classes are created with the keyword `class` and variables can be assigned for the entire class like `a` or like `b`:
```python
class ExampleClass():
    # Inside the class's indentation block
    a = "hats"
# Outside the class's indentation block
ExampleClass.b = 23
```
With this `ExampleClass` we can access and change `a` and `b` by calling them with the class:
```python
print(ExampleClass.a) # "hats"
print(ExampleClass.b) # 23
ExampleClass.a = "cheese"
print(ExampleClass.a) # "cheese"
```
In order to create objects from that class you make a constructor which is a special type of function that uses the name `__init__`. Here you will declare variables that will be specific to that object with `self.VARIABLE`.
```python
class Animal():
    # this is a class variable that can be accessed by using the name of the class or any Animal object
    num_animals = 0
    def __init__(self, color, size, name=""):
        Animal.num_animals += 1
        # these are instance variables specific to that object
        self.color = color
        self.size = size
        self.hunger = 5
        if(name == ""):
            self.name = "unnamed"
        else:
            self.name = name

a_anim = Animal("blue", 5, "Shark")
b_anim = Animal("green", 1, "Turtle")
```
Be careful when changing class variables directly. If you change a class variable with the name of the class it will update that variable for all objects. However, if you directly change a class variable with an object, that variable will no longer be bound to the class and will no longer update with the class.
```python
class Examp():
    a = 5
    def __init__(self, b):
        self.b = b
    
examp_a = Examp("hats")
examp_b = Examp("cheese")
print(Examp.a) # 5
print(examp_a.a) # 5
print(examp_b.a) # 5

examp_a.a = 3
Examp.a = 15

print(Examp.a) # 15
# a doesn't get updated to 15 because it was directly edited
print(examp_a.a) # 3 
print(examp_b.a) # 15
```

To have functions for your objects you will do it just as you create methods, except the first argument should always be named `self` which references the object itself and will be used to access instance variables.
```python
class Animal():
    # this is a class variable that can be accessed by using the name of the class or any Animal object
    num_animals = 0
    def __init__(self, color, size, name=""):
        Animal.num_animals += 1
        # these are instance variables specific to that object
        self.color = color
        self.size = size
        self.hunger = 5
        if(name == ""):
            self.name = "unnamed"
        else:
            self.name = name
    
    def print_name(self):
        print("name: " + self.name)
        return
    
    def add_size(self, add):
        self.size += add
        return self.size
    
a_anim = Animal("blue", 5, "Shark")
b_anim = Animal("green", 1, "Turtle")

a_anim.print_name() # name: Shark
print(b_anim.size)
print(b_anim.add_size(3)) # 4
print(a_anim.num_animals) # 2
```
To have functions of the class itself you will need to add the `@classmethod` or the `@staticmethod` decorator before the function. Typically, you will use class methods if you need to access class variables and use static methods if you are just working with parameters. For class methods you will typically use the first parameter as `cls` to represent the class. These methods can be called by the class name or by objects. You cannot access instance variables in class or static methods.
```python
class Student():
    school_name = "CVHS"
    num_students = 0
    def __init__(self, gpa, birthday, name, social_security_num):
        Student.num_students += 1
        self.gpa = gpa
        self.birthday = birthday
        self.name = name
        self.ssn = social_security_num
    
    def add_gpa(self, change):
        self.gpa += change
        return self.gpa

    @classmethod
    def school_stats(cls, extra_message=""):
        print("School name: " + cls.school_name)
        print("Number of students: " + str(cls.num_students))
        if(extra_message != ""):
            print(extra_message)

    @staticmethod
    def is_schoolday(day):
        if day not in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
            return False
        return True
    
student_a = Student(4.2, "Jan 9", "Boris", 5)

print(student_a.is_schoolday("sunday")) # False
Student.is_schoolday("wednesday") # True

Student.school_stats() 
# School name: CVHS
# Number of students: 1

student_b = Student(-2, "Feb 30", "Jada", 0)

student_a.school_stats()
# School name: CVHS
# Num of students: 2
```
There are many other things to know with classes but there are the basics, next time we will go over dunder/magic methods and inheritance probably

If I got any stuff wrong or forgot some stuff write me an angry email or come over and yell at me -Ronan