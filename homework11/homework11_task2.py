import json
import sys

# витратив неочікувано багато часу та сил, але якось це подолав (не без невеличкої допомоги, буду відвертим).
# Хотілось ще багато чого реалізувати, однак занадто багато часу вже й на це витратив :/


our_file = sys.argv[1]  # we indicate that our variable will take a value
# (in our case, the name of the file) from the terminal


def user_input():  # the main function in which we give the user a choice of actions by calling other functions
    while True:  # create an eternal loop that will allow the user to forge actions until he exits the program
        user_choice = input('Choose a number from 1 to 10 or q if you want to exit:\n '
                            '1. Open the contact list;\n '
                            '2. Add a new contact;\n '
                            '3. Search for a contact by first name;\n '
                            '4. Search for a contact by last name;\n '
                            '5. Search for a contact by full name;\n '
                            '6. Search for a contact by phone number;\n '
                            '7. Search for a contact by city;\n '
                            '8. Search for a contact by state;\n '
                            '9. Delete a contact by phone number;\n '
                            '10. Update contact by phone number;\n '
                            'q. End the program.\n ')
        if user_choice == '1':  # when selecting 1, we call the function of reading our file
            contact_list(our_file)
        elif user_choice == '2':  # when selecting 2, we call the function of adding a new dictionary to our file
            add_contact(our_file)
        elif user_choice == '3':  # when selecting 3, call the search function in our dictionary file by the first name
            search_firstname(our_file)
        elif user_choice == '4':  # when selecting 4, call the search function in our dictionary file for the last name
            search_lastname(our_file)
        elif user_choice == '5':  # when selecting 5, call the search function in our dictionary file by the full name
            search_fullname(our_file)
        elif user_choice == '6':  # when selecting 6, we call the search function in our dictionary file by phone number
            search_number(our_file)
        elif user_choice == '7':  # when selecting 7, call the search function in our dictionary file by city
            search_city(our_file)
        elif user_choice == '8':  # when selecting 8, call the search function in our dictionary file by state
            search_state(our_file)
        elif user_choice == '9':  # when selecting 9, we call the function of searching our dictionary file by number
                                    # and deleting the dictionary with this number
            contact_delete(our_file)
        elif user_choice == '10':  # when selecting 10, we call the search function in our dictionary file by number
                                    # and then update one of its values
            contact_update(our_file)
        elif user_choice == 'q':  # when selecting q, terminate the program due to a break
            break
        else:  # output this print if a character was entered that is not in the list of available ones
            print("An invalid character was entered. You should only use numbers from 1 to 10 or q.")


def contact_list(given_file):  # function in which we open a file and read it
    with open(given_file, 'r') as file_object:
        print(file_object.read())


def add_contact(given_file):  # a function in which we ask the user for the data we need
    phonebook = {'first name': '', 'last name': '', 'full name': '', 'phone number': '', 'city': '', 'state': ''}
    first_name = input('Enter your first name: ').lower()  # data is accepted and written in lower case
    phonebook['first name'] = first_name  # transfer the entered data to the required key in our dictionary
    last_name = input('Enter your last name: ').lower()
    phonebook['last name'] = last_name
    full_name = first_name + ' ' + last_name
    phonebook['full name'] = full_name
    phone_number = input('Enter your phone number: ')
    if phone_number.isdigit() and len(phone_number) == 12:  # check that the entered number consists of only 12 numbers
        phonebook['phone number'] = phone_number  # add the entered number to the dictionary if it fulfills the
                                                    # condition
    else:  # if the condition is not met, we cause an error in the program,
                # indicating that the number was entered incorrectly
        assert phone_number.isdigit() and len(phone_number) == 12, 'The phone number can be up to 12 digits long! ' \
                                                                   'Please try again!'
    city = input('Enter your city: ').lower()
    phonebook['city'] = city
    state = input('Enter your state: ').lower()
    phonebook['state'] = state
    with open(f'{given_file}', 'r') as file_object:  # open the file and add our new information dictionary to it
        contact = json.load(file_object)
        contact['phonebook'].append(phonebook)
        with open(f'{given_file}', 'w') as file_:
            json.dump(contact, file_, indent=3)
            print('Contact added successfully!')


def search_firstname(given_file):  # create a function to search for a contact by the first name entered by the user
    firstname = input('Enter the first name by which you want to find the contact: ').lower()
    with open(f'{given_file}', 'r+') as file_object:  # open our json file in which we will search
        inform = json.load(file_object)
        number_of_contact = 0
        for key in inform['phonebook']:  # tell the key to go through the values of our dictionary
            if key['first name'] == firstname:  # if the key finds the required value, then we display this contact
                print(inform['phonebook'][number_of_contact])
            else:
                number_of_contact += 1
            if number_of_contact == len(inform['phonebook']):  # if no matches were found, print this
                print("This first name is not in your contact list")


def search_lastname(given_file):  # create a function to search for a contact by the last name entered by the user
    lastname = input('Enter the last name by which you want to find the contact: ').lower()
    with open(f'{given_file}', 'r+') as file_object:  # open our json file in which we will search
        inform = json.load(file_object)
        number_of_contact = 0
        for key in inform['phonebook']:  # tell the key to go through the values of our dictionary
            if key['last name'] == lastname:  # if the key finds the required value, then we display this contact
                print(inform['phonebook'][number_of_contact])
            else:
                number_of_contact += 1
            if number_of_contact == len(inform['phonebook']):  # if no matches were found, print this
                print("This last name is not in your contact list")


def search_fullname(given_file):  # create a function to search for a contact by the full name entered by the user
    fullname = input('Enter the full name by which you want to find the contact: ').lower()
    with open(f'{given_file}', 'r+') as file_object:  # open our json file in which we will search
        inform = json.load(file_object)
        number_of_contact = 0
        for key in inform['phonebook']:  # tell the key to go through the values of our dictionary
            if key['full name'] == fullname:  # if the key finds the required value, then we display this contact
                print(inform['phonebook'][number_of_contact])
            else:
                number_of_contact += 1
            if number_of_contact == len(inform['phonebook']):  # if no matches were found, print this
                print("This full name is not in your contact list")


def search_number(given_file):  # create a function to search for a contact by the phone number entered by the user
    number = input('Enter the number by which you want to find the contact: ')
    if number.isdigit() and len(number) == 12:  # check whether the entered string consists of 12 numbers
        with open(f'{given_file}', 'r+') as file_object:  # open our json file in which we will search
            inform = json.load(file_object)
            number_of_contact = 0
            for key in inform['phonebook']:  # tell the key to go through the values of our dictionary
                if key['phone number'] == number:  # if the key finds the required value, then we display this contact
                    print(inform['phonebook'][number_of_contact])
                else:
                    number_of_contact += 1
                if number_of_contact == len(inform['phonebook']):  # if no matches were found, print this
                    print("This number is not in your contact list")
    else:  # if something else is entered instead of 12 numbers, we cause an error in which we indicate this
        assert number.isdigit() and len(number) == 12, 'The phone number can be up to 12 digits long! ' \
                                                                   'Please try again!'


def search_city(given_file):  # create a function to search for a contact by the city entered by the user
    city_search = input('Enter the city by which you want to find the contact: ').lower()
    with open(f'{given_file}', 'r+') as file_object:  # open our json file in which we will search
        inform = json.load(file_object)
        number_of_contact = 0
        for key in inform['phonebook']:  # tell the key to go through the values of our dictionary
            if key['city'] == city_search:  # if the key finds the required value, then we display this contact
                print(inform['phonebook'][number_of_contact])
            else:
                number_of_contact += 1
            if number_of_contact == len(inform['phonebook']):  # if no matches were found, print this
                print("This city is not in your contact list")


def search_state(given_file):  # create a function to search for a contact by the state entered by the user
    state_search = input('Enter the state by which you want to find the contact: ').lower()
    with open(f'{given_file}', 'r+') as file_object:  # open our json file in which we will search
        inform = json.load(file_object)
        number_of_contact = 0
        for key in inform['phonebook']:  # tell the key to go through the values of our dictionary
            if key['state'] == state_search:  # if the key finds the required value, then we display this contact
                print(inform['phonebook'][number_of_contact])
            else:
                number_of_contact += 1
            if number_of_contact == len(inform['phonebook']):  # if no matches were found, print this
                print("This state is not in your contact list")


def contact_delete(given_file):  # create a function in which we search for a contact by the specified number and
                                                            # delete it
    number_search = input('Enter the number you want to delete the contact: ')
    if number_search.isdigit() and len(number_search) == 12:  # we do another check on 12 numbers
        with open(f'{given_file}', 'r+') as file_object:  # open our json file in which we will search
            inform = json.load(file_object)
            number_of_contact = 0
            for key in inform['phonebook']:  # tell the key to go through the values of our dictionary
                if key['phone number'] == number_search:  # if the key finds the required value,
                                                            # then remove the contact from our dictionary
                    inform['phonebook'].pop(number_of_contact)
                else:
                    number_of_contact += 1
            with open(f'{given_file}', 'w') as file_:  # output the changes to our dictionary
                json.dump(inform, file_, indent=3)
                if number_of_contact == len(inform['phonebook']):  # if no matches were found, print this
                    print("This number is not in your contact list")
    else:  # if the condition is not met, we cause an error in the program,
                # indicating that the number was entered incorrectly
        assert number_search.isdigit() and len(number_search) == 12, 'The phone number can be up to 12 digits long! ' \
                                                                   'Please try again!'
        print('Contact deleted successfully!')


def contact_update(given_file):  # create a function in which we search for a contact by number
                                            # and update the required value
    number1 = input('Enter the number you want to update the contact: ')
    if number1.isdigit() and len(number1) == 12:  # check for 12 numbers
        with open(f'{given_file}', 'r+') as file_object:  # open our json file in which we will search
            inform = json.load(file_object)
            number_of_contact = 0
            for key in inform['phonebook']:  # tell the key to go through the values of our dictionary
                if key['phone number'] == number1:  # if the key finds the required value,
                                                    # then we display options for the user that he can edit
                    choice_user = input('Choose what you want to update or write something to finish the update :\n '
                                        '1. First name;\n'
                                        '2. Last name;\n'
                                        '3. Phone number;\n'
                                        '4. City;\n'
                                        '5. State.\n')
                    if choice_user == '1':  # instead of the existing first name,
                                                # write the new value entered by the user
                        key['first name'] = input('Specify the first name with which you '
                                                  'want to replace the existing one ').lower()
                    elif choice_user == '2':  # instead of the existing last name,
                                                # write the new value entered by the user
                        key['last name'] = input('Specify the last name with which you '
                                                'want to replace the existing one ').lower()
                    elif choice_user == '3':  # instead of the existing number, write the new value entered by the user
                        new_number = input('Specify the number to which you want to replace the existing one ')
                        if new_number.isdigit() and len(new_number) == 12:  # but before that we check for 12 numbers
                            key['phone number'] = new_number
                        else:  # in case of non-execution of the body, we raise an error
                            assert new_number.isdigit() and len(new_number) == 12, 'The phone number can be up to 12 ' \
                                                                                   'digits long! Please try again!'
                    elif choice_user == '4':  # instead of the existing city, write the new value entered by the user
                        key['city'] = input('Specify the city with which you want to replace the existing one ').lower()
                    elif choice_user == '5':  # instead of the existing state, write the new value entered by the user
                        key['state'] = input('Specify the state with which you want '
                                             'to replace the existing one ').lower()
                    else:
                        number_of_contact += 1
                if number_of_contact == len(inform):
                    print("This number is not in your contact list")
            with open(given_file, 'w') as file_:
                json.dump(inform, file_, indent=3)
    else:
        assert number1.isdigit() and len(number1) == 12, 'The phone number can be up to 12 digits long! ' \
                                                                   'Please try again!'
        print('Contact successfully updated!')


if __name__ == '__main__':
    user_input()
