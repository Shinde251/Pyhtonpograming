# Set Methods :

x={10,20,30,40,50}
print(x)

#1. add(): adds one element in a set at a time.

x.add(60) # adding 60 to set

print(x)

'''
x.add(10,20,30) # Error --> bcaz add() requires only one parameter
print(x)
'''

x.add((10,20,30)) # valid but taken as tuple
print(x)

#2. update() : adds multiple elements in a set at a time

x.update((70,80,90))
print(x)

#3. copy() :- copies one set in another set

a={'chetan','jay','raj'}
print("a :---> ",a)
b=a.copy()
print("b :---> ",b)

#4. pop() :- removes one element in set whichever is first.

print(x)
x.pop()
print(x)

x.pop()
print(x)

#5. remove() :- removes perticular element from Set.

#if element found remove it but if element not found then gives error

x.remove(60)

print(x)

'''
x.remove(100)  # gives Error
print(x)
'''
#6. discards() :- removes perticular eleemnt from Set.

# if element found remove it and if not found discards it(Error not occured).


x.discard(40)
print(x)


x.discard(100)  # Error does not occures
print(x)


#7. clear() :- clear all element in set

x.clear()

print(x)












