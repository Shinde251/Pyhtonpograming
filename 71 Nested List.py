# Nested List :- A list within another list is called as nested list

x=[[10,20,30],[40,50,60],[70,80,90]]

print(x, type(x), len(x))



print(x[0])  # Accessing 1st list 

print(x[1])  # Accessing 2nd list

print(x[2])  # Accessing 3rd list 

print(x[0][0] ) # 10
print(x[1][0])  #40
print(x[2][0])  # 70


print("\nAccessing List Elemets using for loop ")

for p in x:
    print(p)

print("\nAccessing List element's elements using for loop")

for p in x:
    for q in p:
        print(q)
        


