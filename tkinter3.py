from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("800x500")
# changing the title
root.title("Student Dashboard")

# important label options
# text = adds the text
# bd = background
# fg = foreground
# font = sets the font
# padx = x padding
# pady = y padding
# relief = border styling = SUNKEN, RAISED , GROOVE, RIDGE
image = Image.open("images/divyaKhosla.jpg")
image = image.resize((400,300), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
imageLabel = Label(root, image= photo)
imageLabel.pack(side= RIGHT)

title_label = Label( text = ''' Divya Khosla Kumar (born 20 November 1987)[1] is an Indian film actress, producer and director.\n She has directed various advertisements and has also featured in some\n music videos. She is the wife of Bhushan Kumar, the chairman and managing \ndirector of T-Series music label and film production company.''', bg = "crimson",fg= "white",pady=20,padx= 40, font= ("comicsansns 14 bold"), borderwidth=3,relief = SUNKEN)

# pack attributes
# anchor = nw,se,sw,ne etc
# side = top, bottom, left, right
# fill = X,Y : fills acoordingly to the whole
# padx = padding to the outer body of the text Label
# pady = ""
# title_label.pack( side = BOTTOM, fill = X)

title_label.pack( side = LEFT, fill = Y)
root.mainloop()