def oops():  # create the oops function
    raise IndexError  # explicitly raise an error in it IndexError

def catch_function():  # create a function in which we use a try/except block and call the oops function in it
    try:  # point to the oops check function
        oops()
# if we do not specify the expected error, then regardless of what error the oops function will cause,
# except will still be triggered
    except KeyError:
        print('I think, it"s wrong answer')  # specify the text that will be called instead of the error

catch_function()  # call the second function

def your_numbers():  # create a function in which we request two variables from the user
    a = int(input('Еnter a number in the variable a '))
    b = int(input('enter a number in the variable b '))
    print(a, b)  # print the numbers a and b
    return (a**2)/b  # return them as specified in the task, which we will use for further error checking

try:  # create a try/except block in which we call our function
    your_numbers()
# specify what will be displayed instead of an error when the user enters a character other than a number
except ValueError:
    print('You can enter only numbers!')
# specify what will be displayed instead of an error when the user enters 0 in the variable b
except ZeroDivisionError:
    print("You can't divide by zero!")
