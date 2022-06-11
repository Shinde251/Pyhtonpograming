# Tuple Addresses 1

a=[1,2,3,4]
b=[1,2,3,4]

print(a, type(a), id(a))
print(b, type(b), id(b))

print(a is b) # False

print(a==b) # True

print(a[0]==b[0]) # True

print(a[0] is b[0]) # True

# For All Mutable objects if content is same or different then different(multiple)
# objects are crated.


x=(1,2,3,4)
y=(1,2,3,4)


print(x, type(x), id(x))
print(y, type(y), id(y))
  
print(x is y)  #True

print(x==y) # True

print(x[0]==y[0]) # True

print(x[0] is y[0]) # True


# For All Immutable object if content is Same then only one object is Crated.


p=(1,2,[3,4])
q=(1,2,[3,4])

# Here Two tuple data is Same but here modification is allowed so two different
# objects are crated.

print(p, type(p), id(p))
print(q, type(q), id(q))

print( p is q) # False
print(p==q) # True
print(p[0] is q[0]) #True

print(p[0]==q[0]) # True
















