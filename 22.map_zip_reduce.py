# Python map() Function
# The map() function executes a given function to each element of an iterable (such as lists, tuples, etc.)
# The map() applies the function it receives as an argument to each element in a sequence and returns the resulting -
# sequence.


# Example : 1
numbers = [1, 2, 3, 4]


def square(number):
    return number * number


# apply square() to each item of the numbers list
squared_numbers = map(square, numbers)
print('squared_numbers : ', squared_numbers, ' == ', list(squared_numbers))

# Example : 2
# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print('Double all numbers : ', list(result))

# Example : 3
# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print('Add two lists : ', list(result))

# Python zip() Function
# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and returns it.

# Example : 1
languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print('ZIP Example-1 :', list(result))

# Example : 2
names = ['Mukesh', 'Roni', 'Ankit']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    print('ZIP Example-2 :', i, name, age)


# Python reduce() Function
# The reduce() applies the function to the elements of the sequence, from left to right, starting with the first two -
# elements in the sequence.

# Example : 1
def my_add(num_1, num_2):
    sum_result = num_1 + num_2
    print('Sum Result {} + {} = {}'.format(num_1, num_2, sum_result))
    return sum_result


from functools import reduce
numbers_list = [0, 1, 2, 3, 4]
total = reduce(my_add, numbers_list)
print('Total : ', total)
