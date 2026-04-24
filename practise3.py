# Print all the files folders and contents of any directory using the os module.

import os

directory_path= r'C:\Users\HP\Desktop\web dev'


contents=os.listdir(directory_path)
for items in contents:
    print(items)