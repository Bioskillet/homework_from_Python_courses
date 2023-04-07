# task_1

# create an external decorator function in which we specify the function that we will decorate as a parameter
def logger(func):
    # create an internal decorator function in which we specify an unclear number of values as a parameter
    def inner(*args):
        func(*args)  # we indicate that our decorated function takes the values that will be given as arguments
        # print the name of the function we are working with and the arguments we specified
        print(f'{func.__name__} called with {args}')
    return inner


@logger  # decorate our function
def add (x,y):  # create a function that takes x and y as parameters
    return x + y


@logger  # decorate our function
def square_all(*args):  # create a function that will accept an unclear number of values
    return [arg ** 2 for arg in args]  # return the squares of our values


add(4, 5)  # call our decorated functions
square_all(4, 5)
# task_2

def stop_words(words: list):  # create a function in which we pass a list of our stop words as a parameter
    def decor(functi):  # create an internal function whose parameter will be the function we are decorating
        # create another internal function in which the main work will be done and specify the name
        # that will be given as an argument
        def decor2(nam):
            value_string = functi(nam).split()  # break our sentence into a list and assign a new value to it
            for i in range(len(value_string)):  # point to our and walk the length of our list
                for j in words:  # tell our j to take the value of our list of forbidden words
                    # indicate that if a word from our list is equal to a stop word, then replace it with *
                    if value_string[i] == j:
                        value_string[i] = '*'
            return ' '.join(value_string)  # return our list again as a string
        return decor2
    return decor



@stop_words(['pepsi','BMW'])  # decorate our function and specify a list of stop words
def create_slogan(name:str)->str:  # create a function with a name parameter in a sentence
    return f'{name} drinks pepsi in his brand new BMW !'

print(create_slogan('Steve'))  # print our decorated function with name Steve



# task_3
# create an external function with the necessary parameters
def arg_rules(type_: type, max_length: int, contains: list):
    def decor(func):  # create an internal function that will take the decorated function as a parameter
        def res(name_check):  # create another internal function that will take the name to be checked as a parameter
            error_list = []  # create an empty list
            # specify if the length of the recorded name is longer than the one specified in the decorator,
            # then add the string to the empty list
            if len(name_check) > max_length:
                error_list.append(f'The length of the "{name_check}" is greater than {max_length}')
            if type(name_check) != type_:  # make it similar to the top if
                error_list.append(f'The type of the "{name_check}" no match type {type_}')
            result = 0
            # create a loop in which we specify to go through the list of necessary characters in the word
            for i in contains:
                if i in name_check:  # if the character is in our word, add 1 to our variable
                    result += 1
            # if our variable is not equal to the length of our list, then add it to our error list
            if result != len(contains):
                error_list.append(f'{name_check} does not consist of {contains}')
            if error_list:  # indicate that if our list is not empty, then print it
                print(*error_list, sep='\n')
                return False
            return func(name_check)
        return res
    return decor


@arg_rules(type_=str, max_length=15, contains=['05', '@'])  # decorate our function with the arguments we need
def create_slogan(name: str) -> str:  # create a function that we will decorate with a name parameter
    return f"{name} drinks pepsi in his brand new BMW"


print(create_slogan('johndoe05@gmail.com'))
print(create_slogan('S@SH05'))