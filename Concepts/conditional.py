"""
We use if elif else for conditional statements
Or 
Match case
"""

num = 100231014
if num % 7:
    print(f"{num} is divisible by 7")
elif num % 5:
    print(f"{num} is divisible by 5")
else:
    print(f"{num} is not divisible by 7 and 5")

# -------------------------------------------------------------------------------------------------------------------------

day = input("Enter day of week: ").lower()

match day:
    case 'sunday' | 'monday' | 'tuesday':
        print(":(")
    case 'wednesday' | 'thrusday':
        print(":|")
    case 'friday':
        print(':)')
    case _:
        print("*3*")