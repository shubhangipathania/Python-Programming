f=open("file.txt",'r')
data=f.read()
print(data)
f.close()

f1=open("file.txt",'w')
f1.write("Happy Holi Sabko.")
f1.close()