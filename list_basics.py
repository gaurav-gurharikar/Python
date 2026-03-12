list = [2,1,7,3,4,4]
#mutable

list.append(8) 
print(list)

list.reverse()
print(list)

list.sort() #ascending
print(list)

list.sort(reverse=True) #descending
print(list)

list.insert(0, 6) #(index,element)
print(list)

list.pop(0) #pop(index)
print(list)

list.remove(4) #first occurence of element
print(list)

#list comprehension
newList = [i for i in range(5)]
print(newList)