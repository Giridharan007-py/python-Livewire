
#Key Takeaways
#try :lets you test code for errors.
#except : handles specific or general exceptions.
#else :runs if no errors occur.
#finally :runs always (good for cleanup tasks).
#raise: is used to manually throw exceptions               


try:
    
    print(x)
except:
    print("an error occured")



try:
   
    b=10+a
except NameError:
    print("variable a is not defined")
except:
    print("something went wrong")


    
try:
    w=10
    print(w)
except:
    print("something went wrong")
else:
    print("nothing went wrong")



    
try:
    print(w)
except:
    print("something went wrong")
else:
    print("nothing went wrong")    





try:
    print(x)
except:
    print("something went wrong")
else:
    print("nothing went wrong")
finally:
    print("the 'try except' is finished")





#raise exception
a="hello"
assert a=="hello"





try:
    num = int(input("Enter a number: "))
    result = 10/num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input!")
else:
    print(f"Success! Result is {result}")
finally:
    print("Execution complete.")














    
