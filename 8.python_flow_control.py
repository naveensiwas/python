# Example 1: Python if Statement
print('>>>> Example - 1 >>>>')
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

# Example 2: if...else
print('\n')
print('>>>> Example - 2 >>>>')
num = 1
if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")

# Example 3: if...elif...else
print('\n')
print('>>>> Example - 3 >>>>')
num = 3.4

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# Example 4: Python Nested if
print('\n')
print('>>>> Example - 4 >>>>')
num = 10
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

# Example 5: Python for Loop
print('\n')
print('>>>> Example - 5 >>>>')
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]
sum_of_num = 0

for val in numbers:
    sum_of_num = sum_of_num + val

print("The sum is", sum_of_num)

# Example 6: Python for Loop with range() function
print('\n')
print('>>>> Example - 6 >>>>')
genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print("I like", genre[i])

# Example 7: Python for Loop with if...else condition
print('\n')
print('>>>> Example - 7 >>>>')
student_name = 'Soyuj'
marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')

# Example 8: Python while Loop
print('\n')
print('>>>> Example - 8 >>>>')
n = 10
sum_of_num = 0
i = 1

while i <= n:
    sum_of_num = sum_of_num + i
    i = i + 1

print("The sum is", sum_of_num)

# Example 9: Python break
print('\n')
print('>>>> Example - 9 >>>>')
for val in "string":
    if val == "i":
        break
    print(val)

print("The end")

# Example 10: Python continue
print('\n')
print('>>>> Example - 10 >>>>')
for val in "string":
    if val == "i":
        continue
    print(val)

print("The end")

# Example 11: pass Statement
print('\n')
print('>>>> Example - 11 >>>>')
'''pass is just a placeholder for
functionality to be added later.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
