"""
Dictionary is also an array but is arranged in a key value pair
Simply the key acts as the index number and value is the value of that index number
Dictionary is defined same as set using {} sign but has key and value
"""

individual = {'name': 'AyousoCrazy Guy', 'age': 18, 'address': 'Nepal', 'interest': 'programming', 'Birth Year': 2007}
print(individual)
print(type(individual))
"""
Output:
{'name': 'AyousoCrazy Guy', 'age': 18, 'address': 'Nepal', 'interest': 'programming', 'Birth Year': 2007}
<class 'dict'>
"""

# -------------------------------------------------------------------------------------------------------------------------

# You can access the value using keys as index 
print(individual['name'])
print(individual['age'])
"""
Output:
AyousoCrazy Guy
18
"""

print(individual['language'])
# this will raise an error as there is no key 'language'

# instead you can do 
print(individual.get('language', 'Not Found'))
"""
Output:
Not Found
"""
# .get does not raise error instead we can use it as conditional

# -------------------------------------------------------------------------------------------------------------------------

# You can get all the keys and all the values using .keys and .values
# .items returns each item as a tuple 
print(individual.keys())
print(individual.values())
print(individual.items())
"""
Output:
dict_keys(['name', 'age', 'address', 'interest', 'Birth Year'])
dict_values(['AyousoCrazy Guy', 18, 'Nepal', 'programming', 2007])
dict_items([('name', 'AyousoCrazy Guy'), ('age', 18), ('address', 'Nepal'), ('interest', 'programming'), ('Birth Year', 2007)])
"""

# -------------------------------------------------------------------------------------------------------------------------

print(individual['interest'])

individual['interest'] = ['singing', 'programming', 'gaming']
print(individual['interest'])
# Dictionary are mutable and we can set an array as the value as well
print(individual['interest'][0:2])
# And we can also slice the value of the array value using the index number

"""
output:
programming
['singing', 'programming', 'gaming']
['singing', 'programming']
"""

individual['marksheet'] = {'math': 35, 'literature': 44, 'economics': 23}
print(individual)
print(individual['marksheet']['literature'])
"""
Output:
{'name': 'AyousoCrazy Guy', 'age': 18, 'address': 'Nepal', 'interest': ['singing', 'programming', 'gaming'], 'Birth Year': 2007, 'marksheet': {'math': 35, 'literature': 44, 'economics': 23}}
44

You can have dictionary as value of dictionary and you can also access the value off the dictionary value
"""

# -------------------------------------------------------------------------------------------------------------------------

keys = ['brand', 'year', 'color']
values = ['Ford', 2013, 'gray']

car_dictionary = dict(zip(keys, values))
print(car_dictionary)
# you can use zip to create a pair and dict(zip()) to create a dictionary of that pair 

# -------------------------------------------------------------------------------------------------------------------------

car_dictionary.pop('year')
print(car_dictionary)
# it removes the item based on the key 
car_dictionary.popitem()
print(car_dictionary)
# removes the last inserted item 
car_dictionary.clear()
print(car_dictionary)
# clears the dictionary 
del car_dictionary
print(car_dictionary)
# deleted the entire thing

# -------------------------------------------------------------------------------------------------------------------------

print(individual)
for x in individual.keys():
    print(x)

for x, y in individual.items():
    print(f"{x} : {y}")
# You can loop through a dictionary like this

# -------------------------------------------------------------------------------------------------------------------------

copy = individual
print(copy)
copy = individual.copy()
print(copy)
copy = dict(individual)
print(copy)

# You can copy a dictionary like this