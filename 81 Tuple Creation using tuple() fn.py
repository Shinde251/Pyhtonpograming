# Creating Tuple using tuple() fn
'''
tuple:-
    This is pre-defined fn
    This fn is used to create a tuple.
    This fn takes 0 or 1 argument and return tuple
    That arguement should be iterable type only.
    like str, list, tuple, set etc. '''

a=tuple() # emtpty tuple

print(a, type(a), len(a))

b=tuple("Python")  # tuple creation using str

print(b, type(b),len(b))


c=tuple([10,20,30,40])  # tuple creating using list

print(c, type(c))


e=tuple((60,70,80,90)) # tuple creating using tuple
print(e, type(e))


f=tuple({100,200,300,400}) # tuple creating using set
print(f, type(f))

'''
h=tuple(10)  # Error-- tuple arguement must iterable type only like str,set,list,tuple etc
             # here 10 is int and int is not a Iterable object


print(h, type(h))
'''



'''
c=tuple("Python","Java") #Error --tuple expected at most 1 argument, got 2
print(c, type(c))

'''






