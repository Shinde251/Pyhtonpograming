# String to other type casting

x='10'

a='jay'

print(x, type(x))


# Converting str to int

y=int(x)

print(y, type(y))


# Only valid string can be converted into int types
# ex:-  x='10'  ---> this is valid string and it can convert into int type
# Invalid string can not be converted into int types
# ex:  x='VIP' ----. this is Invalid string and it can not be convert into int type
# if you try this ValueError Occured.

#p=int('VIP') #-->gives error



# String to float convertions
y=float(x)

print(y, type(y))



# String to bool

z=bool(x)

print(z,type(z))


'''
a=bool('0')
print(a)
'''



