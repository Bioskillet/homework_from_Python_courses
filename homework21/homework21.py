import logging  # import module logging


class CustomOpen:  # create a CustomOpen class for working with files
    counter = 0  # initialize the counter as a class attribute

    def __init__(self, file, mode):  # initializes an instance of Worker with a file and mode
        self.file = file
        self.mode = mode

    def __enter__(self):  # method which is called when entering the block with
        self.file_obj = open(self.file, self.mode)  # open the file with the transferred parameters
        CustomOpen.counter += 1  # increase the value of the counter variable by 1
        logging.info(f"Opened file '{self.file}' in mode '{self.mode}'.")  # log about opening the file
        return self.file_obj

    def __exit__(self, exc_type, exc_value, traceback):  # method which is called when exiting the block with
        self.file_obj.close()  # close the file
        logging.info(f"Closed file '{self.file}'.")  # log about closing the file

        if exc_type is not None:  # if an error occurs, log about it and return False
            logging.error(f"Exception '{exc_type.__name__}: {exc_value}' occurred.")
            return False

        return True  # if there were no errors, return True


logging.basicConfig(level=logging.INFO)  # initialize logging

with CustomOpen("example.txt", "w") as file:  # open the file for writing and write data to it
    file.write("Hello, world!")

with CustomOpen("example.txt", "r") as file:  # open the file for reading and read data from it
    contents = file.read()
    print(contents)
# output the number of times the file was opened. In our case, 2 times
print(f"The file was opened {CustomOpen.counter} times.")





