# List is Mutable object but elemetns of list can be mutable or immutable


x=[(10,20,30),[40,50,60],[70,80,90]]

print("Origional List as\n",x)


#x[0][0]="Python" #gives error

#x[0][1]="Java" #gives error

#x[0][2]="CPP" #gives error


x[1][0]="Jay"
x[1][1]="Chetan"
x[1][2]="Ashish"
x[2][0]="Nikita"
x[2][1]="Bhageshri"
x[2][2]="Raj"

print("\nAfter Modifiacation \n",x)

