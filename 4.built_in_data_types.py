# Python frozenset()

# Example 1: frozenset() for Tuple
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The empty frozen set is:', frozenset())
print('frozen set  type : ', type(fSet))
print('Tuple frozen set is : ', fSet)

# frozenset is immutable
# fSet.add('v')
# AttributeError: 'frozenset' object has no attribute 'add'

# Example 2: frozenset() for Dictionary
person = {"name": "John", "age": 23, "sex": "male"}
fSet = frozenset(person)
print('Dictionary frozen set is:', fSet)

# Example 3: frozenset() for List
list1 = [1, 2, 3, 4, 5, 8, 9, 5, 6, 7]
fSet = frozenset(list1)
print('List frozen set is:', fSet)

# Example 4: frozenset() for Set
set1 = {1, 2, 3, 4, 5, 8, 9, 5, 6, 7}
fSet = frozenset(set1)
print('Set frozen set is:', fSet)

# Frozenset operations
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()
print('copying a frozenset : ', C)

# union
print('union :', A.union(B))

# intersection
print('intersection : ', A.intersection(B))

# difference
print('difference : ', A.difference(B))

# symmetric_difference
print('symmetric_difference : ', A.symmetric_difference(B))

# Python range()

# Example 1 : Range
print(list(range(0)))
print(list(range(10)))
print(list(range(1, 10)))

# Example 2 : Range
start = 2
stop = 14
step = 2
print(list(range(start, stop, step)))

# Example 3 : print()
print('This sentence is output to the screen')

a = 5
print('The value of a is', a)

# Example 4 : Output formatting
x = 5
y = 10
print('The value of x is {} and y is {}'.format(x, y))

print('I love {0} and {1}'.format('bread', 'butter'))
print('I love {1} and {0}'.format('bread', 'butter'))

# Example 5 : Python Input
num = input('Enter a number: ')
print('You have entered : ', num)

# Example 6 : Python Import
import math

print(math.pi)

# Example 7 : Python package path.
import sys

print('Your sys path : ', sys.path)
