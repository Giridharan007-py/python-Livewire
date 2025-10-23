def fibonaaci():
    n=int(input("Enter a number:"))
    a=0
    b=1
    i=0
    while (i<n):
        print(a)
        a,b=b,a+b
        i+=1
fibonaaci()
