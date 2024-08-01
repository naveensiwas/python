# Python Local Variables
# Example : 1
print('>>>> Example - 1 >>>>')


def greet():
    msg_hello = 'Hello'
    print('Local variable : ', msg_hello)


greet()

# try to access message variable
# print(msg_hello) #NameError: name 'msg_hello' is not defined


# Python Global Variables
# Example : 1
print('\n')
print('>>>> Example - 2 >>>>')

# declare global variable
msg_hi = 'Hi'


def greet_one():
    print('Local variable : ', msg_hi)


greet_one()
print('Global variable : ', msg_hi)

# Example : 2
print('\n')
print('>>>> Example - 3 >>>>')

# declare global variable

msg_bye = 'Bye'


def greet_two():
    print('Local variable : ', msg_bye)
    # msg_bye = 'Bye Bye' #UnboundLocalError: local variable 'msg_bye' referenced before assignment


greet_two()

# Example : 3
print('\n')
print('>>>> Example - 4 >>>>')
# declare global variable
msg_bye_bye = 'Bye Bye'
print('Global variable before update : ', msg_bye_bye)


def greet_three():
    global msg_bye_bye
    msg_bye_bye = 'Bye Bye Updated'
    print('Updated Global variable : ', msg_bye_bye)


greet_three()
