
# Printing Sum of Even number form range given range using if condition



start=int(input("Enter start value : ")) # initialization
stop=int(input("Enter stop value : "))


                               
sum=0
while start<=stop :                     # condition

    if (start%2==0):
        print(start)
        sum=sum+start
    start=start+1                        # step


print("Sum : ",sum)              # defeault stmts executes only once
