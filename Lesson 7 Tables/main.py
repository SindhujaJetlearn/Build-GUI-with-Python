from tkinter import *
from tkinter.ttk import *
  
# Creating tkinter window 
window = Tk() 
window.title('Mathematical table generator')
  
# label text for title 
title=Label(window, text = "Mathematical table")
title.grid(row = 0, column = 0,columnspan = 3, pady=25)

caption=Label(window, text = "Number and Range:")
caption.grid(column = 0,row = 1,padx=10)


  
# Combobox creation  
theNum = IntVar() 
numbers=Combobox(window,textvariable = theNum,width=5)   
# Adding combobox drop down list 
numbers['values'] = tuple(range(101))
#place combobox
numbers.grid(column = 1, row = 1)


#radio buttons
endVal = IntVar()
r10=Radiobutton(window,text="10",variable=endVal,value=10)
r20=Radiobutton(window,text="20",variable=endVal,value=20)
r30=Radiobutton(window,text="30",variable=endVal,value=30)
#set the default value
endVal.set(10)

#place radiobuttons
r10.grid(column = 2, row = 1)
r20.grid(column = 2, row = 2,padx=30)
r30.grid(column = 2, row = 3,padx=30)


def generateMulTable():
    tables=""
    for i in range(endVal.get()+1):
        # 4 X 0 = 0 (Till the end value)
        tables += str(theNum.get())+"   X   "+str(i)+"   =   "+str(theNum.get()*i)+"\n" 
    table.configure(text=tables)

#create button and place it
generateButton=Button(window,text="Generate",command=generateMulTable)
generateButton.grid(row=4,column=1)

#create and place result table
table=Label(window,anchor="center")
table.grid(row=5,column=1, pady = 25)


window.mainloop() 