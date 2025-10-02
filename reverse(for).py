# REVERSE THE GIVEN NUMBER USING FOR LOOP

num=int(input("Enter a number:"))
reverse=0
original=num
num_digit=len(str(num))
for i in range(num_digit):
    digit=num%10
    reverse=reverse*10+digit
    num//=10
print("The reversed number of ",original,"is",reverse)



# REVERSE TNE STRING USING FOR LOOP

string=input("Enter a string:")
rev_string=''
for i in string:
    rev_string=i+rev_string
print("The revresed string:",rev_string)

