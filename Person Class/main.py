
from string import ascii_letters

# basic Person class
#  working with property objects & decorators
class Person:

    __letters = ascii_letters       # valid symbols for the person name

    def __init__(self, fn, age, passport, weight):          # on Person class object initialization:
        # since names of attributes below exactly match with corresponding property objects names,
        #  on initialization they will automatically call their setter methods
        #   setter method will run verification function that will check if inputed data is in correct format
        self.fn = fn
        self.age = age
        self.passport = passport
        self.weight = weight

    # class method that checks if inputed fn is in correct format
    @classmethod
    def verify_fn(cls, fn):
        if type(fn) != str:                                         # check if string
            raise TypeError('Invalid Type of person Full Name!')
        
        fn = fn.split()
        if len(fn) != 2:                                            # check if it has only 2 parts
            raise TypeError('Invalid Type of person Full Name!')

        for i in fn:
            if len(i) < 1:                                              # each part should have atleast 1 letter
                raise TypeError('Invalid Type of person Full Name!')        
            if len(i.strip(cls.__letters)) != 0:                        # check if it has no invalid symbols
                raise TypeError('Invalid Type of person Full Name!')
    
    # static method that checks if inputed age is in correct format
    @staticmethod
    def verify_age(age):
        if type(age) != int or age < 18 or age > 110:               # age should be int. valid range - [18, 110]
            raise TypeError('Invalid Type of age! Valid Range - [18, 110]')

    # static method that checks if inputed passport is in correct format
    @staticmethod
    def verify_passport(passport):
        if type(passport) != str:                                   # check if inputed passport is str
            raise TypeError('Invalid Type of passport!')
        
        passport = passport.split()

        # passport should have two parts:
        #   first part should have 4 digits
        #   second part should have 6 digits
        if len(passport) != 2 or len(passport[0]) != 4 or len(passport[1]) != 6:     
            raise TypeError('Invalid Type of passport!')

        for i in passport:
            if not i.isdigit():                                     # check each symbol if it is digit
                raise TypeError('Invalid Type of passport!')
            
    # static method that checks if inputed weight is in correct format
    @staticmethod
    def verify_weight(weight):
        if type(weight) != float or weight < 30:                    # inputed weight should be float. atleast 30 kilos
            raise TypeError('Invalid Type of weight!')

    @property               # property object (getter) decorator for the fn(full name) attribute
    def fn(self):
        return self.__fn
    
    @fn.setter                  # property object (setter) decorator for the fn(full name) attribute
    def fn(self, fn):
        self.verify_fn(fn)          # verify new fn
        self.__fn = fn.split()      # save fn as an array

    @property                   # property object (getter) decorator for the age attribute
    def age(self):
        return self.__age

    @age.setter                 # property object (setter) decorator for the age attribute
    def age(self, age):
        self.verify_age(age)        # verify new age
        self.__age = age

    @property                   # property object (getter) decorator for the passport attribute
    def passport(self):
        return self.__passport
    
    @passport.setter                # property object (setter) decorator for the passport attribute
    def passport(self, passport):
        self.verify_passport(passport)          # verify new passport
        self.__passport = passport

    @property                   # property object (getter) decorator for the weight attribute
    def weight(self):
        return self.__weight
    
    @weight.setter              # property object (setter) decorator for the weight attribute
    def weight(self, weight):           
        self.verify_weight(weight)      # verify new weight
        self.__weight = weight

P1 = Person('Name Lastname', 26, '1234 567890', 92.0)

# it is more comfortable to use property objects to get or set object attributes
#  u can customize get and set methods as you like

P1.age = 35 + 2*((363//3) - 105)

print(P1.fn)
print(P1.age)
print(P1.passport)
print(P1.weight)
print(P1.__dict__)