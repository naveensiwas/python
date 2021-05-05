
# Example 1
x = "Python"
y = "Python"

print('id(x) : ', id(x))
print('id(y) : ', id(y))
print('String is Immutable : ', id(x) == id(y))


#Example 2
a = 50
print('id(a) : ', id(a))
print('type(a) : ', type(a))

b = "Holberton"
print('id(b) : ', id(b))
print('type(b) : ', type(b))

#Example 3
l1 = [1, 2, 3]
l2 = [1, 2, 3]

print('id(l1) : ', id(l1))
print('id(l2) : ', id(l2))
print('List is Immutable : ', id(l1) == id(l2))

#Example 4
s1 = {1, 2, 3}
s2 = {1, 2, 3}

print('id(s1) : ', id(s1))
print('id(s2) : ', id(s2))
print('Set is Immutable : ', id(s1) == id(s2))

