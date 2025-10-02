# CHECK THE AMSTRONG NUMBER WITHOUT LOOP

a=int(input("Enter a number:"))
b=a%10
c=a//10
d=c%10
e=c//10
#print("The reversed number:",b,d,e,sep="")
if((e**3)+(d**3)+(b**3)==a):
    print("The given number is ADAM number")
else:
    print("The given number is not a ADAM number")

