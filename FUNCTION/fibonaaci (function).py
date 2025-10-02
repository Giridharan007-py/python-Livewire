def fibonaaci():
    n=int(input("Enter a number:"))
    a=0
    b=1
    i=0
    print(a)
    while (i<n):
        a,b=b,a+b
        i+=1
        print(a)
fibonaaci()
