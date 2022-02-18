import tkinter as tk

root = tk.Tk()
# root_title and the window size
root_title = root.title('Calculator')
# root.geometry('500x500+100+50')
# The entry window
entryWindow = tk.Entry(root, width=50, borderwidth=5)
entryWindow.grid(column=0, row=0, columnspan=4)
# The buttons of the numbers and signs
button_0 = tk.Button(root, text='0', padx=30, pady=20)
button_1 = tk.Button(root, text='1', padx=30, pady=20)
button_2 = tk.Button(root, text='2', padx=30, pady=20)
button_3 = tk.Button(root, text='3', padx=30, pady=20)
button_4 = tk.Button(root, text='4', padx=30, pady=20)
button_5 = tk.Button(root, text='5', padx=30, pady=20)
button_6 = tk.Button(root, text='6', padx=30, pady=20)
button_7 = tk.Button(root, text='7', padx=30, pady=20)
button_8 = tk.Button(root, text='8', padx=30, pady=20)
button_9 = tk.Button(root, text='9', padx=30, pady=20)
button_add = tk.Button(root, text='+', pady=20, padx=10)
button_decimal = tk.Button(root, text=',', pady=20, padx=10)
button_subtract = tk.Button(root, text='-', pady=20, padx=10)
button_multiply = tk.Button(root, text='x', pady=20, padx=10)
button_divide = tk.Button(root, text='/', pady=20, padx=10)
button_result = tk.Button(root, text='=', pady=20, padx=10)
button_clear = tk.Button(root, text='clear', pady=20, padx=10)
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
button_result.grid(column=3, row=4)
root.mainloop()
