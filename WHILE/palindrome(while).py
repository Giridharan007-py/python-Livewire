# PALINDROME FOR THE GIVEN NUMBER

num=int(input("Enter a number:"))
number=num
reversed_num = 0
while (num!=0):
    digit = num % 10            
    reversed_num = reversed_num * 10 + digit
    num = num // 10            
print("Reversed number:", reversed_num)
if(reversed_num==number):
    print("The given number is palindrome")
else:
    print("The given number is not a palindrome")


# PALINDROME FOR THE THE GIVEN STRING

string=input("Enter a string:")
rev_string=''
x=len(string)-1
while(x>=0):
    rev_string+=string[x]
    x-=1
print("Reversed string:",rev_string)
if(rev_string==string):
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")


