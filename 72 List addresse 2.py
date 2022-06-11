# List Addresses 2

a=[1,2,3,4]
b=[1,2,3,4]



print(a, type(a), id(a))
print(b, type(b), id(b))


print(a is b) # False

print(a==b) # True

# Note :- For All Mutable objects if content is same or different then
#         different objects are crated.

print(a[0], id(a[0]))
print(b[0], id(b[0]))

print(a[0] is b[0]) # True

print(a[0]==b[0]) # True

jay=1

print(jay is a[0]) #True







      
    
