dict = {
    "name": "Abc",
    "marks": [90,92,96]
}
#mutable

print(dict["marks"])

dict["name"] = "xyz"
print(dict)

dict["age"] = 100
print(dict)

null_dict = {}

student = {
    "name": "ABC",
    "scores": {
        "math": 90,
        "physics": 94,
        "chemistry": 85
    },
    "age": 18
}
print(student)
print(student["scores"]["math"])

#print keys
print(student.keys())

#print values
print(student.values())

#print pairs (as tuples)
print(student.items())

#no. of key value pairs
print(len(student))

#print(student["non_existent_key"])  #gives error
print(student.get("non_existent_key")) #returns None
#both perform same task

student.update({"city": "nagpur"})