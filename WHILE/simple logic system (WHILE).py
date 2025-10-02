# SIMPLE LOGIC SYSTEM

i=0
user_name=input("Enter user name:")
password=input("Enter password:")
while(user_name!="admin1234" and password!="1234"):
    print("Something went wrong, please try again")
    user_name=input("Enter user name:")
    password=input("Enter password:")
    i+=1
    if(i==2):
        print("YOU TRY TOO MUCH TIMES, TRY LATER")
        break
if(user_name=="admin1234" and password=="1234"):
    print("YOU LOGGED IN")

