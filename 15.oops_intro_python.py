# Example 1: Creating Class and Object in Python
print('>>>> Example - 1 >>>>')


class Parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))


# Example 2: Creating Methods in Python
print('\n')
print('>>>> Example - 2 >>>>')


class Parrot:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing".format(self.name)


blu = Parrot("Blu", 10)
print(blu.sing("'Happy'"))
print(blu.dance())


# Example 3: Constructors Destructors in Python
print('\n')
print('>>>> Example - 3 >>>>')


class Employee:

    def __init__(self):
        print('Employee created.')

    def __del__(self):
        print('Destructor called, Employee deleted.')


obj = Employee()
