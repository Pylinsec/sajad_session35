from tkinter import filedialog

# f1 = filedialog.askdirectory()
# print(f"askopendirectory --> {f1} --> noe --> {type(f1)}")# x
# f2=filedialog.askopenfile()
# print(f"askopenfile --> {f2} --> noe --> {type(f2)}")
# f3 = filedialog.askopenfilename() # x
# print(f"askopenfilename --> {f3} --> noe --> {type(f3)}")
# f4 = filedialog.askopenfiles()
# print(f"askopenfiles --> {f4} --> noe --> {type(f4)}")
# f5 = filedialog.askopenfilenames()#x
# print(f"askopenfilenames --> {f5} --> noe --> {type(f5)}")


#_______________________________________________
# save = filedialog.asksaveasfile(defaultextension='.pdf', mode='w')
listtype = [('textfile','.txt'),('textfile','.doc'),('textfile','.pdf'),('python','.py'),('all files','.*')]
save = filedialog.asksaveasfilename(defaultextension='.pdf',filetypes=listtype ,)