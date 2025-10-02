'''

1) GET DETAILS FROM STUDENT AND PRINT

2) GET INPUT FROM THE USER AND PRINT HOW MANY CHARACTER IN THE STRING

3) GET A STRING INPUT AND PERFORM A STRING OPERATION

4) CONSTRUCT SIMPLE CALCULATOR USING CONTROL FLOW STATEMENT

5) DESIGN A QUIZ COMPETITON 10 QUESTIONS
                            2 MARKS FOR CORRECT ANSWER
                           -1 MARK FOR WRONG ANSWER
                           
6) GET INPUT FROM n NUMBER OF STUDENT  AND PRINT IT USING LOOP

7) GET TWO STRING AS INPUT AND CONCATENATE IT
   THEN PRINT THE CONSONANT AND PRINT THE COUNT OF THE CONSONANT
   
8)  PRINT THE FOLLOWING PATTERN
    *
   * *
  * * *
 * * * *
'''

# 1) GET DETAILS FROM STUDENT AND PRINT
'''
name=input("Enter the student name:")
roll_no=int(input("Enter the roll number:"))
school=input("Enter the school name:")
tamil=int(input("Enter TAMIL mark:"))
english=int(input("Enter ENGLISH mark:"))
maths=int(input("Enter MATHS mark:"))
physics=int(input("Enter PHYSICS mark:"))
chemistry=int(input("Enter CHEMISTRY mark:"))
computer=int(input("Enter COMPUTER mark:"))
total=(tamil+english+maths+physics+chemistry+computer)
average=total/6
print("NAME:",name)
print("ROLL NO:",roll_no)
print("SCHOOL NAME:",school)
print("TOTAL:",total)
print("AVERAGE:",average)
'''

# 2) GET INPUT FROM THE USER AND PRINT HOW MANY CHARACTER IN THE STRING
'''
string=input("Enter a string:")
length=len(string)
print("Number of character in given string:",length)
'''

# 3) GET A STRING INPUT AND PERFORM A STRING OPERATION
'''
a=input("Enter a string:")
b=input("Enter a string:")
print(a.isupper())
print(b.islower())
print(a.upper())
print(b.lower())
print(a.title())
print(b.swapcase())
print(a.capitalize())
'''
# 4) CONSTRUCT SIMPLE CALCULATOR USING CONTROL FLOW STATEMENT
'''
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
operation=input("operation:")
if(operation=="+"):
    print(a+b)
elif(operation=="-"):
    print(a-b)
elif(operation=="*"):
    print(a*b)
elif(operation=="/"):
    print(a/b)
elif(operation=="//"):
    print(a//b)
elif(operation=="%"):
    print(a%b)
elif(operation=="**"):
    print(a**b)
else:
    print("something went wrong,please try again")
'''

# 5) DESIGN A QUIZ COMPETITON 10 QUESTIONS
                           # 2 MARKS FOR CORRECT ANSWER
                           # -1 MARK FOR WRONG ANSWER

print("WELCOME TO THE QUEST")
score=0
animal=input('''WHAT IS THE INDIA'S NATIONAL ANIMAL?
    (a)lion  (b)tiger  (c)elephant
    ANSWER:''')
if(animal=="b"):
    score+=2
else:
    score-=1
bird=input('''WHAT IS THE INDIA'S NATIONAL BIRD?
    (a)peacock  (b)parrot  (c)crow
    ANSWER:''')
if(bird=="a"):
    score+=2
else:
    score-=1
flower=input('''WHAT IS THE INDIA'S NATIONAL FLOWER
    (a)lily  (b)rose  (c)lotus
    ANSWER:''')
if(flower=="c"):
    score+=2
else:
    score-=1
pm=input('''WHO IS THE PRIME MINISTER OF INDIA?
    (a)modi  (b)seeman  (c)stalin
    ANSWER:''')
if(pm=="a"):
    score+=2
else:
    score-=1
cm=input('''WHO IS THE CHIEF MINISTER OF TAMIL NADU?
    (a)vijay  (b)stalin  (c)seeman
    ANSWER:''')
if(cm=="b"):
    score+=2
else:
    score-=1
print("SCORE:",score)                   


    
# 6) GET INPUT FROM n NUMBER OF STUDENT  AND PRINT IT USING LOOP
'''
for i in range(3):
    name=input("Enter a name:")
    age=int(input("Enter your age:"))
    place=input("Enter the place:")
    print(name)
    print(age)
    print(place)
'''

# 7) GET TWO STRING AS INPUT AND CONCATENATE IT
    #  THEN PRINT THE CONSONANT AND PRINT THE COUNT OF THE CONSONANT
'''
a=0
str1=input("Enter a string:")
str2=input("Enter a string:")
string=str1+str2
print("concadination:",string)   
for i in string:
    if(i!='a' and i!='e' and i!='i' and i!='o' and i!='u' and i!='A' and i!='E' and i!='I' and i!='O' and i!='U'):
        print(i)
        a=a+1
print("Number of consonant:",a)
'''

# 8) PRINT THE FOLLOWING PATTERN
'''
        *
       * *
      * * *
     * * * *
'''

a=int(input("Enter a number:"))
for i in range(a):
    print(' '*(a-i)+' *'*i)







