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