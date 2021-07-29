from tkinter import *


root = Tk()
root.title("simple calculator")

entrytextbox = Entry(root, width=35, borderwidth=5)
entrytextbox.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


# define function
def button_clear():
    entrytextbox.delete(0, END)


def button_click(number):

    current = entrytextbox.get()
    entrytextbox.delete(0, END)
    entrytextbox.insert(0, str(current) + str(number))


def button_add():

  first_num = entrytextbox.get()

  global f_num
  global math

  math = "addition"
  f_num = int(first_num)
  entrytextbox.delete(0, END)


def button_subtract():
    first_num = entrytextbox.get()

    global f_num
    global math

    math = "subtraction"
    f_num = int(first_num)
    entrytextbox.delete(0, END)


def button_multiply():
    first_num = entrytextbox.get()

    global f_num
    global math

    math = "multiplication"
    f_num = int(first_num)
    entrytextbox.delete(0, END)


def button_divide():
    first_num = entrytextbox.get()

    global f_num
    global math

    math = "division"
    f_num = int(first_num)
    entrytextbox.delete(0, END)


def button_equal():

    second_number = entrytextbox.get()
    entrytextbox.delete(0, END)

    if math == "addition":
        entrytextbox.insert(0, int(f_num) + int(second_number))

    elif math == "subtraction":
        entrytextbox.insert(0, int(f_num) - int(second_number))

    elif math == "division":

        entrytextbox.insert(0, int(f_num) / int(second_number))

    elif math == "multiplication":
        entrytextbox.insert(0, int(f_num) * int(second_number))

# define buttons


button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), fg="white", bg="black")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), fg="white", bg="black")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), fg="white", bg="black")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), fg="white", bg="black")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), fg="white", bg="black")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), fg="white", bg="black")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), fg="white", bg="black")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), fg="white", bg="black")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), fg="white", bg="black")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), fg="white", bg="black")
button_add1 = Button(root, text="+", padx=40, pady=20, command=button_add, fg="white", bg="black")
button_eq = Button(root, text="=", padx=91, pady=20, command=button_equal, fg="white", bg="black")
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear, fg="white", bg="black")
button_sub = Button(root, text="-", padx=40, pady=20, command=button_subtract, fg="white", bg="black")
button_mul = Button(root, text="*", padx=40, pady=20, command=button_multiply, fg="white", bg="black")
button_div = Button(root, text="/", padx=40, pady=20, command=button_divide, fg="white", bg="black")

# put buttons on screen

button_1.grid(row= 3, column=0)
button_2.grid(row= 3, column=1)
button_3.grid(row= 3, column=2)
button_4.grid(row= 2, column=0)
button_5.grid(row= 2, column=1)
button_6.grid(row=2 , column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1 , column=1)
button_9.grid(row= 1, column=2)
button_0.grid(row= 4, column=0)

button_add1.grid(row=5, column=0)
button_eq.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_mul.grid(row=6, column=0)
button_div.grid(row=6, column=1)
button_sub.grid(row=6, column=2)


root.mainloop()


