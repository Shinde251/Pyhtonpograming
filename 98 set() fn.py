# Creating Set by using set()
'''
set() is pre-defined fn
which is used to create set.
This fn takes zero or only one arugement and
return set.
That argument must be iterable types like string, list, tuple and set etc.

'''

#creating empty set

a=set()
print(a,type(a))

#crating set with string
b=set("Python")
print(b, type(b))

'''
c=set("python","java") # Error ser requires 0 or 1 argument and here got 2
print(c, type(c))'''

# creating set with list

d=set([10,20,30])
print(d, type(d))

#e={[]} #gives Error


#creating set with tuple

f=set((40,50,60))
print(f, type(f))

# creating set with set

g=set({70,80,90})
print(g,type(g))


#h={{70,80,90}} # gives Error







