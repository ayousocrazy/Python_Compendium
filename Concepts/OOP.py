"""
Classes are blueprint to create an object
Object are anything with attribute and methods
"""

class College:
    institute = "NEB"
    # This is a class variable (static variable)
    # It is shared among all objects unless overridden by an instance variable

    def __init__(self, name, reg_no, address, students):
        # __init__() is the initializer
        # Python's actual constructor is __new__(), but __init__() is what initializes object attributes
        # It runs automatically whenever an object is created
        self.name = name
        self.reg_no = reg_no
        self.address = address
        self.students = students
        # These are instance variables that changes with object 

    def register(self):
        # This is a method of object
        print(f"Registered {self.name} with reg. no {self.reg_no}")
    
kmc = College('Kathmandu Model College', 'kmc112211io', 'Baagbazar, Kathmandu', 1201)
gcm = College('Global College of Management', 'gcm112212io', 'Old Baneshwor, Kathmandu', 905)

gcm.reg_no = 'gcm1009io'
# You can change the value of instance variable

College.register(kmc)
gcm.register()

kmc.institute = 'Cambridge International'
# Here the value of class variable didn't change it created another instance variable that hides the class variable
print(kmc.institute)
del kmc.institute
print(kmc.institute)

College.institute = 'Cambridge International'
print(kmc.institute)
print(gcm.institute)

"""
Output:
Registered Kathmandu Model College with reg. no kmc112211io
Registered Global College of Management with reg. no gcm1009io
Cambridge International
NEB
Cambridge International
Cambridge International
"""

# -------------------------------------------------------------------------------------------------------------------------

class Bike:
    wheels = 2

    def __init__(self, liscense, year, company, mileage):
        self.liscense = liscense
        self.year = year
        self.company = company
        self.milage = mileage

    def registration(self):
        print(f"{self.company} {self.year} Bike {self.liscense} registered") 
    # This is called instance method because it deals with instance variable
    # There are 2 type of instance method, accessor and mutator method

    def get_liscense(self):
        return self.liscense
    # This is accessor instance method

    def update_liscense(self, liscense):
        self.liscense = liscense
    # This is mutator instance method

    @classmethod
    def modification(cls):
        cls.wheels = 3
        return "Has 3 wheels now"
    # This is class method as it deals with class variable
    # @classmethod receives the class as 'cls' and can modify class-level data

    @staticmethod
    def petrol_price():
        print("The petrol price is NRP 146")
    # @staticmethod does not receive the class or the object
    # It is used when the method is logically related to the class but does not access class or instance variables

bike1 = Bike('B AB 1445', 2017, 'Yamaha', 2.4)
bike2 = Bike('B DE 2108', 2020, 'BMW', 1.6)

bike1.registration()
print(bike1.get_liscense())
bike1.update_liscense('B AB 1444')
print(bike1.get_liscense())
print(Bike.modification())
Bike.petrol_price()
bike1.petrol_price()

"""
Output:
Yamaha 2017 Bike B AB 1445 registered
B AB 1445
B AB 1444
Has 3 wheels now
The petrol price is NRP 146
The petrol price is NRP 146
"""

# -------------------------------------------------------------------------------------------------------------------------

class Professor:
    def __init__(self, name, age, *subject, brand, processor, ram, storage):
    # def __init__(self, name, age, *subject_laptop):
        self.name = name
        self.age = age

        # *subject, brand, processor, ram, storage = subject_laptop

        self.subjects = list(subject)
        self.laptop = self.Laptop(brand, processor, ram, storage)
        
    def info(self):
        print("Personal Info:-")
        print(f"Name: {self.name}\nAge: {self.age}\nSubjects: {', '.join([x for x in self.subjects])}")
        self.laptop.info()

    class Laptop:
        def __init__(self, brand, processor, ram, storage):
            self.brand = brand
            self.processor = processor
            self.ram = ram
            self.storage = storage

        def info(self):
            print("Laptop Info:-")
            print(f"Brand: {self.brand}\nProcessor: {self.processor}\nRAM: {self.ram}\nStorage: {self.storage}")

p1 = Professor("Chitra Poudel", 32, 'Physics', 'Mathematics', brand = 'HP', processor = 'i5', ram = '16GB', storage = '256GB SSD')
# You have to pass keyword argument in this situation
# p1 = Professor("Chitra Poudel", 32, 'Physics', 'Mathematics', 'HP', 'i5', '16GB', '512GB SSD')
# If you don't want that you can pass positional argument and make a tuple and then distribute the values
p2 = Professor("MD Jafeer", 40, 'History', 'Geology', brand = 'Lenovo', processor = 'i7', ram = '32GB', storage = '512GB SSD')
p3 = Professor("Suchana Pradhan", 30, 'Computer Science', brand = 'HP', processor = 'i5', ram = '16GB', storage = '256GB SSD')

p1.info()
p3 = Professor("Chitra Poudel", 32, 'Physics', 'Mathematics', brand = 'HP', processor = 'i5', ram = '16GB', storage = '256GB SSD')


print(id(p1.laptop))
print(id(p2.laptop))
print(id(p3.laptop))
# creates a different laptop object for different Professor object though p1 and p3 has same Laptop specs
"""
Output:
Personal Info:-
Name: Chitra Poudel
Age: 32
Subjects: Physics, Mathematics
Laptop Info:-
Brand: HP
Processor: i5
RAM: 16GB
Storage: 256GB SSD
1786500253696
1786502096144
1786502096288

Like this you can have inner class 
Inner (nested) classes are defined inside another class
They are useful when the inner class is closely related to the parent class and should not be used independently

"""

del Professor
del p1
del p2
del p3

# -------------------------------------------------------------------------------------------------------------------------

class Professor:
    def __init__(self, name, age, *subject):
        self.name = name
        self.age = age
        self.subjects = list(subject)
        self.laptop = []

    def add_laptop(self, brand, processor, ram, storage):
        laptop = self.Laptop(brand, processor, ram, storage)
        self.laptop.append(laptop)
        
    def info(self):
        print("Personal Info:-")
        print(f"Name: {self.name}\nAge: {self.age}\nSubjects: {', '.join([x for x in self.subjects])}")
        for l in self.laptop:
            l.info()

    class Laptop:
        def __init__(self, brand, processor, ram, storage):
            self.brand = brand
            self.processor = processor
            self.ram = ram
            self.storage = storage

        def info(self):
            print("Laptop Info:-")
            print(f"Brand: {self.brand}\nProcessor: {self.processor}\nRAM: {self.ram}\nStorage: {self.storage}")

p1 = Professor('Chiranjibi Acharya', 35, 'Micro Finance', 'Economics')
p1.add_laptop("HP", "i5", "16GB", "256GB SSD")
p1.add_laptop("Dell", "i7", "32GB", "512GB SSD")

p1.info()

for l in p1.laptop:
    print(id(l))

"""
Personal Info:-
Name: Chiranjibi Acharya
Age: 35
Subjects: Micro Finance, Economics
Laptop Info:-
Brand: HP
Processor: i5
RAM: 16GB
Storage: 256GB SSD
Laptop Info:-
Brand: Dell
Processor: i7
RAM: 32GB
Storage: 512GB SSD
2556343780128
2556343780080

Now one professor can have multiple laptop and new laptop object in created for individual laptop of professor
"""

# -------------------------------------------------------------------------------------------------------------------------

class Land:
    def __init__(self):
        print("Initializing Land Animals")

    def walk(self):
        print("Can walk")

    def reproduce(self):
        print("Lay egg and also give birth")

class Water:
    def __init__(self):
        print("Initializing Water Animals")

    def swim(self):
        print("Can swim")

    def reproduce(self):
        print("Most lay eggs")

class Amphibian(Land, Water): # This class is inheriting attribute and method from two classes
    def __init__(self): # The __init__ of parent class is initialized when child class doesn't have one
        super().__init__() # With super() you can access the parent class/ super class 
        # super() calls the next class in the Method Resolution Order (MRO)
        # Because Amphibian inherits from (Land, Water), MRO runs left to right, so Land.__init__() runs first
        print("Initializing Amphibians")

    def locomotion(self):
        print("Can walk and swim")

a1 = Amphibian()
a1.locomotion()
a1.walk()
a1.swim()
# Can access all methods of parent class 
a1.reproduce()
# MRO(method Resolution Order) due to this reproduce method of Land gets executed

# -------------------------------------------------------------------------------------------------------------------------

class Maintenance:
    def execute(self):
        print("Maintain the product")

class Quality:
    def execute(self):
        print("Check quality and perform quality control")

class Accounts:
    def execute(self):
        print("Calculate P&L and maintain Books of Accounts")

class Employee:
    def work(self, department):
        department.execute()

m = Maintenance()
q = Quality()
a = Accounts()

e1 = Employee()

for x in [m, q, a]:
    e1.work(x)
"""
Output:
Maintain the product
Check quality and perform quality control
Calculate P&L and maintain Books of Accounts

This is duck typing. It doesnot matter which department is passed if the department has method execute it will work
Duck Typing = If an object has the method you want, you can use it
Python focuses on behavior, not the object’s actual type
“If it walks like a duck and quacks like a duck, it’s a duck”

In duck typing, the type of the object does NOT matter
Only the presence of the required method matters

like len() in string, tuple, lists
"""

# -------------------------------------------------------------------------------------------------------------------------

class Account:
    def __init__(self, net_income = 0, interest = 0, tax = 0, depreciation = 0, amortization = 0): # this is called method overloading
        # Python does not support method overloading like Java/C++
        # Instead, we use default arguments (*args, **kwargs) to simulate overloading behavior
        # In other language function1(a, b) and function1(a, b, c) can exist i.e. same method with same name but accepting different number of argument can exist this is method overloading
        self.net_income = net_income
        self.tax = tax
        self.interest = interest
        self.depreciation = depreciation
        self.amortization = amortization
        
    def __add__(self, extra):
        if isinstance(extra, Account):
            new = Account(
                self.net_income + extra.net_income,
                self.interest + extra.interest,
                self.tax + extra.tax,
                self.depreciation + extra.depreciation,
                self.amortization + extra.amortization
            )
            return new
        else:
            raise TypeError("Can only add Account objects")

b1 = Account(1200, 300, 30, 200)
b2 = Account(1300, 400, 500, 20, 40)

b3 = b1 + b2

print(b3.interest, b3.net_income, b3.depreciation, b3.tax, b3.amortization)

"""
Output:
700 2500 220 530 40

This is called operator overloading
"""

# -------------------------------------------------------------------------------------------------------------------------

class Parent:
    def run(self):
        print("Parent Compiling")
        print("Parent Running")

class Child1(Parent):
    pass

class Child2(Parent):
    def run(self):
        print("Child Compiling")
        print("Child Running")

c1 = Child1()
c2 = Child2()

print("c1 running")
c1.run()
print("c2 running")
c2.run()

"""
Output:
c1 running
Parent Compiling
Parent Running
c2 running
Child Compiling
Child Running

This is called method overriding where child class method over rides the parent class method
Method overriding occurs when a child (derived) class defines a method with the same name as the parent class, but gives it a different implementation.
Overriding happens when child class redefines the same method name as the parent class
"""

# -------------------------------------------------------------------------------------------------------------------------

class Citizen:
    def __init__(self, name, citizenship_no, age, religion, DOB):
        self.name = name
        self.__citizenship_no = citizenship_no # adding __ encapsulates the attribute and make the property private
        self.age = age
        self.religion = religion
        self.DOB = DOB

    def get_citizenship_no(self):
        return self.__citizenship_no # the private data can only be accessed from inside the class
    
    def update_citizenship_no(self, num):
        if isinstance(num, (str, int)):
            self.__citizenship_no = num
        else:
            print("Invalid format")
            return("Invalid format")
        
del c1
c1 = Citizen("Ramesh Pradhan", '14-22-44-1234', 24, 'Hindu', '10/10/2000')
print(c1.name)
# print(c1.__citizenship_no) # This will raise an error as this is a private attribute and it cannot be accessed from outside the class
c1.__citizenship_no = "22-33-44-5678" # the private data cannot be changed outside the class
print(c1.__citizenship_no)
# It created another instance variable of c1 but didn't change the value 
print(c1.get_citizenship_no())
c1.update_citizenship_no("22-33-44-5678")
print(c1.get_citizenship_no())
print(c1._Citizen__citizenship_no) # This is not recommended
# In this way python uses name mangling to access private properties
# When you use double underscores __, Python automatically renames it internally by adding _ClassName in front.

"""
Output:
Ramesh Pradhan
22-33-44-5678
14-22-44-1234
22-33-44-5678

Double underscore (__var) → Private attribute  
- Python applies name-mangling → _ClassName__var  
- Cannot be accessed or modified directly outside the class.
"""

# -------------------------------------------------------------------------------------------------------------------------

class Vote:
    def __init__(self, name, voter_no, nin, DOB):
        self.name = name
        self.DOB = DOB
        self.__voter_no = voter_no
        self.__nin = nin

    def __validate(self, voter_no, nin): # This is private method as it cannot be accessed from outside the class
        if isinstance(voter_no, str) and isinstance(nin, str):
            return True
        else:
            return False
        
    def update_voter_id(self, voter_no, nin):
        if self.__validate(voter_no, nin):
            self.__voter_no = voter_no
            self.__nin = nin
        else:
            print("Invalid NIN or Voter Number")
    
    def get_voter_number(self):
        return self.__voter_no
    
    def get_nin(self):
        return self.__nin
    
v1 = Vote("Narayan Gopal", '12245', '22-43-66-7812', '12/12/2005')
print(v1.get_voter_number())
print(v1.get_nin())
# v1.__validate('12244', '22-43-66-7811') # this will raise an error because __validate is a private method
v1.update_voter_id('12244', '22-43-66-7811')
print(v1.get_voter_number())
print(v1.get_nin())

"""
Output:
12245
22-43-66-7812
12244
22-43-66-7811

Private methods (__method):
- Can only be called inside the class.
- Name-mangled: _ClassName__method
"""

# -------------------------------------------------------------------------------------------------------------------------

class NID:
    def __init__(self, name, nin):
        self.name = name
        self._nin = nin
        # A single underscore _ is just a convention
        # It tells other programmers that the property is intended for internal use, but Python doesn't enforce this restriction.

n1 = NID('Brijesh Lama', 12556)
print(n1._nin)

"""
Output:
12556

Single underscore (_var) → Protected (by convention only)  
- Python does NOT enforce protection  
- Developers treat it as "internal use".
"""