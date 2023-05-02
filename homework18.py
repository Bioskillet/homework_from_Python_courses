# task_1
import re  # import module re
from functools import wraps # for task_3


class MyClass:  # initializes an instance of MyClass with an email
    def __init__(self, email):
        self.email = email
        self.validate(email)  # validating the email address using the class method validate()

    @classmethod  # decorator to make validate() a class method
    def validate(cls, email):  # сlass method to validate email addresses
        # regular expression pattern to validate email addresses
        # дуже довго махався з цією штукою. Скористався допомогою товариша :/
        email_regex = r'^[a-zA-Z0-9]+([._-][a-zA-Z0-9]+)*@[a-zA-Z0-9]+([.-][a-zA-Z0-9]+)*\.[a-zA-Z]{2,}$'
        # if the email address doesn't match the pattern raise a ValueError with an error message
        if not re.match(email_regex, email):
            raise ValueError('Invalid email address')
        else:  # otherwise prints our email
            print(email)

# пояснення дій для себе: ^[a-zA-Z0-9]+: початок рядка. Починається з будь-якої комбінації малих і великих літер
# латинського алфавіту та цифр, довжина якої дорівнює 1 або більше символів
# ([._-][a-zA-Z0-9]+)*: дозволяє використовувати символи ".", "_", "-" як роздільники між символами. Перевіряємо, чи
# існує будь-яка кількість таких символів, за якою знову йде одна або більше літера або цифра
# @: роздільник між локальною та доменною частинами
# [a-zA-Z0-9]+: доменна частина повинна містити одну або більше літеру або цифру
# ([.-][a-zA-Z0-9]+)*: дозволяє використовувати символи ".", "-" як роздільники між символами доменної частини
# Перевіряємо, чи існує будь-яка кількість таких символів, за якою знову йде одна або більше літера або цифра
# \.[a-zA-Z]{2,}$: кінець рядка. Завершується крапкою, після якої йде дві або більше літери (наприклад, .com, .edu)


MyClass.validate('abc-d@mail.com')
# MyClass.validate('abc-@mail.com')
MyClass.validate('abc.def@mail.com')
# MyClass.validate('abc..def@mail.com')


# task_2
class Boss:  # initializes an instance of Boss with an id_, name, company. _workers is also created as an empty list
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property  # create a property called workers that returns the value of the _workers instance variable
    def workers(self):
        return self._workers

    def add_worker(self, worker):  # create method which adds a new worker to the _workers list for this Boss instance
        if isinstance(worker, Worker):  # checks whether worker object is an instance of the Worker class
            self._workers.append(worker)  # if it is, it appends it to the _workers list
        else:
            raise ValueError("Value must be an instance of Worker")  # if it is not, it raises a ValueError


class Worker:  # initializes an instance of Worker with an id_, name, company and _boss
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property  # create a property called boss that returns the value of the _boss instance variable
    def boss(self):
        return self._boss

    @boss.setter  # create a setter method for the boss property
    def boss(self, value):
        if isinstance(value, Boss):  # checks whether a value is an instance of the Boss class
            self._boss = value  # if it is, it sets the _boss instance variable to that value
        else:
            raise ValueError("Value must be an instance of Boss")  # if it is not, it raises a ValueError


boss1 = Boss(1, "John Doe", "ABC Inc.")
boss2 = Boss(2, "Jane Smith", "XYZ Corp.")
worker1 = Worker(11, "Mike Johnson", "ABC Inc.", boss1)
worker2 = Worker(12, "Lisa Brown", "ABC Inc.", boss1)
print("Boss1 name:", boss1.name)
print("Worker1's boss name:", worker1.boss.name)
boss1.add_worker(worker2)
print("Workers for boss1:", [worker.name for worker in boss1.workers])


class TypeDecorators:
    @staticmethod
    def to_int(func):  # a static method that takes in a function and returns a new function that converts its output to
        # an integer
        @wraps(func)
        def wrapper(*args, **kwargs):  # defines a wrapper function for the input function
            result = func(*args, **kwargs)
            try:
                return int(result)
            except (ValueError, TypeError):
                return result  # # trying to convert the result to an integer, and if it fails, it returns the original
                # result

        return wrapper

    @staticmethod  # a static method that takes in a function and returns a new function that converts its output to a
    # string
    def to_str(func):
        @wraps(func)  # defines a wrapper function for the input function
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return str(result)

        return wrapper

    @staticmethod  # a static method that takes in a function and returns a new function that converts its output to a
    # boolean
    def to_bool(func):
        @wraps(func)  # defines a wrapper function for the input function
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, str):  # checks if the result is a string, and if it is, it returns True if the
                # lowercase version of the result is in a list of accepted string values
                return result.lower() in ['true', '1', 't', 'y', 'yes']
            return bool(result)  # if the result is not a string, it returns the boolean value of the result

        return wrapper

    @staticmethod  # a static method that takes in a function and returns a new function that converts its output to a
    # float.
    def to_float(func):
        @wraps(func)  # defines a wrapper function for the input function
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:  # trying to convert the result to a float, and if it fails, it returns the original result.
                return float(result)
            except (ValueError, TypeError):
                return result

        return wrapper


@TypeDecorators.to_int  # applies the to_int decorator to the do_nothing function, which returns the input string
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool  # applies the to_bool decorator to the do_something function, which returns the input string as
# a boolean
def do_something(string: str):
    return string


print(do_nothing('25'))
print(do_something('True'))

# assert do_nothing('25') == 25
# assert do_something('True') is True

