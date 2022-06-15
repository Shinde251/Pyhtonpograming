
# Printing Sum of Even number form range 1 to 10 numbers using if condition


i=0                               # initialization
sum=0
while i<=10 :                     # condition

    if (i%2==0):
        print(i)
        sum=sum+i
    i=i+1                         # step


print("Sum : ",sum)              # defeault stmts executes only once
