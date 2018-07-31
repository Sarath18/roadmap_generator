#!/usr/bin/python3
from tkinter import *
from grid import *

class worldSettings(object):
    def __init__(self):
        self.ambient = "120 120 120 255"
        self.time = "10:00"
        self.rows = 10
        self.rows = 10

    def worldScene(self):
        #self.time = input("Enter time of day[24 hrs](hh:mm): ")
        if self.time == "":
            self.time = "10:00"
        time = self.time[0:2]
        time = int(time)

        #Night / Early Morning
        if time<6 or time>=21:
            self.ambient = "20 40 50 255"
        #Dawn
        elif time<7 and time>=6:
            self.ambient = "120 80 60 255"
        #After Dawn
        elif time<8 and time>=7:
            self.ambient = "120 70 80 255"
        #Before Dusk
        elif time<20 and time>19:
            self.ambient = "120 70 80 255"
        #Dusk
        elif time<21 and time>=20:
            self.ambient = "120 80 60 255"

    def getEntry(self):
        self.rows = int(row_entry.get())
        self.cols = int(col_entry.get())
        self.time = time_entry.get()
        self.worldScene()
        root.destroy()


if __name__ == "__main__":
    #m = int(input("Enter number of rows: "))
    #n = int(input("Enter number of cols: "))
    rows = 0
    cols = 0
    root = Tk()
    root.title('Road Generator')


    #FRAME 1
    row_frame = Frame(master=root,width=200,height=5)

    rowLabelText=StringVar()
    rowLabelText.set("\t           Number of Rows: ")
    row_label=Label(row_frame, textvariable=rowLabelText)
    row_label.pack(side=LEFT,padx=10,pady=5)

    row_entry = Entry(row_frame)
    row_entry.pack(side=LEFT,padx=10,pady=5)
    row_entry.focus_set()

    row_frame.pack()

    #FRAME 2
    col_frame = Frame(master=root,width=100,height=50)

    colLabelText=StringVar()
    colLabelText.set("\t            Number of Cols: ")
    col_label=Label(col_frame, textvariable=colLabelText)
    col_label.pack(side=LEFT,padx=10,pady=5)

    col_entry = Entry(col_frame)
    col_entry.pack(side=LEFT,padx=10,pady=5)

    col_frame.pack()

    time_frame = Frame(master=root,width=100,height=50)

    timeLabelText=StringVar()
    timeLabelText.set("Enter time of day[24 hrs](hh:mm):")
    time_label=Label(time_frame, textvariable=timeLabelText)
    time_label.pack(side=LEFT,padx=10,pady=5)

    time_entry = Entry(time_frame)
    time_entry.pack(side=LEFT,padx=10,pady=5)

    time_frame.pack()

    w = worldSettings()

    #Submit Buttom
    b = Button(root,text='Submit',command=w.getEntry).pack(pady=5)
    root.mainloop()

    print(w.rows,w.cols,w.time,w.ambient)

    OpenGrid(w)
