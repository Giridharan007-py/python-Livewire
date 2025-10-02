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
