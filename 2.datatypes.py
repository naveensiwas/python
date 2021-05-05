#Python Numbers
a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a, "is complex number?", isinstance(1+2j,complex))

#Python String 
s = "This is a string"
print(s)

s = "This is a string 1+3j, 323645 3.56"
print(s)

s = '''A multiline
string'''
print(s)

#String slicing
print("s[0:3] = ", s[0:3])
print("s[5:] = ", s[5:])
print("s[0:8] = ", s[0:8])
print("s[:8] = ", s[:8])

#String is immutable
#s[1] = 'n'
#TypeError: 'str' object does not support item assignment

#Python List
a = [1, 2.2, 'python', 1+3j, 'python']
print(a)

#List slicing
b = [5,10,15,20,25,30,35,40]
print("b[2] = ", b[2])
print("b[0:3] = ", b[0:3])
print("b[5:] = ", b[5:])

#Lists are mutable, meaning, the value of elements of a list can be altered.
a = [1, 2, 3]
a[2] = 4
print(a)

#Python Tuple
t = (5,'program', 1+3j, 1.6)
print("t = ", t)

#Tuple slicing
print("t[1] = ", t[1])
print("t[0:3] = ", t[0:3])

#Tuples are immutable
#t[0] = 10
#TypeError: 'tuple' object does not support item assignment

#Python Set
a = {5,2,3,1,4}
print("a = ", a)
print(type(a))

a = {5,2,3,1,4,2,2,2,4,5}
print("a = ", a)
print(type(a))

a = {5,2,"string",3+4j,3.4}
print("a = ", a)
print(type(a))

a = {1,2,3}
#print("a[1] = ", a[1])
#TypeError: 'set' object does not support indexing

#Set slicing
#print("a[1] = ", a[1])
##TypeError: 'set' object does not support indexing

#Python Dictionary
d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);

d = {'key1':'value1','key2':'value2'}
print(type(d))
print("d['key1] = ", d['key1']);
print("d['key2'] = ", d['key2']);

d['key2'] = 'value3'
print("d : ", d)

#Dictionary slicing
d = {'key1':'value1','key2':'value2', 'key3':'value3','key4':'value4', 55 : 66, 77 : 88}
print("d : ", d)
#print("d[0:3] = ", d[0:3])
#TypeError: unhashable type: 'slice'

