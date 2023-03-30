# # task_1
# # enter a sentence, transform it into a list in lower case and split it into words
# words_list = input('Write your sentence: ').lower().split()
# our_dict = dict()  # create a dictionary in advance to add our words to
# for word in words_list:  # create a loop in which we tell the variable to go through our list
#     if word in our_dict:  # set a condition if the word is in our dictionary, then add +1 to the value
#         our_dict[word] += 1
#     else:  # if the word is not in our dictionary, then write it as a new key with a value of 1
#         our_dict |= {word: 1}
# print(our_dict)  # output our dictionary

# task_2
# write the specified data to the dictionaries
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
elements = dict()  # create a dictionary in which we will add our values
total_price = int()  # create a variable in which we will display our result
for i in stock:  # create a loop in which we specify a variable and go through our keys-values
    elements[i] = (stock[i] * prices[i])  # specify that the elements variable takes the multiplied
                                            # values of the other two dictionaries
# create a loop in which we tell j to go through all the values in the dictionary and add them to each other
for j in elements:
    total_price += elements[j]
print(total_price)  # print the total price of stock

# task_3
# create a list consisting of tuples, in which one element takes a value from 1 to 10, and the other is its square
our_list = [(i, i**2) for i in range(1, 11)]
print(our_list)  # output our list

# task_4
# create a list of days of the week
# week_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
# create a dictionary in which the days of the week will be the keys, and their sequence number will be the value
week_dictionary ={1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
# create an inverted pre-dictionary
week_reverse_dictionary = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4,
                           "Friday": 5, "Saturday": 6, "Sunday": 7}
# create a term that is divided into days and converted into a list
week_list = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()
# option to create a dictionary through a loop
week_dict_loop = dict()  # create a dictionary in advance to add our words to
i = 0
for day in week_list:  # create a loop in which we tell the variable to go through our list
    i += 1
    week_dict_loop |= {day: i}  # specify that each iteration of the day is written with a key with value 0
# option to create a reverse dictionary through a loop
week_reversedict_loop = dict()  # create a dictionary in adance to add our words to
# create a loop in which we tell the variable to go through our list and their index
for number, day1 in enumerate(week_list):
    number += 1  # add +1 to the day's index
    # add the sequence number of the day as a key and the day as a value to our list
    week_reversedict_loop |= {number: day1}
week_dict_generator = {numberday+1:day3 for (numberday,day3) in enumerate(week_list)}
print(week_list, week_dictionary, week_reverse_dictionary, week_dict_loop, week_reversedict_loop,
      week_dict_generator, sep='\n')