with open ('codingal.txt','w') as file:
    file.write("Hi! I am a student of codingal.I really enjoy programming,")
    file.close()
    
with open ('codingal.txt','r') as file:
    data=file.readlines()
    print("Words in the file are...")
    for line in data:
     word=line.split()
     print(word)
file.close()    