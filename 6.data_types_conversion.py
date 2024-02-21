# Conversion between data types

# Example 1 : Implicit Type Conversion.
num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

# Example 2 : Explicit Type Conversion.
print('float(5) : ', float(5))
print('int(10.6) : ', int(10.6))
print('int(-10.6) : ', int(-10.6))
print('float(2.5) : ', float('2.5'))
print('str(25) : ', str('25'))
# print('int(25) : ', int('25n')) #ValueError: invalid literal for int() with base 10: '25n'

print('set([1,2,3]) : ', set([1, 2, 3]))
print('tuple({5,6,7}) : ', tuple({5, 6, 7}))
print("list('hello') : ", list('hello'))
print('dict([[1,2],[3,4]])', dict([[1, 2], [3, 4]]))
