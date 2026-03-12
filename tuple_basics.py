tup = (1,2,3,4) 
#immutable

tup = (1) #python will think this is an integer
tup = (1,) # declare single tuple values like this
print(tup)

t = (1,2,2,2,2,3,4,5,6)
print(t.count(2)) #t.count(el): counts no. of el

print(t.index(2)) #t.index(el): returns index of first occurence of el