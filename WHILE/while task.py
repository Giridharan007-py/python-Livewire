# 1) Amstrong Number

num = int(input("Enter a 3-digit number: "))
original = num
sum = 0

while num > 0:
    digit = num % 10
    sum += digit ** 3
    num = num // 10

if sum == original:
    print(f"{original} is an Armstrong number.")
else:
    print(f"{original} is not an Armstrong number.")

# 2) Keep asking for a password until it's correct

password = ""
while password != "secret123":
    password = input("Enter the password: ")
print("Access granted!")

# 3) Sum numbers until the user types 0

total = 0
number = int(input("Enter a number (0 to stop): "))
while number != 0:
    total += number
    number = int(input("Enter a number (0 to stop): "))
print("Total sum is:", total)

# 4) Countdown from 5 to 1

count = 5
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Blast off!")


# 5) Print only even numbers between 1 and 20

num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1

# 6) Simple login system (3 tries only)

correct_username = "admin"
correct_password = "1234"
tries = 0
while tries < 3:
    username = input("Username: ")
    password = input("Password: ")
    if username == correct_username and password == correct_password:
        print("Login successful!")
        break
    else:
        print("Incorrect. Try again.")
        tries += 1
if tries == 3:
    print("Too many attempts. Access denied.")

# 7) Simulate a basic calculator (until user exits)

while True:
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    if op == "+":
        print("Result:", num1 + num2)
    elif op == "-":
        print("Result:", num1 - num2)
    elif op == "*":
        print("Result:", num1 * num2)
    elif op == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")
    else:
        print("Unknown operator")

    again = input("Do you want to continue? (yes/no): ")
    if again.lower() != "yes":
        break

# 8) Create a multiplication table for a given number

num = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

















