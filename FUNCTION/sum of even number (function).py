


'''
def number(*num):
    a=0
    b=0
    for i in num:
        if((i%2)==0):
            a=a+i
        else:
            b=b+i
    print("Sum of EVEN numbers:",a)
    print("Sum of ODD number:",b)        
number(1,2,3,4,5,6,7,8,9,10)
'''

def number(*num):
    a=0
    b=0
    for i in num:
        if((i%2)==0):
            a=a+i
        else:
            b=b+i
    print("Sum of EVEN numbers:",a)
    print("Sum of ODD number:",b)
    print("The even numbers:")
    for i in num:
        if((a>50) and (i%2)==0):
            print(i)
    print("The odd numbers:")
    for i in num:
        if((b>50) and (i%2)!=0):
            print(i)
number(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)










