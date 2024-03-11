# Example of a function
print('>>>> Example - 1 >>>>')


def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")


greet('Naveen')
print(greet.__doc__)

# Example of a function with return
print('\n')
print('>>>> Example - 2 >>>>')


def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


print(absolute_value(2))
print(absolute_value(-4))

# Example of a function with argument
print('\n')
print('>>>> Example - 3 >>>>')


def greet(name, msg):
    """This function greets to
    the person with the provided message"""
    print("Hello", name + ', ' + msg)


greet("Monica", "Good morning!")

# 2 keyword arguments
greet(name="Bruce", msg="How do you do?")

# 2 keyword arguments (out of order)
greet(msg="How do you do?", name="Bruce")

# Example of Python Arbitrary Arguments
print('\n')
print('>>>> Example - 4 >>>>')


def greet(*names):
    """This function greets all
    the person in the names tuple."""

    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John")
greet(["Monica", "Luke", "Steve", "John"])
greet({"Monica", "Luke", "Steve", "John"})

# Python *args
print('\n')
print('>>>> Example - 5 >>>>')


def adder(*num):
    sum_of_num = 0

    for n in num:
        sum_of_num = sum_of_num + n

    print("Sum:", sum_of_num)


adder(3, 5)
adder(4, 5, 6, 7)
adder(1, 2, 3, 5, 6)

# Python **kwargs
print('\n')
print('>>>> Example - 6 >>>>')


def intro(**data):
    print("Data type of argument:", type(data))

    for key, value in data.items():
        print("{} is {}".format(key, value))


intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)

# Example of Python Pass statement.
print('\n')
print('>>>> Example - 7 >>>>')


def empty_function():
    pass


# Example of Lambda Function in python.
print('\n')
print('>>>> Example - 8 >>>>')
double = lambda x: x * 2
print(double(5))

# Example of Lambda Function in python with filter()
print('\n')
print('>>>> Example - 9 >>>>')
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x % 2 == 0), my_list))
print(new_list)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: x * 2, my_list))
print(new_list)

# Example of Lambda Function in python with map()
print('\n')
print('>>>> Example - 10 >>>>')
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: (x % 2 == 0), my_list))
print(new_list)

my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2, my_list))
print(new_list)

# Example of Python List Comprehension
print('\n')
print('>>>> Example - 11 >>>>')
# Using loop
h_letters = []

for letter in 'human':
    h_letters.append(letter)
print(h_letters)

# List Comprehension
print('\n')
print('>>>> Example - 12 >>>>')
h_letters = [letter for letter in 'human']
print(h_letters)

# Conditionals in List Comprehension
print('\n')
print('>>>> Example - 13 >>>>')
number_list = [x for x in range(20) if x % 2 == 0]
print(number_list)
