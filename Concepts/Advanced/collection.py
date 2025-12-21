from collections import Counter, OrderedDict, defaultdict, ChainMap, namedtuple, deque, UserDict, UserString, UserList

"""
The collections module enables to import specialized container data types beyond built-in types like list, dict and tuple.
"""

# -------------------------------------------------------------------------------------------------------------------------

c1 = Counter(['A', 'B', 'C', 'C', 'A', 'B', 'A', 'A'])
c2 = Counter({'A': 3, 'B': 2, "C": 10})
c3 = Counter(A=3, B=4, C=12)

print(c1)
print(c2)
print(c3)
print(type(c1))

"""
Output:
Counter({'A': 4, 'B': 2, 'C': 2})
Counter({'C': 10, 'A': 3, 'B': 2})
Counter({'C': 12, 'B': 4, 'A': 3})
<class 'collections.Counter'>

Counter is used to keep the count of the elements in an iterable in the form of an unordered dictionary
"""

# -------------------------------------------------------------------------------------------------------------------------

ud = OrderedDict()
ud["Name"] = "CrazyGuy"
ud["Age"] = 18
ud["Profession"] = "Python Dev"
ud["Sex"] = "M"

print("Before: ")
print(ud)

del ud["Age"]
print(ud)

print("After:")
ud["Age"] = 20
print(ud)
print(type(ud))

"""
Output:
Before:
OrderedDict({'Name': 'CrazyGuy', 'Age': 18, 'Profession': 'Python Dev', 'Sex': 'M'})
OrderedDict({'Name': 'CrazyGuy', 'Profession': 'Python Dev', 'Sex': 'M'})
After:
OrderedDict({'Name': 'CrazyGuy', 'Profession': 'Python Dev', 'Sex': 'M', 'Age': 20})
<class 'collections.OrderedDict'>

OrderedDict preserves insertion order.
From Python 3.7 onwards, the built-in dict also guarantees insertion order
(as part of the language specification). Before Python 3.6, dicts were
unordered. In Python 3.6, insertion order was preserved in CPython as an
implementation detail, but it was not guaranteed by the language.
OrderedDict is still useful when explicit reordering, order-sensitive
equality, or specialized behaviors (e.g., LRU cache) are required.
"""

# -------------------------------------------------------------------------------------------------------------------------

dd1 = defaultdict(int)
dd2 = defaultdict(str)
dd3 = defaultdict(list)
dd4 = defaultdict(float)
dd5 = defaultdict(tuple)
dd6 = defaultdict(set)
dd7 = defaultdict(dict)

print(dd1[9])
print(dd2[9])
print(dd3[9])
print(dd4[9])
print(dd5[9])
print(dd6[9])
print(dd7[9])

"""
Output:
0

[]
0.0
()
set()
{}

defaultdict gives default value to each key instead of returning an error when value doesnot exist
"""

dd = defaultdict(list)

l = [1, 2, 3, 4, 1, 2, 3, 1, 2, 1]

for x in l:
    dd[x].append(x)

print(dd)
print(type(dd))

"""
Output:
defaultdict(<class 'list'>, {1: [1, 1, 1, 1], 2: [2, 2, 2], 3: [3, 3], 4: [4]})
<class 'collections.defaultdict'>
"""

# -------------------------------------------------------------------------------------------------------------------------

car1 = {"Car": "BMW", "Year": 2016, "Speed": 240, "Lift": 20, "RWD": True}
car2 = {"Car": "Tesla", "Year": 2024, "Electric": True, "AWD": True}
car3 = {"Car": "Honda"}

cm = ChainMap(car1, car2)
print(cm)
print(cm["Car"])
print(cm["RWD"])
print(cm["AWD"])

cm["Car"] = "Mercedes"
print(cm)
del cm["Speed"]
print(cm)
print(type(cm))
# del cm["AWD"]

"""
Output:
ChainMap({'Car': 'BMW', 'Year': 2016, 'Speed': 240, 'Lift': 20, 'RWD': True}, {'Car': 'Tesla', 'Year': 2024, 'Electric': True, 'AWD': True})
BMW
True
True
ChainMap({'Car': 'Mercedes', 'Year': 2016, 'Speed': 240, 'Lift': 20, 'RWD': True}, {'Car': 'Tesla', 'Year': 2024, 'Electric': True, 'AWD': True})
ChainMap({'Car': 'Mercedes', 'Year': 2016, 'Lift': 20, 'RWD': True}, {'Car': 'Tesla', 'Year': 2024, 'Electric': True, 'AWD': True})
<class 'collections.ChainMap'>
Error

Chaimmap merges two dictionary while keeping their original reference and without creating a new copy
Chainmap moves from left to right so cm["Car"] is BMW while car2 also has key Car
while modifying and deleting it only checks the first dict so it raised an error when deleting cm["AWD"] as car1 doesnot have key AWD
"""

# Accessing the keys and values of chainmap
print(cm.keys())
print(cm.values())
print(list(cm.keys()))
print(list(cm.values()))

"""
Output:
KeysView(ChainMap({'Car': 'Mercedes', 'Year': 2016, 'Lift': 20, 'RWD': True}, {'Car': 'Tesla', 'Year': 2024, 'Electric': True, 'AWD': True}))
ValuesView(ChainMap({'Car': 'Mercedes', 'Year': 2016, 'Lift': 20, 'RWD': True}, {'Car': 'Tesla', 'Year': 2024, 'Electric': True, 'AWD': True}))
['Car', 'Year', 'Electric', 'AWD', 'Lift', 'RWD']
['Mercedes', 2016, True, True, 20, True]

doing just .keys and .values returns the key and value view of same chainmap so it seems same
"""

new_cm = cm.new_child(car3)
# Creating a new ChainMap equivalent to new_cm = ChainMap(car3, cm)
print(cm)
print(new_cm)

"""
Output:
ChainMap({'Car': 'Mercedes', 'Year': 2016, 'Lift': 20, 'RWD': True}, {'Car': 'Tesla', 'Year': 2024, 'Electric': True, 'AWD': True})
ChainMap({'Car': 'Honda'}, {'Car': 'Mercedes', 'Year': 2016, 'Lift': 20, 'RWD': True}, {'Car': 'Tesla', 'Year': 2024, 'Electric': True, 'AWD': True})
"""

# -------------------------------------------------------------------------------------------------------------------------

Student = namedtuple('Student', ['name', 'age', 'sex', 'grade']) # This creates a class Student
# The first Student is a variable and the second Student is the name of class. U can use different names for class and variable name
# "name age sex grade" "name, age, sex, grade" instead of list doing space and comma separation can also work

S = Student("AyousoCrazy Guy", 18, "M", 10)

print(S[1])
print(S.name)
print(S)
print(type(S))
print(isinstance(S, tuple))

L = ["Sam", 19, "F", 9]

print(Student._fields)
print(Student._make(L))

print(S._asdict())

S2 = S._replace(grade = 12)
print(S2)

"""
Output:
18
AyousoCrazy Guy
Student(name='AyousoCrazy Guy', age=18, sex='M', grade=10)
<class '__main__.Student'>
True
('name', 'age', 'sex', 'grade')
Student(name='Sam', age=19, sex='F', grade=9)
{'name': 'AyousoCrazy Guy', 'age': 18, 'sex': 'M', 'grade': 10}
Student(name='AyousoCrazy Guy', age=18, sex='M', grade=12)

namedtuple is same as tuple but it enables us to access values using name key instead of interger index
namedtuple makes accessing the values more easier
namedtuples are immutable like tuples
"""

# -------------------------------------------------------------------------------------------------------------------------

d = deque([1, 2, 3, 4])
print(d)
print(type(d))

d.append(5)
print(f"Append right: {d}")
d.appendleft(0)
print(f"Append left: {d}")

rm = d.pop()
print(f"{rm} removed from {d} from right")

rm = d.popleft()
print(f"{rm} removed from {d} from left")

"""
Output:
deque([1, 2, 3, 4])
<class 'collections.deque'>
Append right: deque([1, 2, 3, 4, 5])
Append left: deque([0, 1, 2, 3, 4, 5])
5 removed from deque([0, 1, 2, 3, 4]) from right
0 removed from deque([1, 2, 3, 4]) from left

deque(Double Ended Queue) is a optimized list for quicker append and pop operations from both sides of the container
"""

# -------------------------------------------------------------------------------------------------------------------------

class MyList(UserList):

    def pop(self, s=None):
        raise RuntimeError("Deletion Not Allowed")
    
L = MyList([1, 2, 3, 4])
print(f"Original list: {L}")
L.append(5)
print(f"After Append: {L}")
print(type(L))

# L.pop(1)
# Will raise an error 

"""
Output:
Original list: [1, 2, 3, 4]
After Append: [1, 2, 3, 4, 5]
<class '__main__.MyList'>
Error

UserList is an wrapper around list object that helps to modify list functonality
"""

# -------------------------------------------------------------------------------------------------------------------------

class MyDict(UserDict):
    def popitem(self):
        raise RuntimeError("Item deletion not allowed")
    
    def pop(self):
        raise RuntimeError("Deletion not allowed")
    
D = MyDict({"Room": "202A", "Floor": 2})
print(f"Original dict: {D}")
D["Bed"] = 2
print(f"After insertion: {D}")
print(type(D))

# D.popitem()
# Will raise an error 

"""
Output:
Original dict: {'Room': '202A', 'Floor': 2}
After insertion: {'Room': '202A', 'Floor': 2, 'Bed': 2}
<class '__main__.MyDict'>

UserDict acts as a wrapper around the dictionary objects and is userfull to create dictionary with modified behaviour
"""

# -------------------------------------------------------------------------------------------------------------------------

class MyString(UserString):
    def append(self, s): 
        self.data += s 
          
    def remove(self, s): 
        self.data = self.data.replace(s, "") 

S = MyString("User Python")
print(f"Original string: {S}")
S.append("and Rust")
print(f"After insertion: {S}")
S.remove("and")
print(f"After removal: {S}")

print(type(S))

"""
Output:
Original string: User Python
After insertion: User Pythonand Rust
After removal: User Python Rust
<class '__main__.MyString'>

UserString acts as a wrapper around string objects useful to create their own strings with some modified or additional functionality
"""