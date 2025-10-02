fun=input("Enter the function:")
def adam():
    num=int(input("Enter a number:"))
    sqr=num**2
    print("The square number:",sqr)
    rev_num = 0
    while (num!=0):
        digit = num % 10            
        rev_num = rev_num * 10 + digit  
        num = num // 10         
    print("The Reversed number:",rev_num)
    rev_sqr = 0
    while (sqr!=0):
        digit = sqr % 10          
        rev_sqr = rev_sqr * 10 + digit 
        sqr = sqr // 10
        sqr2=rev_num**2
    print("The Reversed square number:",sqr2)
    if(rev_num**2==rev_sqr):
        print("The given number is ADAM number")
    else:
        print("The given number is not a ADAM number")
def amstrong(): 
    n=int(input("Enter a number:"))
    org=n
    i=0
    while(n!=0):
        d=n%10
        i=i+(d**3)
        n=n//10
    if(i==org):
        print("Amstrong")
    else:
        print("Not an Amstrong")
def palindrome():
    num=int(input("Enter a number:"))
    number=num
    reversed_num = 0
    while (num!=0):
        digit = num % 10            
        reversed_num = reversed_num * 10 + digit
        num = num // 10            
    print("Reversed number:", reversed_num)
    if(reversed_num==number):
        print("The given number is palindrome")
    else:
        print("The given number is not a palindrome")
if(fun=="adam"):
    adam()
elif(fun=="amstrong"):
    amstrong()
elif(fun=="palindrome"):
    palindrome()
else:
    pass















    
