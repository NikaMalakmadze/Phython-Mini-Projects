
# custom data type created by myself :) (:
#  very simple stack(something like array)
class Stack:

    def __init__(self, max_size=None, allowed_types=None):
        # array where items will be stored
        self.__items = []

        # check if user setted max size of stack
        if max_size is not None:
            # check if max_size is integer, if not raise error
            if type(max_size) == int:
                self.__max_size = max_size
            else:
                raise ValueError("Max size argument must be Integer!")
        else:
            self.__max_size = None          # if no max_size argument given, it's None

        # if user inputed allowed types
        if allowed_types is not None:
            # check if given argument value is list plus check if items in that list are class names
            #  so we need it if user want multiple allowed types
            if isinstance(allowed_types, list) and all(self.__is_class(cls) for cls in allowed_types):
                self.__allowed_types = allowed_types

            # if it's not list then it must be one allowed type, but also check if it's class name
            elif self.__is_class(allowed_types):
                self.__allowed_types = [allowed_types]
            else:
                raise ValueError("allowed_types must be a class or a list of classes")
        else:
            self.__allowed_types = None  # allow all types if not specified

    # static method, needed to check if given value is class name -> instance of type object
    @staticmethod   # <- Decorator
    def __is_class(value):
        return isinstance(value, type)

    # simple method that checks if stack is full
    def is_full(self):
        return True if self.__max_size is not None and len(self.__items) >= self.__max_size else False

    # simple method to check if stack is empty
    def is_empty(self):
        return len(self.__items) == 0
    
    # helper method to check if inputed item is instance of any allowed type
    def __check_type(self, item):
        return True if any([isinstance(item, allowed_type) for allowed_type in self.__allowed_types]) else False

    # push method
    def push(self, item):
        # check if theres enough space in stack
        if not self.is_full():
            # if user inputed allowed types
            if self.__allowed_types is not None:
                # check type of inputed item
                if self.__check_type(item):
                    self.__items.append(item)                       # push in stack if it passes test
                else:
                    raise ValueError('Not allowed type!')           # raise error if it fails test
            else:
                self.__items.append(item)                           # if theres no restrictions, just add any item in stack
        else:
            raise ValueError('Reached Max size of Stack!')          # if not raise error

    # simple method to pop item from stack
    def pop(self):
        # check if stack is not empty
        if not self.is_empty():
            return self.__items.pop()                               # return pop item
        else:
            raise ValueError("Can't pop, Stack is Empty!")          # raise error if stack is empty
    
    # simple method to peek(get last element of stack)
    def peek(self):
        # check if stack is not empty
       if not self.is_empty():
           return self.__items[-1]                                  # return last item in stack
       else:
            raise ValueError("Can't peek, Stack is Empty!")         # raise error if stack is empty
    
    # simple method to get size/length of stack 
    def size(self):
        return len(self.__items)
    
    # simple method to reverse stack
    def reverse(self):
        self.__items.reverse() 

    # custom representation of my stack, cool!
    def __str__(self):
        return ":) " + ', '.join(str(item) for item in self.__items) + " (:" if self.__items else ":) Empty! (:"

my_stack = Stack(max_size= 16, allowed_types=[int, str, float, list])

my_stack.push(35)
my_stack.push([])
my_stack.push(554)
my_stack.push('feage')
my_stack.push('feage335')
my_stack.push('3.5463')
my_stack.push(3352.43)
my_stack.push(72.43)
my_stack.push(362.783)
my_stack.push([[1, 2, 3]])
my_stack.reverse()
print(my_stack.is_empty())
print(my_stack.is_full())
print(my_stack.size())
print(my_stack.peek())
print(my_stack.pop())
print(my_stack)