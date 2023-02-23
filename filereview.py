from tkinter import filedialog

files = filedialog.askopenfilenames()
print(files)
for file in files:
    print(file)
    with open(file,'w') as f:
        f.write(f"{file} \n sajjad ")
              
# with open('sajjad.txt','r') as file:
#     print(file.readline(10))

# file.read() -->  harche dakhel file bood miareh
# file.readline -->  karkard ba character
# file.readlines() --> list barmigardand ke har line yek ozv on hast 