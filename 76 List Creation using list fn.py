# Creating List using list() fn.
'''
This is pre-defined fn which is used to create a list.
This fn takes 0 or  1 arguement.
That arguemnent should be iterable type only.
like string, list, set, tuple etc.
'''



# Empty List Created

a=list()  
print(a, type(a), len(a))


# Creating List by passsing String

b=list("python")

print(b, type(b), len(b))


'''
c=list("python","java") # list() fn requires 0 or 1 arguement and here got 2
print(c, type(c), len(c))
'''

c=list("python ,java")
print(c, type(c), len(c))

# Creating List by passing List

d=list([10,20,30,40])

print(d, type(d), len(d))

# Creating List by passing Tuple

e=list((70,80,90))

print(e, type(e),len(e))

# Creating List by passing Set

f=list({100,200,300,400})

print(f, type(f), len(f))

'''

g=list(10)  # give Error
print(g,type(g),len(g))
'''





