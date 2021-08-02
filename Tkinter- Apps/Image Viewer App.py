from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("images viewer")

myimg1 = ImageTk.PhotoImage(Image.open("Assets/DOOD.jpg"))
myimg2 = ImageTk.PhotoImage(Image.open("Assets/atlantis_1nebula_14-wallpaper-1920x1080.jpg"))
myimg3 = ImageTk.PhotoImage(Image.open("Assets/pp.webp"), width="1")
myimg4 = ImageTk.PhotoImage(Image.open("Assets/hi.png"))
myimg5 = ImageTk.PhotoImage(Image.open("Assets/DOOD.jpg"))
image_list = [myimg1, myimg2, myimg3, myimg4, myimg5]

status = Label(root, text="image 1 of" + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)

myLabel = Label(image=myimg1)
myLabel.grid(row=0, column=0, columnspan=3)


def popup():
    messagebox.showinfo("Error", "end of gallery")


def forward(number):
    global myLabel
    global button_forward
    global button_back

    myLabel.grid_forget()
    myLabel = Label(image=image_list[number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(number + 1))
    button_back = Button(root, text="<<", command=lambda: back(number - 1))

    if number == 5:
        button_forward = Button(root, text=">>", command=popup)

    myLabel.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status1 = Label(root, text="image" + str(number) + " of " + str(len(image_list)))
    status1.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(number):
    global myLabel
    global button_forward
    global button_back

    if number == 1:
        button_back = Button(root, text="<<", state=DISABLED)

    myLabel.grid_forget()
    myLabel = Label(image=image_list[number - 1])

    button_back = Button(root, text="<<", command=lambda: (number - 1))

    myLabel.grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command=lambda: forward(number + 1))
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=0)

    status2 = Label(root, text="image" + str(number) + " of " + str(len(image_list)))
    status2.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(root, text="<<", command=back, state=DISABLED)
button_forward = Button(root, text=">>", command=lambda: forward(2))
button_exit = Button(root, text="EXIT", command=root.quit)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
status.grid(row=2, column=0, columnspan=3, sticky=W + E)

root.mainloop()
