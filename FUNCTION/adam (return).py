# WRITE A PROGRAM TO FIND A ADAM NUMBER USING FUNCTIONS WITH RETURN STATEMENT

def adam(num):
    print("The number:",num)
    sqr=num**2
    return sqr
print("The square number:",adam(12))
def reverse(num):
    rev_num=0
    while(num!=0):
        digit=num%10
        rev_num=rev_num*10+digit
        num=num//10
    return rev_num
print("The Reversed square number:",adam(21))
print("The Reversed number:",reverse(12))
print("The Reversed square number:",reverse(144))
if(adam(21)==reverse(144)):
    print("The given number is ADAM number")
else:
    print("The given number is not a ADAM number")



