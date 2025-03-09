
import copy

# custom error for stack size
class StackSizeError(Exception):
    pass

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
                raise StackSizeError("Max size argument value must be Integer!")
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
                raise ValueError("allowed_types must be a class or a list of classes!")
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

    # simple method to clear stack
    def clear(self):
        self.__items.clear()
    
    # simple method to check if item is in stack
    def contains(self, item):
        return item in self.__items
    
    # simple method to get max size of stack
    def max_size(self):
        return self.__max_size
    
    # simple method to set new max size of stack
    def set_max_size(self, new_max_size):
        # check if given value is int
        if type(new_max_size) == int:
            # check if given number is more or equal to current number of items in stack
            if new_max_size >= len(self.__items):
                self.__max_size = new_max_size
            else:
                raise StackSizeError('Stack size is less then new max_size!')        # raise custom error if invalid size
        else:
            raise StackSizeError("Max size argument value must be Integer!")
        
    # simple method to get how many space left in stack if it has limit
    def space_left(self):
        return self.__max_size - len(self.__items) if self.__max_size else -1               # return -1 if no limit
    
    # method to get deep(so mutable objects inside of stack get copied) copy of stack
    def copy_stack(self):
        # create new stack with same properties as original
        new_stack = Stack(self.__max_size, copy.deepcopy(self.__allowed_types))

        new_stack.__items = copy.deepcopy(self.__items)         # set items to new stack from original stack

        return new_stack                                        # return new stack

    # method to get item from stack using indexes
    def __getitem__(self, index):
        # check if index's value is integer
        if type(index) == int:
            if index < 0:                                   # handle negative indexes
                index = len(self.__items) + index           # convert negative index to positive

            # check if given index is in correct range
            if 0 <= index < len(self.__items):
                return self.__items[index]
            else:
                raise IndexError("Stack index out of range!")                             # raise error if it's out of range
        else:
            raise ValueError('Index must be integer!')                                    # raise error if its not integer

    # method to set new value at a specific index using indexes
    def __setitem__(self, index, value):
        # check if index's value is integer
        if type(index) == int:
            if index < 0:                                   # handle negative indexes
                index = len(self.__items) + index           # convert negative index to positive

            # check if given index is in correct range
            if 0 <= index < len(self.__items):
                if self.__allowed_types is None or self.__check_type(value):
                    self.__items[index] = value
                else:
                    raise ValueError("Not allowed type!")                                # raise error if incorrect type given
            else:
                raise IndexError("Stack index out of range!")                             # raise error if it's out of range
        else:
            raise ValueError('Index must be integer!')                                    # raise error if its not integer

    # method to delete items in stack using indexes
    def __delitem__(self, index):
        # check if index's value is integer
        if type(index) == int:
            # check if given index is index of last item in stack
            if index == -1:
                del self.__items[index]
            else:
                raise IndexError("Can delete only last item in Stack!")                             # raise error if it's not index of last item
        else:
            raise ValueError('Index must be integer!')                                    # raise error if its not integer

    # method to make stack iterable
    def __iter__(self):
        return iter(self.__items)

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

print(my_stack.contains(554))
print(my_stack.max_size())
my_stack.set_max_size(32)
print(my_stack.max_size())
my_stack.clear()
print(my_stack)
my_stack.push(72.43)
my_stack.push(362.783)
my_stack.push('feage335')
my_stack[0] = "ega"
print(my_stack[-1])
del my_stack[-1]
print(my_stack)
for i in my_stack:
    print(i)
my_stack2 = my_stack.copy_stack()
print(my_stack2.space_left())