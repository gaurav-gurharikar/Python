myset = {1,2,3,4}
#mutable
#elements within a set are immutable (list and dictionary cannot be a part of set)

a = {} #empty dictionary
b = set() #empty set
print(b)

myset.add(5) #adds element

myset.remove(1) #removes element
print(myset)

myset.pop() #removes random value
print(myset)

myset.clear() #empties the set
print(myset)

myset1 = {1,2,3,4}
myset2 = {2,3,4,5,6,7}

set_union = myset1.union(myset2) #combines both sets
print(set_union)

set_intersection = myset1.intersection(myset2) #combines only common values
print(set_intersection)