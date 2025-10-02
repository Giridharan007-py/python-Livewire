
# write a program to replace a vowel letter by "@" using for loop in string and using replace() function

vowels=['a','e','i','o','u','A','E','I','O','U']
def vowel(string):
    for i in vowels:
      string=string.replace(i,"@")
    print("modified string:",string)
vowel("giridharan")
print(type(vowels))
