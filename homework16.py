# task_1

class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.age)

    def __repr__(self):
        return self.first_name + ' ' + self.last_name


class Teacher(Person):

    def __init__(self, first_name, last_name, age, salary, subject):
        super().__init__(first_name, last_name, age)
        self.salary = salary
        self.subject = subject

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.age) + ' ' + str(self.salary) + ' ' + self.subject



class Student(Person):

    def __init__(self, first_name, last_name, age, student_class):
        super().__init__(first_name, last_name, age)
        self.student_class = student_class

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + str(self.age) + ' ' + str(self.student_class)


person = Person('Kuzma', 'Kuzmich', 28)
teacher = Teacher('Bogdan', 'Kulbaba', 64, 12000, 'Physic')
student = Student('Vasya', 'Pupkin', 17, 11)
print(person.__str__())
print(teacher.__str__())
print(student.__str__())
print(person.__repr__())
print(teacher.__repr__())
print(student.__repr__())

# task_2

class Mathematician:

    def square_nums(self, numbers_list):
        self.numbers_list = numbers_list
        new_numbers_list = []
        for number in self.numbers_list:
            new_numbers_list.append(number ** 2)
        return new_numbers_list

    def remove_positives(self, numbers_list):
        self.numbers_list = numbers_list
        new_number_list = []
        for number in self.numbers_list:
            if number < 0:
                new_number_list.append(number)
        return new_number_list

    def filter_leaps(self, numbers_list):
        self.numbers_list = numbers_list
        new_number_list = []
        for number in self.numbers_list:
            if number % 400 == 0 or number % 4 == 0:
                new_number_list.append(number)
        return new_number_list



m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

# task_3
# довго намагався вирішити задачу сам, але довелося просити допомоги


class Product:
    # A class for products
    def __init__(self, types, name, price):
        # Constructor to initialize a Product object with type, name, and price attributes
        self.type = types
        self.name = name
        self.price = price
        self.income = 0


class ProductStore:
    # A class for a store that sells products
    def __init__(self):
        # Constructor to initialize a ProductStore object with an empty product list, income, and product info
        self.product_list = []
        self.income = 0
        self.info = ()

    def add(self, product, amount):
        # Method to add a product to the store's product list, or increment the quantity of an existing product
        for item in self.product_list:
            # Loop through the product list
            if product.name == list(item.keys())[0]:
                # If the product name matches an existing product in the list
                item[product.name][0] += amount
                # Increment the product quantity
                return
        self.product_list.append({product.name: [amount, product.type, product.price * 1.3]})
        # Otherwise, add a new product to the product list with its quantity, type, and price

    def set_discount(self, identifier, percent, identifier_type='name'):
        # Method to set a discount for a product by name or type
        for i in self.product_list:
            # Loop through the product list
            if identifier in i:
                # If the identifier matches a product name or type in the list
                i[identifier][2] *= (100-percent)/100
                # Calculate the new discounted price
        print(self.product_list)

    def sell_product(self, product_name, sell_amount):
        # Method to sell a product and increment the store's income
        for i in self.product_list:
            # Loop through the product list
            if product_name in i:
                # If the product name matches an existing product in the list
                if sell_amount < i[product_name][0]:
                    # If there is enough quantity of the product in the store
                    i[product_name][0] -= sell_amount
                    # Decrement the product quantity
                    self.income += sell_amount * i[product_name][2]
                    # Increment the store's income
                else:
                    raise ValueError("You don't have enough product to sell.")
                    # Otherwise, raise an error that there isn't enough quantity to sell
                return

    def get_income(self):
        # Method to get the store's current income
        print(self.income)
        return self.income

    def get_all_products(self):
        # Method to get a list of all products in the store
        print(self.product_list)
        return self.product_list

    def get_product_info(self, product_name):
        # Method to get information on a specific product by name
        for i in self.product_list:
            # Loop through the product list
            if product_name in i:
                # If the product name matches an existing product in the list
                self.info = (product_name, i[product_name][0])
                # Get the product name and quantity
                print(self.info)
                return self.info


p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()
s.add(p, 10)
s.add(p2, 300)
s.add(p, 20)
s.add(p, 10)
s.get_product_info('Football T-Shirt')
s.sell_product('Ramen', 10)
s.set_discount('Ramen',50)
assert s.get_product_info('Ramen') == ('Ramen', 290)
print(s.product_list)

# task_4


class CustomException(Exception):  # Declaration of a class named CustomException that inherits from the Exception class
    def __init__(self, msg):  # Declaration of an __init__ method with a parameter named msg
        self.msg = msg  # Assigning the value of the msg parameter to an attribute named msg of the object
        self.error = f"Custom exception occurred: {msg}"  # Creating a string with an error message that includes
    # the msg argument
        with open("logs.txt", "a") as file_object:  # Opening the logs.txt file in append mode with an alias file_object
            file_object.write(self.error + "\n")  # Writing the error message to the logs.txt file
        super().__init__(self.error)  # Calling the constructor of the base class Exception with the self.error argument


# try:
#     # some code that may raise an exception
#     raise CustomException(NameError("Something went wrong with name"))  # Creating an object of the CustomException
#     # class with a NameError object as an argument and raising an exception
# except CustomException as eror:  # Handling the exception if it occurs
#     print('An error occurred:', eror)  # Printing the error message to the screen

try:
    raise CustomException("Something went wrong with value")  # Creating an instance of the CustomException class and
    # raising it as an exception
except CustomException as eror:  # Handling the exception if it occurs
    print('An error occurred:', eror)  # Printing the error message to the screen
