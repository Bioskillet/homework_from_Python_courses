def full_name(first, last):  # create a function that accepts parameters of the first and last name
    return first.title() + ' ' + last.title()  # return the given arguments of the first and last name with the first
    # letter capitalized and the following ones in lower case


def squares(l):  # create a function that accepts a list
    l2 = []  # create an empty list
    for num in l:  # loop through the given list and square each number, adding it to the empty list
        l2.append(num**2)
    return l2
