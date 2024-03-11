import os

# Example : Get Current Directory.
print('>>>> Example - 1 >>>>')

print('Current working directory : ', os.getcwd())

# Example : Changing Directory.
print('\n')
print('>>>> Example - 2 >>>>')

print('Change directory : ', os.chdir('../../venv'))
print('Current working directory : ', os.getcwd())

# Example : List Directories and Files
print('\n')
print('>>>> Example - 3 >>>>')

print('Change directory : ', os.chdir('bin'))
print('Current working directory : ', os.getcwd())
print('List directories and files : ', os.listdir())
