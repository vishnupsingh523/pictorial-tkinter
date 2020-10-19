# setting the link to the label frame using webbrowser library

from tkinter import *
import webbrowser
root = Tk()
root.geometry("800x400")

frame = Frame(root, bg="black", borderwidth=4)
frame.pack(side = TOP, fill=X)

l1 = Label(frame, text="Vishwanath Github Account",fg = "black", bg = "white",cursor = "hand2")
l1.pack( pady=10)
l1.bind("<Button-1>", lambda e: webbrowser.open_new("http://www.github.com/vishnupsingh523"))
root.mainloop()