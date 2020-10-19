# Making the login form sample here
from tkinter import *

root = Tk()
root.geometry("600x500")
root.title("Student Login")
# using frame where all the other elements will lie
mainFrame = Frame(bd = 2, bg = "grey")
mainFrame.pack(pady= 100)

loginTop = Label(mainFrame, text = "LogIn",bg="navy",fg="white", font = "Arial 20 bold", padx = 30)
loginTop.pack(fill = X)

# declearing the other frames
detailsFrame = Frame(mainFrame, bg = "white",padx=20,pady=10)
detailsFrame.pack(fill=X)

username = Label(detailsFrame, text="Username",font = "Arial 12 ",bg="white", fg="black").grid(row=0,column=0)
usernameInput = Entry(detailsFrame,bg = "lightgrey").grid(row = 0, column = 1)

password = Label(detailsFrame, text="Password",font = "Arial 12 ", bg="white", fg="black").grid(row=1,column=0)
passwordInput = Entry(detailsFrame,bg = "lightgrey", show = "*").grid(row = 1, column = 1)

# creating submit frame here
submitFrame = Frame(mainFrame, bg= "white")
submitFrame.pack(fill = X)
submit = Button(submitFrame, text = "Submit",font = "Arial 10 ", bg = "lightgrey", fg = "black")
submit.pack(pady = 10)
root.mainloop()