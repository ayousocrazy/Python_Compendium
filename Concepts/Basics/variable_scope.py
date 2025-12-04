re = 332211

def update():
    num = 1221
    print(num)
    print(re)

update()
print(num)
"""
Here re is a global variable and it can be accessed by any function
But
num is a local variable and its scope is only within the function it is defined in
"""

# -------------------------------------------------------------------------------------------------------------------------

def modify():
    global num
    num = 1221
    print(num)

modify()
print(num)
"""
The global <variable_name> makes that variable global
"""

# -------------------------------------------------------------------------------------------------------------------------

n = 101
print(id(n))

def alter():
    n = 100
    print(id(n))
    globals()['n'] = 1001
    print(n)

alter()
print(n)
"""
gloals()['variable_name'] helps in accessing the global variable with its variable name also creating a local variable with the same variable name
"""

# -------------------------------------------------------------------------------------------------------------------------

def call1():
    alpha = 30
    print(alpha)
    def call2():
        nonlocal alpha
        alpha = 45
        print(alpha)
    call2()
    print(alpha)

call1()
print(alpha)
"""
nonlocal gives increases the scope of variable to the outer variable while not making it a global variable
"""