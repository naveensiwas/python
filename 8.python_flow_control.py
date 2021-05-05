#Example: Python if Statement
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

#Example: if...else
num = 1
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

#Example: if...elif...else
num = 3.4

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

#Example: Python Nested if
num = 10
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

#Example: Python for Loop
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum = 0

for val in numbers:
	sum = sum+val

print("The sum is", sum)

#Example: Python for Loop with range() function
genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
	print("I like", genre[i])

#Example: Python for Loop with if...else condition
student_name = 'Soyuj'
marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')

#Example: Python while Loop
n = 10
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1

print("The sum is", sum)

#Example: Python break
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

#Example: Python continue
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

#Example: pass Statement
'''pass is just a placeholder for
functionality to be added later.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

