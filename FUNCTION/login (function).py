def old_user():
    user_name=input("Enter the the user name:")
    password=input("Enter the password:")
    if(user_name=="admin1234" and password!="1234"):
        print("Enter a valid password")
    elif(user_name!="admin1234" and password=="1234"):
        print("Enter a valid user name")
    elif(user_name!="admin1234" and password!="1234"):
        print("something went wrong")
    else:
        print("You have logged in")
def new_user():
    phone=int(input("Enter your phone number:"))
    user_name=input("Enter the the user name:")
    password=input("Enter the password:")
    re_password=input("Enter the password once again:")
    if(password==re_password):
        print("You signed in")
    else:
        print("Check the password")
print("(A) Old user     (B)New user")
user=input("Enter the user type:")
if(user=="A" or user=="a"):
    old_user()
elif(user=="B" or user=="b"):
    new_user()
else:
    print("Enter a valid user type")
