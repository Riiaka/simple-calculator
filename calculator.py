from tkinter import*

root=Tk()
root.title("simple calculator")
root.configure(background = "powderblue")

e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def Button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))

def Button_clear():
    e.delete(0,END)

def Button_add():
    first_number = e.get()
    global f_num
    global math
    math="addition"
    f_num = int(first_number)
    e.delete(0, END)

def Button_equal():
    second_number = e.get()
    e.delete(0,END)

    if math == "addition":
       e.insert(0, f_num + int(second_number))

    if math == "subtraction":
       e.insert(0, f_num - int(second_number))

    if math == "multiplication":
       e.insert(0, f_num *int(second_number))

    if math == "division":
       e.insert(0, f_num /int(second_number))


def Button_subtract():
    first_number = e.get()
    global f_num
    global math
    math="subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def Button_multiply():
    first_number = e.get()
    global f_num
    global math
    math="multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def Button_divide():
    first_number = e.get()
    global f_num
    global math
    math="division"
    f_num = int(first_number)
    e.delete(0, END)




#define buttons

Button_1 = Button(root, text="1",  padx=40, pady=20, command = lambda: Button_click(1))
Button_2 = Button(root, text="2",  padx=40, pady=20, command = lambda: Button_click(2))
Button_3 = Button(root, text="3",  padx=40, pady=20, command = lambda: Button_click(3))
Button_4 = Button(root, text="4",  padx=40, pady=20, command = lambda: Button_click(4))
Button_5 = Button(root, text="5",  padx=40, pady=20, command = lambda: Button_click(5))
Button_6 = Button(root, text="6",  padx=40, pady=20, command = lambda: Button_click(6))
Button_7 = Button(root, text="7",  padx=40, pady=20, command = lambda: Button_click(7))
Button_8 = Button(root, text="8",  padx=40, pady=20, command = lambda: Button_click(8))
Button_9 = Button(root, text="9",  padx=40, pady=20, command = lambda: Button_click(9))
Button_0 = Button(root, text="0",  padx=40, pady=20, command = lambda: Button_click(0))
Button_add = Button(root, text="+", padx=39,pady=20, command =  Button_add)
Button_equal = Button(root, text="=", padx=95, pady=20, command =  Button_equal)
Button_clear = Button(root, text="clear", padx=86, pady=20, command = Button_clear)
Button_subtract = Button(root, text="-", padx=40,pady=20, command =  Button_subtract)
Button_multiply = Button(root, text="*", padx=41,pady=20, command =  Button_multiply)
Button_divide = Button(root, text="/", padx=41,pady=20, command =  Button_divide)


#display the button on the screen

Button_1.grid(row="3",column="0")
Button_2.grid(row="3",column="1")
Button_3.grid(row="3",column="2")

Button_4.grid(row="2",column="0")
Button_5.grid(row="2",column="1")
Button_6.grid(row="2",column="2")

Button_7.grid(row="1",column="0")
Button_8.grid(row="1",column="1")
Button_9.grid(row="1",column="2")

Button_0.grid(row="4",column="0")
Button_clear.grid(row="4",column="1",columnspan=2)
Button_add.grid(row="5",column="0")
Button_equal.grid(row="5",column="1",columnspan=2)

Button_subtract.grid(row="6",column="0")
Button_multiply.grid(row="6",column="1")
Button_divide.grid(row="6",column="2")

root.mainloop()
