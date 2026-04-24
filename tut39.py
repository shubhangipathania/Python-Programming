f = open('file5.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


f = open('myfile.txt', 'w')
lines = ['good day sabko\n', 'have a great day\n', 'may god bless you\n']
f.writelines(lines)
f.close()

f=open('file5.txt','r')
content=f.read()
print(content)
f=open('file5.txt','r')
content1=f.readlines()
print(content1)

