# THE MULTIPLICATION TABLE FOR THE GIVEN NUMBER 

num=int(input("Enter a number:"))
while(num!=0):
    print(num,"TABLE")
    for i in range(1,1010):
        print(i,"x",num,"=",i*num)
    break



