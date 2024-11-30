new_file=open('New_file.txt','x')
new_file.close()


import os
print("Check if the file exists or not...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
    
else:
    print("The file doesn't exist.")
    
new_file=open('New_file.txt','w')
new_file.write("Hello! I am Apshara Tasnim.I am from Bangladesh.")
new_file.close()

os.remove('codingal.txt')

os.rmdir('File handling')