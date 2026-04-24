#file handling in python
f=open('myfile.txt','r')
content=f.read()
print(content)
f=open('myfile.txt','a')
f.write("\nTrust the universe")
#f1=open('file1.txt','x')
f1=open('file1.txt','rb')
contents2=f1.read()
print(contents2)
f1.close()

f.close()

with open('myfile2.txt','r') as a:
    contents4=a.read()
    print(contents4)