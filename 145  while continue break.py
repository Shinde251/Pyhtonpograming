# while continue and break


# only three attempt

cnt=0

while True:

    cnt=cnt+1
    if cnt==4:
        break
    
    user=input("Enter User Name : ")

    if user!='Chetan':
        continue
    password=input("Welcome Chetan now enter your password : ")

    if password=="VIP":
        break

    
        

if cnt==4:
    print("Try after 24 hours")
else:
    print("Your are Authenticated User")
