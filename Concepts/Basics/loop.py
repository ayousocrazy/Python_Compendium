"""
There are two ways to loop
while
for
"""

# While loop needs a variable declaration before while, condition check on while and increment on loop 
i = 0
while i<5:
    print("Ayousocrazy")
    i +=1

# For loop handles everything in the same line 
for x in range(1, 10, 2):
    print(x)

fruits = ["Apple", "Banana", "Mango", "Orange", "Kiwi", "Tomato", "Papaya", "Cherry", "Fig", "Melon"] 

for x in fruits:
    if x.lower() == 'tomato':
        break
    print(x)
else:
    print("Loop Ended")
# You can add a break to break out of the loop at any time 

for x in range(1, 5):
    if x.lower() == 'tomato':
        continue
    print(x)
else:
    print("Loop Ended")
# the else only execute when loop ends without break 