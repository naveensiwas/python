# Example 1: Use of Inheritance in Python
print('>>>> Example - 1 >>>>')


# Parent class
class Bird:

    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")


# Child class
class Penguin(Bird):

    def __init__(self):
        # Call parent class Constructor.
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")


peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()

# Example 2: Data Encapsulation in Python
print('\n')
print('>>>> Example - 2 >>>>')


class Computer:

    def __init__(self):
        self.__max_price = 900

    def sell(self):
        print("Selling Price: {}".format(self.__max_price))

    def setMaxPrice(self, price):
        self.__max_price = price


c = Computer()
c.sell()

# change the price
c.__max_price = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

# Example 3: Using Polymorphism in Python
print('\n')
print('>>>> Example - 3 >>>>')


class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")


class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")


# common interface
def flying_test(bird):
    bird.fly()


# instantiate objects
blu = Parrot()
peggy = Penguin()

# passing the object
flying_test(blu)
flying_test(peggy)
