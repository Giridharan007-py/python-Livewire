# write a program to remove a duplicates from list
'''
numbers = [4, 2, 7, 2, 5, 4, 9, 1, 5]
original_numbers = []
for num in numbers:
    if num not in original_numbers:
        original_numbers.append(num)
print(sorted(original_numbers))
'''

# write a program to find the sum of list
'''
total=0
numbers=[5,7,3,8,9,1,4,6,2]
even_num=[]
odd_num=[]
for num in numbers:
    total=total+num
    if(num%2==0):
        even_num.append(num)
    else:
        odd_num.append(num)
print("Sum of the list:",total)
print("The smallest number:",min(numbers))
print("The biggest number:",max(numbers))
print("The sorted list:",sorted(numbers))
print("The EVEN numbers:",sorted(even_num))
print("The ODD numbers:",sorted(odd_num))
'''


# write a program to get a list of name,place,age and print the particular person data using index value without using function

name=[]
place=[]
age=[]
count=int(input("How many people do you want to enter:"))
for i in range(count):
    na=input("Enter your name:")
    pl=input("Enter your place:")
    ag=int(input("Enter your age:"))
    name.append(na)
    place.append(pl)
    age.append(ag)
print(name,place,age,end="\n")
for i in range(count):
    if(age[i]>18):
        print(name[i],place[i],age[i])
    

























































