try: # try this block of code if there is no error
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    div = num1 / num2

except ZeroDivisionError as e: # handle ZeroDivisionError with this
    print("You cannot divide a number by 0", e)

except ValueError as e:# handle ValueError with this
    print("Invalid Number")

except Exception as e: # handle other Exception with this
    print(e)

else: # runs only when no exception occurs
    print(f"{num1} / {num2} = {div}")

finally: # this block works either there is an exception or not
    print("Division done")

# -------------------------------------------------------------------------------------------------------------------------

def set(age):
    if isinstance(age, (int, float, complex)):
        if age < 0:
            raise ValueError("Age cannot be less than zero")
    else:
        raise TypeError("Age cannot be this type")
    
    print(f"Age set: {age}")

try:
    set("five")
except Exception as e:
    print(e)

# You can use raise error method to display modified error message

# -------------------------------------------------------------------------------------------------------------------------

class MyException(Exception):
    def __init__(self, age, message="Invalid age"):
        self.age = age
        self.message = message
        super().__init__(f"{message}: {age}")

def set_age(age):
    if isinstance(age, (int, float, complex)):
        if age < 0:
            raise MyException(age, "Age cannot be less than zero")
    else:
        raise MyException(age, "Age cannot be this type")
    
    print(f"Age set: {age}")

try:
    set_age(-5)
except MyException as e:
    print(e.age)
    print(e.message)

# You can also create custom exceptions by defining a new class that inherits from Python’s built-in Exception class?