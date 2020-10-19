from tkinter import *
from PIL import Image, ImageTk
main_root = Tk()

# width and height setting
main_root.geometry("1000x400")

# # width, height minsize() setting the minimum size
# main_root.minsize(500,200)
#
# # setting the maximum size of the gui box
# main_root.minsize(1200,600)

# label = Label(text = "Vishwanath Pratap Singh is a very good programmmer.")
# # packing the label this is the rule of python gui
# label.pack()

# importing the image to our gui
image = Image.open("vishnu.jpg")
# resizing the image: height and width
image = image.resize((350,400), Image.ANTIALIAS)

photo = ImageTk.PhotoImage(image)
image_label = Label(main_root,image=photo)
image_label.pack()

main_root.mainloop()