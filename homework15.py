# task_1
class Person:  # create a class

    def __init__(self, firstname, lastname, age):  # initialize our instance attributes
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):  # create a method that, when called, will display a sentence with the used attributes
        print(f"Hello, my name is {self.firstname} {self.lastname} and I'm {self.age} years old")


persona = Person('Carl', 'Johnson', 26)  # create an instance with the specified attributes
persona.talk()  # call the talk method to our instance

# task_2


class Dog:  # create a class in which to pass the class attribute
    age_factor = 7

    def __init__(self, dog_age):  # initialize our instance attributes
        self.dog_age = dog_age

# create a method that will return the dog's age multiplied by a class attribute that shows the ratio of dog
    # to human age
    def human_age(self):
        return self.dog_age * Dog.age_factor


doge = Dog(10)  # create an instance to which we pass the dog's age attribute
print(doge.human_age())  # call the method to the created instance

# task_3

CHANNELS = ['BBC', 'Discovery', 'TV1000']  # channel list


class TVController:  # create a class
    # initialize the instance attributes, indicating that our initial channel starts from scratch
    def __init__(self, channels, channel_current=0):
        self.channels = channels
        self.channel_current = channel_current

    def first_channel(self):  # create a method that returns the first channel from the list
        return self.channels[0]

    def last_channel(self):  # create a method that returns the last channel from the list
        return self.channels[-1]

    def turn_channel(self, number_channel):  # create a method that will return the specified channel
        self.number_channel = number_channel  # initialize the instance attribute
        # we indicate that if the specified number is greater than the length of the channel list or less than zero,
        # then an error is thrown
        if self.number_channel > len(self.channels) or self.number_channel <= 0:
            raise IndexError
        # we specify the key to go through the tuple from 0 to the value of the length of our list
        for key in range(len(self.channels)):
            # if the value of key + 1 is equal to the entered number, then return the list item with the key index
            if (key+1) == number_channel:
                return self.channels[key]
        # варіант з якого починав, але зрозумів, що ідея погана. Вирішив залишити
        # if number_channel == 1:
        #     return self.channels[0]
        # elif number_channel == 2:
        #     return self.channels[1]
        # elif number_channel == 3:
        #     return self.channels[2]
        # else:
        #     raise IndexError

    def next_channel(self):  # create a method that will include the previous channel from the list
        self.channel_current += 1  # add +1 to the value of our current channel
        # indicate that if the number of our current channel is equal to the length of the channel list,
        # then assign the current channel a value of 0
        if self.channel_current == len(self.channels):
            self.channel_current = 0
        return self.channels[self.channel_current]

    def previous_channel(self):  # create a method that will include the previous channel from the list
        self.channel_current -= 1  # subtract 1 from the value of our current channel
        # if the value of our current channel is -1, then we assign it the value of the length of our list - 1
        if self.channel_current == -1:
            self.channel_current = len(self.channels) - 1
        return self.channels[self.channel_current]

    def current_channel(self):  # create a method that displays the name of the current channel
        return self.channels[self.channel_current]  # return an item from the list by the index of the current channel

    # create a method that shows us whether the channel number and name are in the channel list
    def is_exist(self, number_string):
        self.number_string = number_string  # initialize the attribute of our instance
        # if the entered number is in a tuple from 1 to the value of the length of our list +1, then return "yes"
        if self.number_string in range(1, len(self.channels) + 1):
            return 'Yes'
        elif self.number_string in self.channels:  # if the entered channel name is in our list, then return its name
            return self.number_string
        else:  # in any other case print "no"
            return 'No'


controller = TVController(CHANNELS)  # create an instance in which to pass our list as an attribute
print(controller.next_channel(), controller.previous_channel())
print(controller.current_channel())
print(controller.is_exist('Abuba'))











