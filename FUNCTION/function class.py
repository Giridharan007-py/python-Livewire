# Creating a Function&Call it
'''
def my_function():
print("Hello")
my_function()

def me():
    print("Name:giri")
    print("Place:manalmadu")
    print("Age:17")
me()
'''
#Arguments
def my_function(fname):
  print(fname + " dhoni")

my_function("M.S")
my_function("captain")
my_function("THALA")

def add(a,b):
  print(a+b)

add(2,5)

#Arbitrary Arguments, *args
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("giri", "dharun", "siva")

#Keyword Arguments
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "giri", child2 = "dharun", child3 = "siva")





