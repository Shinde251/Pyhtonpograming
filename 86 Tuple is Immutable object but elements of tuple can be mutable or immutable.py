# Tuple is Immutable object but elements of tuple can be mutable of immutable

x=([10,20,30],[40,50,60],[70,80,90])

#x[0]=15 #Error

x[0][0]=101
x[0][1]="Chetan"
x[0][2]="Python"

#x[1]=25  # Error
x[1][0]=102
x[1][1]="Jay"
x[1][2]="Java"

#x[2]=30  # Error

x[2][0]=103
x[2][1]="Jay"
x[2][2]="Web Desinging"


print(x)
