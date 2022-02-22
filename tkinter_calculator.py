import tkinter as tk

root = tk.Tk()
root.iconbitmap('./my.ico')

# function for taking the value of the buttons

def button_values(number):
    initial = entryWindow.get()
    entryWindow.delete(0, tk.END)
    entryWindow.insert(0, str(initial) + str(number))


# Function for clear

def clearer():
    entryWindow.delete(0, tk.END)
    f_num = 0


# funtion for the displaying signs

def signs(signed):
    first_number = float(entryWindow.get())
    global f_num
    global sign
    sign = signed
    f_num = first_number
    entryWindow.delete(0,tk.END)

def result():
    next_number = int(entryWindow.get())
    entryWindow.delete(0,tk.END)

    final_result = 0
    if sign == "+":
        final_result=f_num+next_number
    elif sign == "-":
        final_result=f_num-next_number
    elif sign == "/":
        final_result=f_num/next_number
    elif sign == "*":
        final_result=f_num*next_number


    entryWindow.insert(0,final_result)


# root_title and the window size
root_title = root.title('Calculator')
# root.geometry('500x500+100+50')
# The entry window
entryWindow = tk.Entry(root, width=40, borderwidth=5)
entryWindow.grid(column=0, row=0, columnspan=4)


# The buttons of the numbers and signs
button_0 = tk.Button(root, text='0', padx=40, pady=20, command=lambda: button_values(0))
button_1 = tk.Button(root, text='1', padx=40, pady=20, command=lambda: button_values(1))
button_2 = tk.Button(root, text='2', padx=40, pady=20, command=lambda: button_values(2))
button_3 = tk.Button(root, text='3', padx=40, pady=20, command=lambda: button_values(3))
button_4 = tk.Button(root, text='4', padx=40, pady=20, command=lambda: button_values(4))
button_5 = tk.Button(root, text='5', padx=40, pady=20, command=lambda: button_values(5))
button_6 = tk.Button(root, text='6', padx=40, pady=20, command=lambda: button_values(6))
button_7 = tk.Button(root, text='7', padx=40, pady=20, command=lambda: button_values(7))
button_8 = tk.Button(root, text='8', padx=40, pady=20, command=lambda: button_values(8))
button_9 = tk.Button(root, text='9', padx=40, pady=20, command=lambda: button_values(9))
button_decimal = tk.Button(root, text='.', pady=20, padx=43,command=lambda: button_values('.'))

button_add = tk.Button(root, text='+', pady=20, padx=45, command = lambda:signs("+"))
button_subtract = tk.Button(root, text='-', pady=20, padx=45,command = lambda:signs("-"))
button_multiply = tk.Button(root, text='x', pady=20, padx=45,command = lambda:signs("*"))
button_divide = tk.Button(root, text='/', pady=20, padx=45, command = lambda:signs("/"))
button_result = tk.Button(root, text='=', pady=20, padx=150,command=result)
button_clear = tk.Button(root, text='clear', pady=20, padx=30, command=clearer)

# Placing the buttons


button_7.grid(column=2, row=1)
button_8.grid(column=1, row=1)
button_9.grid(column=0, row=1)
button_multiply.grid(column=3, row=1)

button_6.grid(column=2, row=2)
button_5.grid(column=1, row=2)
button_4.grid(column=0, row=2)
button_subtract.grid(column=3, row=2)

button_3.grid(column=2, row=3)
button_2.grid(column=1, row=3)
button_1.grid(column=0, row=3)
button_add.grid(column=3, row=3)

button_0.grid(column=0, row=4)
button_clear.grid(column=1, row=4)
button_decimal.grid(column=2, row=4)
button_divide.grid(column=3, row=4)

button_result.grid(column=0, row=5, columnspan=4)

root.mainloop()
