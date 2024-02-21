#Example 1 : A simple closure function.
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

times_3 = make_multiplier_of(3)
times_5 = make_multiplier_of(5)

print(times_3(9))
print(times_5(3))
print(times_5(times_3(2)))

#Example 2 : A simple decorators function.
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")

# call ordinary() function.
ordinary()

#let's decorate this ordinary function.
pretty = make_pretty(ordinary)
pretty()

#Example 3 : @ symbol along with the name of the decorator function.
@make_pretty
def ordinary():
    print("I am ordinary function as decorator function")
    
# call ordinary() function as decorator function.
ordinary()    

#Example 4 : @ symbol along with the name of the decorator function with parameters.
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)

divide(4, 2)
