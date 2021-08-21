#Example 1 : A simple generator function.
def my_generator():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

my_gen = my_generator()

print('my_gen 1 : ',next(my_gen))
print('my_gen 2 : ',next(my_gen))
print('my_gen 3 : ',next(my_gen))

#Example 2 : Python Generator Expression.
my_list = [1, 3, 6, 10]

# square each term using list comprehension
list_ = [x**2 for x in my_list]

# same thing can be done using a generator expression
# generator expressions are surrounded by parenthesis ()
generator_ = (x**2 for x in my_list)

print('list_ :', list_)

print(generator_)
print('generator_ 1 : ',next(generator_))
print('generator_ 2 : ',next(generator_))
print('generator_ 3 : ',next(generator_))
print('generator_ 4 : ',next(generator_))

