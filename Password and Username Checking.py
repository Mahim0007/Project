username=(input("Enter your username: "))
password=(input("Enter  your password: "))
if username == "username":
    if password == "password":
        print("Your access is granted.")
    elif password == '1234':
        print("Weak password.")
    else:
        print("Password is incorrect.")
else:
     if username == 'guest':
         if password == 'guest':
             print("Your access is granted.")
         else:
             print("Password is incorrect.")
     else:
        print("Unknown  user.")