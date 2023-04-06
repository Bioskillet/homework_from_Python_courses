# task_1
# перший варіант підглянутий в Інтернеті;
def function_with_variables():  # create a function with our values
    variable1 = 53  # value of type int
    variable2 = [2, 4, 7]  # value of type list
    variable3 = 'Where am I?'  # value of type string
    return variable1, variable2, variable3  # return our values

# using the .__code__.co_nlocals command, check the calculation of variables in the function = 3
print(function_with_variables.__code__.co_nlocals, "the number of local variables declared in a function.")
# task_1 (variant 2)


def function_variables():  # create a function with our values
    var1 = 67  # value of type int
    var2 = [3, 6, 3]  # value of type list
    var3 = "I don't know"  # value of type string
    var4 = {2: 4}  # value of type vocabulary
    return var1, var2, var3, var4  # return our values

# create a function with which we will search for the number of variables in another function
def function_seeker(func):
    list_for_seek = []  # create an empty list
    for variable in func:  # write a loop that will go through another function and write each value to our list
        list_for_seek.append(variable)
    print(len(list_for_seek), "the number of local variables declared in a function.")
    return list_for_seek  # write out the length of our list and return it

# call the function_seeker and pass as an argument the function in which we will look for variables = 4
function_seeker(function_variables())


# task_2
def external_function(parametr):  # create a function in which we will pass a certain parameter
    a = 10  # create the variable a
    print('External function')  # print to see if our external function is working

    def internal_function():  # create an internal function in which we will work
        nonlocal parametr, a  # specify that the parameter and variable must be searched for in the external function
        parametr += 10  # we indicate that 10 should be added to the argument we specify later and 1 to the variable a
        a += 1
        return 5 + a + parametr
    return internal_function


b = external_function(10)  # assign b to our external function and pass the argument 10
print(b())  # 36


# task_3
def choose_func(nums: list, func1, func2):
    if all(num > 0 for num in nums):  # create a function in which we will check our lists for positivity or negativity
        return func1(nums)  # if the list consists of positive numbers, then use the first specified function
    else:
        return func2(nums)  # if the list consists of negative numbers, then use the second specified function


nums1 = [1, 2, 3, 4, 5]  # lists we will work with
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):  # create a function in which we specify as a parameter the list that we will use as an argument
    return[num ** 2 for num in nums]  # return our list with square values


def remove_negatives(nums):
    return [num for num in nums if num > 0]  # the second function should remove negative values from the list


print(choose_func(nums1, square_nums, remove_negatives))  # checking the development with a positive list
print(choose_func(nums2, square_nums, remove_negatives))  # checking the development with a negative list

#assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
#assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]

