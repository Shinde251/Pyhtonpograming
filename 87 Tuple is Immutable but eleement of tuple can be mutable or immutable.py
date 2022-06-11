# Tuple is Immutable object but elements of tuple can be mutable of immutable

x=((10,20,30),[10,20,30],10,20,30)

print(x)

#x[0]=100 # Error--> Tuple element can not be modify

#x[0][0]=200 # Error--> x[0][0] is Tuple element element which does not modification


#x[1]=300 # Error--> x[1] is Tuple elelement

x[1][0]="Python" # Valid--> x[1][0] is tuple element element which allows modification

print(x)


