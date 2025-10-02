
user_name=input("Enter user name:")
password=input("Enter password:")
if(user_name=="admin1234" and password!="1234"):
    print("Enter a valid password")
elif(user_name!="admin1234" and password=="1234"):
    print("Enter a valid user name")
elif(user_name!="admin1234" and password!="1234"):
    print("something went wrong")
else:
  print("You have logged in")

'''
user_name=input("Enter the user name:")
password=input("Enter the password:")
while(password!="1234"):
    print("The password is wrong")
    print("Try again")
    password=input("Enter the password:")
if(password=="1234"):
    print("You logged in")
'''
'''
num=1
number=0
while(num!=0):
    num=int(input("Enter a number:"))
    number=number+num
print("SUM:",number)
'''


'''
a=int(input("Enter a number A:"))
b=int(input("Enter a number B:"))
c=input("Enter the operation:")
while(c!="exit"):
    if(c=="+"):
        print(a+b)
        c=input("Enter the operation:")
    elif(c=="-"):
        print(a-b)
        c=input("Enter the operation:")
    elif(c=="*"):
        print(a*b)
        c=input("Enter the operation:")
    elif(c=="/"):
        print(a/b)
        c=input("Enter the operation:")
    elif(c=="%"):
        print(a%b)
        c=input("Enter the operation:")
    elif(c=="//"):
        print(a//b)
        c=input("Enter the operation:")
    elif(c=="**"):
        print(a**b)
        c=input("Enter the operation:")
    else:
        pass
if(c=="exit"):
    print("The work is done")
'''

# count out from 5 to 1
'''
num=int(input("Enter a number:"))
while(num!=0):
    num=num-1
    print(num)
''' 
    






































