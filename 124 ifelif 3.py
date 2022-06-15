# Display Max numnber from two numbers. if both numbers are equal then
# diplay equal message


x=int(input("Enter 1st number : "))
y=int(input("Enter 2nd number : "))

if x==y:
    print("Equal")
elif x>y:
    print(x," is Max number")
else:
    print(y," is Max number")
