# Creating Dictionary using {}

a={}  # empty dictionary
print(a, type(a))

'''
a={10}
print(a, type(a))  # Set Created not dictionary
'''

# Homogeneous Keys and Homogeneous values
b={"name":"jay", "city":"Jalgaon","class":"Python"}
print(b, type(b))

d={"chetan":80, "jay":85, "raj":90}
print(d, type(d))


# Hetrogeneous  Keys and Hetrogeneous values

c={"name":"Jay", 5:"height" , "weight":55.2}
print(c, type(c))

# Duplicate keys not allow but values allow

e={'a':10, 'b':20, 'a':30, 'a':40 , 'c':40}
print(e, type(e))









