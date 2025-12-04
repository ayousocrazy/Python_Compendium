import os
os.chdir(r"C:\Users\HP\Desktop\Python\Concepts\Advanced") # change the working directory if python cannot find the file

doc = open('Example.txt', 'r') # open a file in read mode
print(doc)
content = doc.read() # read the entire context 
print(content)

print(doc.readline()) # when you read from a file, the internal file pointer moves forward
# So this won't print anything as the pointer is now at the end of the file

doc.seek(0) # moves the internal pointer to the top
print(doc.readline())
print(doc.readline())

for i in doc:
    print(i)

doc.close()

# -------------------------------------------------------------------------------------------------------------------------

f = open('Doc.txt', 'w') # open file in write mode(open a new file if file doesn't exist and replaces if exists before)

f.write(content) # writes the content of Example.txt to Doc.txt

f.close()

# -------------------------------------------------------------------------------------------------------------------------

f = open("Example.txt", 'a') # open file in append mode(open a new file if file doesn't exist and adds content instead of replacing)

pr = "\nPractice makes perfect"
f.write(pr)

f.close()

# -------------------------------------------------------------------------------------------------------------------------

with open('Example.txt', 'r') as txt: # Using with you dont have to manually close the file it closes automatically
    print(txt.read())