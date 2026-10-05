a = [10,"ashish", "kumar", "data", "science",29,True,False]

# list array jaise he hota hai lekin isme diffrent type of data store kar sakte hai joki array mai possible nahi hai 

# slice in list

# slice = a[2:7:1]
# print(slice)

# # reverse a list

# print(a[::-1])

# looping in list 


# for ele in a :
#     print(ele)
#     if(ele == "data"):
#         break


# modify in Lists 

# # last mai add krta hai 
# a.append(True)

# # jis jagah man us jagah insert kr sakte hai isko 2 chiz dena padta hai 1 kaha par insert karna hai 2 kya insert krna hai 
# a.insert(1,"kya haal chal hai ji ")

# # remove krne le liye agar same chiz 2 baar hai list mai tou sirf 1st baar wale ko remove krega

# a.remove("kya haal chal hai ji ")

# # pop eek method hai joki last wale ko hat dega or wo return krega 

# print(a.pop())


# # Replace krna hai tou reassign kr denge 

# a[0] = 1000
# print(a)

# Nasted List


# list = ["a",12,23,["ashish",True,False],"modi","modi"]


# print(list[3][2])


# Unpacking List

# agar value list ke andar jyada hai unpacking krte waqt to error aayega lekin agar hum * lga de 
# bache hue saare list last wale variable ke andar chale jayege
# output -> 10 20 [30, 50, 400]
point =[10,20,30,50,400]
x,y,*z = point

print(x,y,z)
