"""
Classes are blueprint to create an object
Object are anything with attribute and methods
"""

class College:
    institute = "NEB"
    # This is static/class variable and this is same for all objects of the class 

    def __init__(self, name, reg_no, address, students):
        # The __init__ is like a constructor but it is not a actual constructor
        # Constructor are methods that runs automatically when objects are created and they initialize the object
        # __init__ also runs autometically and initializes the object
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

    @staticmethod
    def petrol_price():
        print("The petrol price is NRP 146")
    # This is static method that does not deal with instance variable nor class variable

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
        # But it follows MRO(method Resolution Order) from left to right so __init__ of Land will execute
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

This is duck typing. It doesnot matter which department is passed if the department has method execute it will work.
Duck Typing = If an object has the method you want, you can use it.
Python focuses on behavior, not the object’s actual type.
“If it walks like a duck and quacks like a duck, it’s a duck.”

like len() in string, tuple, lists
"""

# -------------------------------------------------------------------------------------------------------------------------

class Account:
    def __init__(self, net_income = 0, interest = 0, tax = 0, depreciation = 0, amortization = 0): # this is called method overloading
        # In python method overloading does not exist independently but we can give a default value that can be later over written
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
            return TypeError("Can only add Account objects")

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
"""