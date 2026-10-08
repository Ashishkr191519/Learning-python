# Dictonary in Pyhton
# dictionary -> {} isse bnaya jata hai same set bhi isse se bnaya jata hai
# diffrence ye hai ki isme key:value pair rakhe tou ye dictionary kahenge and nomal value tou set
# a = {"name": "Ravi", "age": 20}   # key: value pair → dict
# b = {1, 2, 3}                     # sirf values → set
# c = {}                            # kuch nahi → dict (default)



d1 = {
    "name":"Ashish",
    "age":23,
    "gender":"male",
    "person":"isGood"

}

print(d1["name"])
print(d1)

# dictionary mai key wahi ho sakta hai jo hashable ho jaise int,float,tuple, boolean etc. 
# list , sets -> unhashable hote hai 
# dictionary mai value find krne mai 0(1) time complexity lagega
