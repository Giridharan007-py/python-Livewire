# FIND THE BIGGEST NUMBER BETWEEN THREE NUMBERS


a=int(input("Enter a number A:"))
b=int(input("Enter a number B:"))
c=int(input("Enter a number C:"))
if(a>b and a>c):
    print("A is greater than B and C")
elif(b>a and b>c):
    print("B is greater than A and C")
else:
     print("C is greater than A and B")
