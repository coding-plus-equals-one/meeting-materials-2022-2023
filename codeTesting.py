class ExampleClass():
    a = "hats"
    b = 13

    def __init__(self, c, d):
        self.c = c
        self.d = d
        self.e = 5
        print(self.a)

    def set_a(self, a_):
        #local var a rather than instance or class
        a = a_

    @staticmethod
    def set_class_a(a_):
        ExampleClass.a = a_

test_thing = ExampleClass(1,2)

print(test_thing.a)
print(ExampleClass.a)
print()

ExampleClass.a = "sphere"

print(test_thing.a)
print(ExampleClass.a)
print()

test_thing.a = "cows"

print(test_thing.a)
print(ExampleClass.a)
print()

test_thing.set_a("cheese")

print(test_thing.a)
print(ExampleClass.a)
print()

test_thing.u = 5

print(test_thing.u)

ExampleClass.i = 65
print(ExampleClass.i)
print(test_thing.i)

ExampleClass.a = "fin"

print(test_thing.a)
print(ExampleClass.a)
print()

test_thing.set_class_a("cheese")

print(test_thing.a)
print(ExampleClass.a)
print()