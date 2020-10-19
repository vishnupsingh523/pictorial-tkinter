# Using the CHECK BOX in GUI
from tkinter import *
main_root = Tk()

main_root.geometry("500x400")
main_root.maxsize(500,400)

frame1 = Frame(borderwidth=2,bg="grey")
frame1.pack()

terms = Label(frame1, text = "You have to give your property to Mr. Vishwanath Pratap Singh. And not only this but you also have to make it clear that there is no place within the 25 Km range of area.\nIf you agree this condition so definately he will purchase this house with whatever amount you want.\nRegards Tera Baap", wraplength = 300, padx= 10,pady = 20)
terms.pack(fill = X)
check = Checkbutton(frame1, text = "I accept your Terms & Conditions.",fg = "green")
check.pack(fill=X)

main_root.mainloop()