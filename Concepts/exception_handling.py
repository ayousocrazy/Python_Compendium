try: # try this block of code if there is no error
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    div = num1 / num2

    print(f"{num1} / {num2} = {div}")

except ZeroDivisionError as e: # handle ZeroDivisionError with this
    print("You cannot divide a number by 0", e)

except ValueError as e:# handle ValueError with this
    print("Invalid Number")

except Exception as e: # handle other Exception with this
    print(e)

finally: # this block works either there is an exception or not
    print("Division done")