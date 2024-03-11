# Example 1 : Slicing for positive index.
print('>>>> Example - 1 >>>>')
colors = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print('colors[0] : ', colors[0])
print('colors[1] : ', colors[1])
print('colors[5] : ', colors[5])

# Example 2 : Slicing for positive index.
print('\n')
print('>>>> Example - 2 >>>>')
print('colors[2:5] : ', colors[2:5])
print('colors[2:] : ', colors[2:])
print('colors[:4] : ', colors[:4])

# Example 3 : Slicing for negative index.
print('\n')
print('>>>> Example - 3 >>>>')
print('colors[-1] : ', colors[-1])
print('colors[-2] : ', colors[-2])
print('colors[-5] : ', colors[-5])

# Example 4 : Slicing for negative index.
print('\n')
print('>>>> Example - 4 >>>>')
print('colors[-5:-2] : ', colors[-5:-2])
print('colors[-2:] : ', colors[-2:])
print('colors[:-4] : ', colors[:-4])

# Example 5 : Taking n first elements of a list
print('\n')
print('>>>> Example - 5 >>>>')
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print('nums[:5] : ', nums[:5])

# Example 6 : Taking n last elements of a list
print('\n')
print('>>>> Example - 6 >>>>')
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print('nums[-3:] : ', nums[-3:])

# Example 7 : Taking all but n last elements of a list
print('\n')
print('>>>> Example - 7 >>>>')
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print('nums[:-2] : ', nums[:-2])

# Example 8 : Taking every nth-element of a list.
print('\n')
print('>>>> Example - 8 >>>>')
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# If we want to have only every 2-nd element of nums.
print('nums[::2] : ', nums[::2])

# We omit start/stop parameters and use only step.
print('nums[1::2] : ', nums[1::2])

# If we don’t want to include some elements at the end, we can also add the stop parameter.
print('nums[1:-3:2] : ', nums[1:-3:2])  # Exclude last 3 elements from list.

# Example 9 : Using Negative Step and Reversed List.
print('\n')
print('>>>> Example - 9 >>>>')
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# We can use a negative step to obtain a reversed list
print('nums[::-1] : ', nums[::-1])

# So, we start from the -2 element (value 80) and go from right to left collecting all the elements in a reversed list.
# We can use stop value to stop taking before some element. E.g., let’s not include 20 and 10 values:
print('nums[-2::-1] : ', nums[-2::-1])
print('nums[-2:1:-3] : ', nums[-2:1:-3])
