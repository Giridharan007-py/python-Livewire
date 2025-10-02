
# CHECK THE AMSTRONG NUMBER USING WHILE LOOP

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

