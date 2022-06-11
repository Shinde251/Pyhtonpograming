# Set is Mutable object but elements of Set should be Immutable only.

a={(10,20,30)}  # Tuple can be a Set element
print(a)



#b={[10,20,30]} # List can not be a Set elements
#print(b)


#c={{10,20,30}}  # Set can not be a Set element
#print(c)


'''
d=[[],[],[]]---> Valid
e=((),(),())---> Valid
f={{}, {}, {}}-> Invalid bcaz set is Mutable object and set allows only Immutable eleemnts.
h={[],[],[]}---> Invalid
i={(),(),()}---> Valid '''
