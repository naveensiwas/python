#Example : Catching Exceptions in Python
import sys
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)

    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
    

#Example : Python try... except... finally
import sys
randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)

    except:
        print("Oops!", sys.exc_info()[0], "occurred.")

    finally:
        print('It will always execute')

#Example : User-Defined Exception in Python
class Error(Exception):
    """Base class for other exceptions"""
    pass

class ValueTooSmallError(Error):
    """Raised when the input value is too small"""
    pass

class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass
number = 10

while True:
    try:
        i_num = int(input("Enter a number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break

    except ValueTooSmallError:
        print("This value is too small, try again!")

    except ValueTooLargeError:
        print("This value is too large, try again!")

print("Congratulations! You guessed it correctly.")

