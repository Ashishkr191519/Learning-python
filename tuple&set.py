

# list kesa hota hai -> l = [] ye ho gya aapka list


# tuple sikhte hai  -> () likhen par tupple ho jata hai nesting bhi ho sakte hai list ke tarah

# Indexing slicig same hote hai list ke tarah
# Tuple list se alag kyu hai -> list mutable hota hai Tuple Unmutable hota hai


t1 = (12,54,True,"Hello",(67,3453,False))
# reverse kr dega ye
# print(t1[::-1])

# reassign krke dekhte hai 

# t1[0] = 131
# TypeError: 'tuple' object does not support item assignment ye error aayega ki reassign nahi kr sakte
# eek ke value rakhoge tou wo class int ke tarah use treat krega 2 value hona kam se kam jarruri hai ya 
# (5,) -> ye krne se bhi tuple bn jata hai bina 2 value diye
# tuple comma ke karan hota hai paranthesis ke karan nahi
# tuple tab use krte hai jab kabhi bhi data change na krna ho -> coordinates,RGB esse jagah use krte hai
# safty ke requirement ke karan
# print(t1)

# # tuple packing -> jisme hum multiple data dalte hai bina paranthesis lgaye hue tou use packing bolte hai

# t2 = 12,False,True,"Ashish"
# # output ye aayega -> <class 'tuple'>
# print(type(t2))

# # Tuple unpacking dekhte hai 
# # output ye hoga -> 12 False True Ashish isi ko kehte hai unpacking
# a,c,v,d = t2
# print(a,c,v,d)


# list and tuple are ordered and allow duplicates only diffrence is tuple is immutable only 


# SETS -> 

# Set unordered hota hai or duplicate item allow nahi krta saare values unique hone chahiye ye bhi mutable hota hai
# set likhne ke liye -> {}
# niche wale set mai duplicate hai dekhte hai output kya aata hai
s1 = {12,13,13,14,14,145,154,1656,546,4564} 
# output -> isne error nahi diya -> {546, 12, 13, 14, 145, 4564, 1656, 154} khud he duplicates hta diye
# lekin koi order nahi hota ouput ka issiliye unordered hota hai
print(s1)

# Sets mai indexing nahi hota hai uske element ko index se access nahi kr sakte hai
# loop krke dekhte hai 

# for ele in s1:
#     print(ele)

# loop sahi se kaam kr raha hai

# sets mai adding and removing 
# add se add hoga
# .remove se remove hoga -> error ho jayega if missing value ko remove krne gye tou
# .discard -> ye error nahi dega hoga tou hta dena nahi tou no error

# s1.add(8999)
# s1.remove(546)
# s1.discard(1)

# print(s1)

# union padte hai -> | ye krnse se do sets ko merge kr dena
# intersection -> & ye lagane se intersection ho jayega dono sets mai jo comman value hai wo eek ne set mai retun hogi
# diffrence -> - lagane se diffrence hoga a - b esse tou jo value unique hongi a mai b ke compare mai usko return kr deta  
# symmatric -> ^ -> ye lagane se hoga isme dono set mai jo unique value hai uska new set bn jayega
s2 ={98,894,6327,8309280,9090}
# output -> {8309280, 546, 98, 9090, 12, 13, 14, 145, 4564, 6327, 1656, 154, 894} merge ho gya unordered

print(s1 | s2)

new_set = s1 & s2
# output -> set() kyuki dono mai saare value unique hai
print(new_set)


# set ko immutable bnane ke liye frozenset -> use krte hai 
# set fast lookup hota hai tuple or list se fast hota hai value dundne mai (Hashtable ka use krta hai sets)
frozenset(s1)
