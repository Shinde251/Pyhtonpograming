# while continue and break


while True:
    user=input("Enter User Name : ")

    if user!='Chetan':
        continue
    password=input("Welcome Chetan now enter your password : ")

    if password=="VIP":
        break

print("Your are Authenticated User")
