
# write a program to find a positive and negative numbers in  the series using arbitrary arguments using for loop

def number(*num):
    print("The positine numbers:")
    for i in num:
        if(i>=0):
            print(i)
    print("The negative numbers:")
    for i in num:
        if(i<0):
           print(i)
number(1,-2,3,-4,5,-6,7,-8,9,-10)
