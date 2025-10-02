# KEEP ASKING FOR PASSWORD UNTIL THE USER ENTER THE CORRECT PASSWORD

user_name=input("Enter the user name:")
password=input("Enter the password:")
while(password!="1234"):
    print("The password is wrong")
    print("Try again")
    password=input("Enter the password:")
if(password=="1234"):
    print("You logged in")
