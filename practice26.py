f=open("poem.txt",'r')
text=f.read()
print(text)
if('twinkle' in text):
    print("The word twinkle is present.")
    print(text.find('twinkle'))
else:
    print("The word twinkle is not present.")

f.close()