
open("file2.txt","x")

data="this is content of the data 007"


f=open("file2.txt","w")
f.write(data)
f.close() 

f=open("file2.txt","a")
f.write("\n")
f.write(data)
f.close()


f=open("file2.txt","r")
data=f.read().split("\n")
print(data)
f.close()
