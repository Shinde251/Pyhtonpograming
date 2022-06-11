#List Functions

x=[10,50,30,40,20]

print(x)

print(sum(x))
print(max(x))
print(min(x))
print(sorted(x)) # return sorted list as [10,20,30,40,50]
print(reversed(x)) # object created and return that object address.


for p in reversed(x):
    print(p,end=" ")



print()

for p in reversed(sorted(x)):
    print(p,end=" ")

    
