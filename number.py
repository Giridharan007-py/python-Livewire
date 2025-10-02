'''number=int(input("Enter a number:"))
if(number<=100):
    if(number%2==0):
        print("The given number is EVEN" )
    else:
        print("The given number is ODD")
else:
    print("The given number is in out of range")
'''
#Loops
'''
for i in range(1,10):
     print(i)
'''

txt="Python"
for i in txt:
    print(i)


'''    
for i in range(1,101):
    if(i%2==0):
        print(i)
    
'''
'''
for i in range(101,1,-1):
    if(i%2==0):
        print(i)
'''

string=input("Enter a string:")    
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        print(i)
    else:
        pass

'''
for i in range(3):
    name=input("Enter a name:")
    age=int(input("Enter your age:"))
    place=input("Enter the place:")
    print(name)
    print(age)
    print(place)

'''
'''
a=int(input("Enter a number:"))
for i in range(a):
    print('*'*i)
'''
'''
a=0
for i in range(1,101):
    a=a+i
print(a)
'''
'''
a=0
string=input("Enter a string:")    
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        print(i)
        a=a+1
print("Number of vowels:",a)
length=len(string)
print("Number of consonent:",length-a)
'''
'''
a=1
for i in range(1,11):
        a=a*i
        print("The factorial of",i,"=",a)
'''

'''
a=int(input("Enter a number:"))
for i in range(a,0,-1):
    print('*'*i)
'''

'''
a=int(input("Enter a number:"))
for i in range(a):
    print(' '*(a-i)+'*'*i)

'''

'''
for i in range(1,101):
    if(i%3!=0):
        print(i)
'''

















