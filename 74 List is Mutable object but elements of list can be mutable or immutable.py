# List is Mutable object but elemetns of list can be mutable or immutable


x=[(10,20,30),[40,50,60],[70,80,90]]

print("Origional List as\n",x)


#x[0][0]="Python" #gives error



x[0]="Python"

x[1]="Java"

x[2]="CPP"

print("\nAfter Modifiacation \n",x)

