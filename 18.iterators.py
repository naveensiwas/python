#Example 1 : Iterating Through an Iterator
my_list = [4, 7, 0, 3]
my_iter = iter(my_list)

print('my_iter 1 : ',next(my_iter))
print('my_iter 2 : ',next(my_iter))
print('my_iter 3 : ',next(my_iter))
print('my_iter 4 : ',next(my_iter))

#Example 2 : Building Custom Iterators - An iterator of powers of two.
class PowTwo:

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration

numbers = PowTwo(3)
iter_obj = iter(numbers)

while True:
    try:
        item = next(iter_obj)
        print('Custom iter items :', item)
    except StopIteration:
        break

