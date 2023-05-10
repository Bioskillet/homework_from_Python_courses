# task_1
# class Stack:
#
#     def __init__(self):
#         self.items = []  # initialize the Stack class with an empty list to store items
#
#     def isempty(self):  # check if the stack is empty by comparing the length of items to zero
#         return len(self.items) == 0
#
#     def push(self, item):  # add an item to the top of the stack by appending it to the items list
#         self.items.append(item)
#
#     def pop(self):  # remove and return the top item from the stack if it's not empty
#         if not self.isempty():
#             return self.items.pop()
#
#     def peek(self):  # return the top item from the stack without removing it if the stack is not empty
#         if not self.isempty():
#             return self.items[-1]
#
#
# def reverse():
#     stack = Stack()  # create an instance of the Stack class
#     sequence = input("Enter a sequence of characters: ")  # take user input for a sequence of characters
#     for char in sequence:  # push each character from the sequence onto the stack
#         stack.push(char)
#     print('Reversed sequence:')
#     while not stack.isempty():
#         char = stack.pop()  # pop and retrieve each character from the stack
#         print(char, end='')   # print the character without a newline
#     print()  # print a newline after printing all characters from the stack
#
#
# reverse()
# task_2
# class Stack:
#
#     def __init__(self):
#         self.items = []  # initialize the Stack class with an empty list to store items
#
#     def isempty(self):  # check if the stack is empty by comparing the length of items to zero
#         return len(self.items) == 0
#
#     def push(self, item):  # add an item to the top of the stack by appending it to the items list
#         self.items.append(item)
#
#     def pop(self):  # remove and return the top item from the stack if it's not empty
#         if not self.isempty():
#             return self.items.pop()
#
#     def peek(self):  # return the top item from the stack without removing it if the stack is not empty
#         if not self.isempty():
#             return self.items[-1]
#
#
# def balanced(sequence):
#     stack = Stack()  # create an instance of the Stack class
#     for char in sequence:  # iterate over each character in the sequence
#         if char in '([{':
#             stack.push(char)  # push an opening character onto the stack if it is an opening parenthesis, brace, or
#             # curly bracket
#         elif char in ')]}':  # check if the character is a closing parenthesis, brace, or curly bracket
#             if stack.isempty():
#                 return False  # if the stack is empty and a closing character is encountered, the sequence is not
#                 # balanced
#             top = stack.pop()  # pop the top character from the stack
#             if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
#                 return False  # if the popped character does not match the expected opening character, the sequence is
#                 # not balanced
#
#     return stack.isempty()   # if the stack is empty after processing all characters, the sequence is balanced
#
# sequence = input("Enter a sequence of characters: ")  # take user input
# balance = balanced(sequence)
#
# if balance:
#     print('The sequence is balanced.')
# else:
#     print('The sequence is not balanced')

# task_3_1
# class Stack:
#
#     def __init__(self):
#         self.items = []  # initialize the Stack class with an empty list to store items
#
#     def isempty(self):  # check if the stack is empty by comparing the length of items to zero
#         return len(self.items) == 0
#
#     def push(self, item):  # add an item to the top of the stack by appending it to the items list
#         self.items.append(item)
#
#     def pop(self):  # remove and return the top item from the stack if it's not empty
#         if not self.isempty():
#             return self.items.pop()
#
#     def peek(self):  # return the top item from the stack without removing it if the stack is not empty
#         if not self.isempty():
#             return self.items[-1]
#
#     def get_from_stack(self, element):
#         if element in self.items:  # check if the element exists in the stack
#             stack_copy = []  # initialize an empty list to store elements temporarily
#             while not self.isempty():  # loop until the stack is empty
#                 top = self.pop()  # remove the top element from the stack and stores it in the 'top' variable
#                 if top == element:  # check if the top element is the desired element
#                     while stack_copy:  # push back the elements from the temporary stack to the original stack in their
#                         # original order
#                         self.push(stack_copy.pop())
#                     return top  # return the found element
#                 else:  # if the top element is not the desired element, it is stored in the temporary stack
#                     stack_copy.append(top)
#             while stack_copy:  # push back the remaining elements from the temporary stack to the original stack
#                 self.push(stack_copy.pop())
#         # if the element is not found in the stack, raise ValueError with message
#         raise ValueError(f'Element {element} not found in the stack.')
#
#
# stack = Stack()
# stack.push(5)
# stack.push(3)
# stack.push(2)
# stack.push(7)
# element = stack.get_from_stack(3)
# print(f'Found element: {element}')
# task_3_2
class Queue:

    def __init__(self):
        self.items = []  # initialize the Queue class with an empty list to store items

    def isempty(self):  # check if the queue is empty by comparing the length of items to zero
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)  # append the item to the end of the items list

    def dequeue(self):
        if not self.isempty():  # check if the queue is not empty
            return self.items.pop(0)  # remove and return the item at index 0 from the items list

    def get_from_queue(self, element):
        if element in self.items:  # check if the element exists in the queue
            queue_copy = []  # initialize an empty list to store elements temporarily
            while not self.isempty():  # loop until the queue is empty
                front = self.dequeue()  # remove the front element from the queue and store it in the front
                if front == element:  # check if the front element is the desired element
                    while queue_copy:   # enqueue back the elements from the temporary queue to the original queue in
                        # their original order
                        self.enqueue(queue_copy.pop(0))
                    return front  # return the found element
                else:  # if the front element is not the desired element, it is stored in the temporary queue
                    queue_copy.append(front)
            while queue_copy:  # enqueue back the remaining elements from the temporary queue to the original queue
                self.enqueue(queue_copy.pop(0))
        # if the element is not found in the queue, raise ValueError with message
        raise ValueError(f'Element {element} not found in the queue.')


queue = Queue()
queue.enqueue(5)
queue.enqueue(3)
queue.enqueue(2)
queue.enqueue(7)
queue.enqueue(53)
element = queue.get_from_queue(53)
print(f'Found element: {element}.')


















