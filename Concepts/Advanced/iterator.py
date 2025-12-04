val = "ADA"

for x in val:
    print(x)
# here for loop works internally using iterator
# the unsugered version looks like
x = val.__iter__() # or iter(val)
# using iter/__iter__ returns an iterator object mostly returns self (if the class itself is the iterator)

while True:
    try:
        print(x.__next__()) # or next(x) 
        # next/__next__ Returns the next value in the sequence
        # Raises StopIteration when the sequence ends
    except StopIteration:
        break

# Iterator are objects that can be iterated, it implements the iterator protocol, which consist of the methods __iter__() and __next__().
print(x)

# -------------------------------------------------------------------------------------------------------------------------

lst = [1, 2, 3, 4, 5]

it = iter(lst)
print(next(it))

for x in it:
    print(x)
# It won't print 1 two times because once we get 1 once the iterator moves to next value

# print(next(it)) # will raise an error StopIteration; to iterate again create an iterator object again
it = iter(lst)
print(next(it))

# -------------------------------------------------------------------------------------------------------------------------

class Count:
    def __init__(self):
        self.val = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.val <= 25:
            v = self.val
            self.val += 1
            return v
        else:
            raise StopIteration
    
    # This is how you create an iterator
c = Count()
print(iter(c))
print(next(c))
print(next(c))

for x in c:
    print(x)
