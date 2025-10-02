# While

i=0
while(i<=20):
    i+=1
    if(i==10 or i==20):
       continue
    print(i)


# fibonacci series
'''
n=int(input("Enter a number:"))
a=0
b=1
i=0
while (i<n):
    print(a)
    c=a+b
    a=b
    b=c
    i+=1

'''

# fibonacci series

'''
n=int(input("Enter a number:"))
a=0
b=1
i=0
while (i<n):
    print(a)
    a,b=b,a+b
    i+=1
'''



# REVERSE THE GIVEN NUMBER 
'''
num = int(input("Enter a number: "))
reversed_num = 0
while (num!=0):
    digit = num % 10            # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Append it to the reversed number
    num = num // 10             # Remove the last digit
print("Reversed number:", reversed_num)

'''

























































