# task_1
def to_power(x, exp):
    if exp < 0:  # check if the exponent is negative
        raise ValueError('This function works only with exp > 0.')  # if exp < 0, raise ValueError
    elif exp == 0:  # check if the exponent is 0
        return 1  # if exp == 0, return 1
    else:
        return x * to_power(x, exp - 1)


print(to_power(2, 2))  # 4
# print(to_power(2, -1))  # error
# print(to_power(2, 0))  # 1
# task_2


def is_palindrome(stringe):
    if len(stringe) <= 1:  # check if the length of the string is < or = 1
        return True  # if it is, return True
    elif stringe[0].lower() != stringe[-1].lower():  # check if the first character in lowercase is not equal to the
        # last character in lowercase
        return False  # if it is, return False
    else:
        return is_palindrome(stringe[1:-1])  # if the first and last characters are equal, recursively check the
        # substring without the first and last characters


print(is_palindrome('Tut'))  # True
# print(is_palindrome('tut'))  # True
# print(is_palindrome('t'))  # True
# print(is_palindrome('tipet'))  # False
# print(is_palindrome('tipek'))  # False
# task_3


def mult(a, n):
    if a < 0 or n < 0:  # check if either a or n is negative
        raise ValueError('This function works only with positive integers.')  # If either of them is negative, raise a
        # ValueError
    elif a == 0 or n == 0:  # check if a and n is 0
        return 0  # if it is, return 0
    else:
        return a + mult(a, n - 1)


print(mult(2, 5))  # 10
# print(mult(-1, 5))  # error
# print(mult(2, -1))  # error
# print(mult(2, 0))  # 0
# print(mult(0, 2))  # 0
# task_4


def reverse(stringe):
    if len(stringe) <= 1:  # check if the length of the string is <= 1
        return stringe  # if it is, return str
    else:
        return reverse(stringe[1:]) + stringe[0]  # recursively reverse the substring starting from the second character
        # append the first character at the end of the reversed substring


print(reverse('Hello!'))  # !olleH
# print(reverse('o'))  # o
# task_5


def sum_of_digits(dig):
    if not dig.isdigit():  # check if the input string contains non-digit characters
        raise ValueError('Input string must be digit string')  # if it is, raise ValueError
    elif len(dig) == 1:  # check if the length of the string is 1
        return int(dig)  # if it is, return the int value
    else:
        return int(dig[0]) + sum_of_digits(dig[1:])  # convert the first character to an integer and add it to the sum
        # of digits in the substring starting from the second character


print(sum_of_digits('27'))  # 9
# print(sum_of_digits('test'))  # error




















