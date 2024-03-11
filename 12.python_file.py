import os

file_read_dir = os.getcwd() + '/files/read_test.txt'

# Read character by character.
print('>>>> Example - 1 >>>>')
f = open(file_read_dir)
print('Read first 2 character of file : ', f.read(2))
f.close()

# Read first line from file.
print('\n')
print('>>>> Example - 2 >>>>')
f = open(file_read_dir, mode='r', encoding='utf-8')
print('File first line : ', f.readline())
f.close()

# Read all lines from file.
print('\n')
print('>>>> Example - 3 >>>>')
f = open(file_read_dir, mode='r', encoding='utf-8')
print('File all line : ', f.readlines())
f.close()

# Read entire content from file.
print('\n')
print('>>>> Example - 4 >>>>')
with open(file_read_dir, 'r', encoding='utf-8') as f:
    print('File entire content : ', f.read())

# Writing Line by line to File in Python.
print('\n')
print('>>>> Example - 5 >>>>')
file_write_dir = os.getcwd() + '/files/write_test.txt'
with open(file_write_dir, 'w', encoding='utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

# Writing multiple Lines to File in Python.
print('\n')
print('>>>> Example - 6 >>>>')
file_write_dir = os.getcwd() + '/files/write_lines_test.txt'
with open(file_write_dir, 'w', encoding='utf-8') as f:
    f.writelines("Since Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off) "
                 "\nSince Random Access Memory (RAM) is volatile (which loses its data when the computer is turned off)"
                 " \n")
