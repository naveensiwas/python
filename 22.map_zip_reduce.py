# Python map() Function
# map() function: This function applies a given function to each item of an iterable and returns a -
# - new iterable with the results.

# Example : 1
print('>>>> MAP Example - 1 >>>>')
numbers = [1, 2, 3, 4]


def square(number):
    return number * number


# apply square() to each item of the numbers list
squared_numbers = map(square, numbers)
print('squared_numbers {} : '.format(numbers), squared_numbers, ' == ', list(squared_numbers))

# Example : 2
print('\n')
print('>>>> MAP Example - 2 >>>>')

# Double all numbers using map and lambda
numbers = (1, 2, 3, 4)
result = map(lambda x: x + x, numbers)
print('Double all numbers {} : '.format(numbers), list(result))

# Example : 3
print('\n')
print('>>>> MAP Example - 3 >>>>')

# Add two lists using map and lambda
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
result = map(lambda x, y: x + y, numbers1, numbers2)
print('Add two lists ({} + {}) : '.format(numbers1, numbers2), list(result))

# Python zip() Function
# zip() function: This function takes one or more iterables and aggregates them into a single iterable of tuples.

# Example : 1
print('\n')
print('>>>> ZIP Example - 1 >>>>')

languages = ['Java', 'Python', 'JavaScript']
versions = [14, 3, 6]

result = zip(languages, versions)
print('Aggregate two lists ({} + {}) elements : '.format(languages, versions), list(result))

# Example : 2
print('\n')
print('>>>> ZIP Example - 2 >>>>')

names = ['Mukesh', 'Roni', 'Ankit']
ages = [24, 50, 18]

for i, (name, age) in enumerate(zip(names, ages)):
    print('Aggregate two lists ({} + {}) elements : '.format(names, ages), i, name, age)

# Python reduce() Function
# The reduce() function takes a function and an iterable and applies the function to the first two elements,
# then to the result and the next element, and so on, until all elements have been processed.
# The result is a single value.

# Example : 1
print('\n')
print('>>>> REDUCE Example - 1 >>>>')


def my_add(num_1, num_2):
    sum_result = num_1 + num_2
    print('Sum Result {} + {} = {}'.format(num_1, num_2, sum_result))
    return sum_result


from functools import reduce
numbers_list = [0, 1, 2, 3, 4]
total = reduce(my_add, numbers_list)
print('Total : ', total)
