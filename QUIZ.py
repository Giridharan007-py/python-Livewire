# QUIZ (KEEP ASKING FOR A CORRECT ANSWER)
# USING (if,elif,else)
score=0
print("WELCOME TO THE QUEST")
animal=input('''WHAT IS THE INDIA'S NATIONAL ANIMAL?
    (a)lion  (b)tiger  (c)elephant
    ANSWER:''')
if(animal=="b"):
    score+=1
    bird=input('''WHAT IS THE INDIA'S NATIONAL BIRD?
    (a)peacock  (b)parrot  (c)crow
    ANSWER:''')
    if(bird=="a"):
        score+=1
        flower=input('''WHAT IS THE INDIA'S NATIONAL FLOWER
    (a)lily  (b)rose  (c)lotus
    ANSWER:''')
        if(flower=="c"):
            score+=1
           pm=input('''WHO IS THE PRIME MINISTER OF INDIA?
    (a)modi  (b)seeman  (c)stalin
    ANSWER:''')
            if(pm=="a"):
                score+=1
                cm=input('''WHO IS THE CHIEF MINISTER OF TAMIL NADU?
    (a)vijay  (b)stalin  (c)seeman
    ANSWER:''')
                if(cm=="b"):
                    score+=1
                    print("You have passed")
                    
                else:
                    print("Enter a valid answer")
            else:
                print("Enter a valid answer")
        else:
            print("Enter a valid answer")
    else:
        print("Enter a valid answer")
else:
    print("Enter a valid answer")
print("You got ",score,"out of 5")





If you fail at something do not ever tell yourself that you have failed.
Tell yourself that you do not try your best yet.












