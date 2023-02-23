from tkinter import filedialog
from tkinter import *

#title=name --> name for window 
#initialdir --> define default directory  --> entekhab directory pishfarz 
# directory = filedialog.askdirectory(title='sajjad', initialdir='M:\\test\\sajjad')
# print(directory) # mesir oon folder ra neshan midehad

#_________________________________________________________________

# win = Tk()
# #initialfile--> mesir file pishfarz khodeman ra moshakhas mikonim
# #mode -->read/write/append  --> r , w , a
# file = filedialog.askopenfile(title='askopenfile',initialdir='M:\\test\\sajjad',initialfile='M:\\test\\sajjad\\sajjad.txt',mode='c')
# file = filedialog.askopenfilename(title= 'askopenfilename',initialdir='M:\\test\\sajjad') # karbord kamtar nesbat be askopenfile
# print(file)

# win.mainloop()

#_____________________________
# filetypes  --> yek list ast az tuple ha ke dar tuple ha name , no pasvand miad 
listtype = [('textfile','.txt'),('textfile','.doc'),('textfile','.pdf'),('python','.py'),('all files','.*')]
files = filedialog.askopenfiles(title='temsah',filetypes=listtype,)
for file in files:
    print(file.name)

# filedialog.askopenfilenames()