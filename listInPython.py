a = ["ashish", "kumar", "data", "science",29,True,False]

# list array jaise he hota hai lekin isme diffrent type of data store kar sakte hai joki array mai possible nahi hai 

# slice in list

slice = a[2:7:1]
print(slice)

# reverse a list

print(a[::-1])

# looping in list 


for ele in a :
    print(ele)
    if(ele == "data"):
        break