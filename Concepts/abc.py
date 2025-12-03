from abc import ABC, abstractmethod

"""
Using ABC helps to create Abstract Classes.

Abstract Classes:
- A class that cannot be instantiated directly.
- It is meant to be inherited by other classes.
- It must contain at least one abstract method.

Abstract Methods:
- Methods declared in the abstract class but not implemented.
- They only define the method signature (name and parameters).
- Child classes MUST override/implement them.
"""
class Server(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def put(self):
        pass
# Server is an abstract class and get, post, put are abstract methods

class Client(Server):
    def get(self):
        print("GET method called")

    def post(self):
        print("POST method called")

    def put(self):
        print("PUT method called")
# Client inherits from Server and MUST implement all abstract methods.
# Abstract classes enforce a required structure in subclasses.

s1 = Server() # Can't instantiate abstract class raises an error
# You cannot create an object of Abstract class because it contains abstract methods that have no implementation.
c1 = Client()
c1.get()
c1.post()
c1.put()