# task_1
def with_index(iterable, start=0):  # define a function named "with_index" that takes an iterable and an optional start
    # value as arguments
    for i, item in enumerate(iterable):  # use a for loop with "enumerate" to loop over each item in the iterable and
        # its index
        yield i+start, item  # yield a tuple containing the current index plus the start value, and the current item


people = ['Bobby', 'Kotik', 'Kowalski']
for i, names in with_index(people, start=1):  # use our function to check if it works like enumerate
    print(f'{i}. {names}')

# task_2


def in_range(start, end, step=1):  # create function that takes a start value, an end value, and an optional step value
    # as arguments
    result = []  # create an empty list
    i = start  # set the variable "i" to the start value
    while i < end:  # use a while loop to iterate over the sequence of numbers
        result.append(i)  # append the current value of "i" to empty list
        i += step  # add the step value to "i" to generate the next number in the sequence
    return result


ex = in_range(0, 10, 2)
print(ex)

# task_3


class MyIterable:
    def __init__(self, iterable):  # initializes an instance of MyIterable with an iterable
        self.iterable = iterable

    def __iter__(self):  # method to initialize the current index and return the object itself
        self.current = 0
        return self

    def __next__(self):  # method to iterate over the iterable object, raising a StopIteration exception when it reaches
        # the end
        if self.current < len(self.iterable):
            result = self.iterable[self.current]
            self.current += 1
            return result
        else:
            raise StopIteration

    def __getitem__(self, index):  # method to allow accessing elements using square brackets syntax
        return self.iterable[index]


my_iterable = MyIterable([1, 2, 3, 4, 5])
for element in my_iterable:
    print(element)

print(my_iterable[0])
print(my_iterable[1])
print(my_iterable[3])


