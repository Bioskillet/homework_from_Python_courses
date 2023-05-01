# task_1
# define the Animal class with an init method that takes a name parameter and sets it as an instance variable.
class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):  # define a talk method that raises a NotImplementedError.
        raise NotImplementedError('Must be implemented by a sub class.')


class Cat(Animal):  # define the Cat class that extends the Animal class.

    def talk(self):  # override the talk method to print 'Meow!'
        print('Meow!')


class Dog(Animal):  # define the Dog class that extends the Animal class.

    def talk(self):  # override the talk method to print 'Woof - woof! Gav - gav!'
        print('Woof - woof! Gav - gav!')

# define a function called animal_talk that takes an Animal object and calls its talk method.
def animal_talk(animal: Animal):
    animal.talk()


dog = Dog('Brodyaga')
cat = Cat('Barsik')

animal_talk(dog)
animal_talk(cat)

# task_2


class Library:

    def __init__(self, name):  # initializes an instance of Library with a name and empty lists of books and authors.
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name: str, year: int, author):
        book = Book(name, year, author)  # creates a new Book object with the given name, year, and author.
        self.books.append(book)  # adds the book to the Library's list of books
        if author not in self.authors:
            self.authors.append(author)  # adds the author to the Library's list of authors if they're not already in it
        author.add_book(book)  # adds the book to the author's list of books
        return book

# returns a list of Book objects in the Library that have the given Author object as their author.
    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

# returns a list of Book objects in the Library that have the given year as their publication year.
    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f'Library {self.name}'

    def __str__(self):
        return f'{self.name} library'


class Book:
    num_of_books = 0  # a class variable that keeps track of the number of books.

    def __init__(self, name, year, author):  # initializes an instance of Book with a name, year, and author.
        self.name = name
        self.year = year
        self.author = author
        self.author.add_book(self)  # adds the book to the author's list of books.
        Book.num_of_books += 1  # increments the class variable num_of_books.

    def __str__(self):
        return f'{self.name}, {self.year}, {self.author.name}'

    def __repr__(self):
        return f'Book ({self.name}, {self.year}, {self.author})'


class Author:
    # all_authors = []
# Initializes an instance of Author with a name, country, birthday, and empty list of books.
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []
        # Author.all_authors.append(self)

    def add_book(self, book):  # adds the given Book object to the author's list of books.
        self.books.append(book)

    def __repr__(self):
        return f'Author ({self.name}, {self.country}, {self.birthday})'

    def __str__(self):
        return f'{self.name}, {self.country}, {self.birthday}'


library = Library('Library of Karazhan')
author1 = Author('Christie Golden', 'USA', 'November 21, 1963')
author2 = Author('William King', 'USA', 'December 7, 1959')
author3 = Author('Greg Weisman', 'USA', 'September 28, 1963')
book1 = library.new_book('Arthas: Rise of the Lich King', 2009, author1)
book2 = library.new_book('Illidan', 2016, author2)
book3 = library.new_book('War Crimes', 2014, author1)
book4 = library.new_book('Traveler', 2016, author3)

print(library.books)
print(library.authors)
print(book1)
print(book2)
print(book3)
print(book4)
print(library.group_by_author(author1))
print(library.group_by_year(2016))
print(library.authors)

# task_3


class Fraction:
    def __init__(self, numerator, denominator):  # initializes an instance of Fraction with a numerator and denominator.
        if denominator == 0:  # if the denominator is 0, then raise an ValueError.
            raise ValueError("Denominator cannot be zero.")
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, other):  # set the operator + new properties.
        # calculate the sum of two fractions by cross-multiplying and adding the numerators,
        # then multiplying the denominators.
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):  # set the operator - new properties.
        # calculates the difference of two fractions by cross-multiplying and subtracting the numerators,
        # then multiplying the denominators.
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):  # set the operator * new properties.
        # calculates the product of two fractions by multiplying the numerators and denominators.
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):  # set the operator / new properties.
        if other.numerator == 0:  # if the numerator of the second fraction is zero, the ValueError is raised.
            raise ValueError("Cannot divide by zero.")
        # calculates the quotient of two fractions by multiplying the first numerator by the second denominator and
        # multiplying the first denominator by the second numerator.
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):  # set the operator == new properties.
        # return True if the two fractions are equal, as determined by comparing their numerators and denominators.
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __lt__(self, other):  # set the operator < new properties.
        # return True if the current fraction is less than another fraction determined by comparing their
        # numerators and denominators.
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):  # set the operator <= new properties.
        # return True if the current fraction is less than or equal to another fraction determined by comparing their
        # numerators and denominators.
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):  # set the operator > new properties.
        # return True if the current fraction is greater than another fraction determined by comparing their
        # numerators and denominators.
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):  # set the operator >= new properties.
        # return True if the current fraction is greater than or equal to another fraction determined by comparing their
        # numerators and denominators.
        return self.numerator * other.denominator >= other.numerator * self.denominator

    def __str__(self):
        if self.numerator == 0:  # if the numerator is zero, "0" is returned instead.
            return "0"
        else:
            # returns a string representation of the fraction in numerator/denominator form.
            gcd = self.gcd(self.numerator, self.denominator)
            return f"{self.numerator // gcd}/{self.denominator // gcd}"

    def gcd(self, a, b):
        while b:  # returns the greatest common divisor of two numbers a and b using the Euclidean algorithm.
            a, b = b, a % b
        return a


if __name__ == "__main__":
    x = Fraction(1, 2)
    y = Fraction(1, 4)
    z = Fraction(2, 4)
    print(x + y)  # 3/4
    print(x - y)  # 1/4
    print(x * y)  # 1/8
    print(x / y)  # 2/1
    print(x == y)  # False
    print(x == z)  # True
    print(x < y)  # False
    print(x <= y)  # False
    print(x > y)  # True
    print(x >= y)  # True
    print(str(x))  # 1/2
