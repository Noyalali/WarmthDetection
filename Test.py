# from tkinter import *
# from tkinter.ttk import *
# root = Tk()
# root.title("First_Program")
# label = Label(root, text="Hello World !").pack()
# root.mainloop()

#######################################################3

# root = Tk()
# # Open window having dimension 100x100
# root.geometry('100x100')
# # Create a Button
# btn = Button(root, text = 'Click me !', bd = '5',
#                           command = root.destroy)
#
# # Set the position of button on the top of window.
# btn.pack(side = 'top')
# root.mainloop()


#######################################################

# root = Tk()
# root.geometry("300x200")
# w = Label(root, text ='SMEC', font = "50")
# w.pack()
#
# Checkbutton1 = IntVar()
# Checkbutton2 = IntVar()
# Checkbutton3 = IntVar()
#
# Button1 = Checkbutton(root, text = "Tutorial",
#                       variable = Checkbutton1,
#                       onvalue = 1,
#                       offvalue = 0,
#                       height = 2,
#                       width = 10)
#
# Button2 = Checkbutton(root, text = "Student",
#                       variable = Checkbutton2,
#                       onvalue = 1,
#                       offvalue = 0,
#                       height = 2,
#                       width = 10)
#
# Button3 = Checkbutton(root, text = "Courses",
#                       variable = Checkbutton3,
#                       onvalue = 1,
#                       offvalue = 0,
#                       height = 2,
#                       width = 10)
#
# Button1.pack()
# Button2.pack()
# Button3.pack()
# mainloop()

##########################################################

# import tkinter as tk
# from tkinter import ttk
#
# # Creating tkinter window
# window = tk.Tk()
# window.title('Combobox')
# window.geometry('500x250')
#
# # label text for title
# ttk.Label(window, text = "GFG Combobox Widget",
#           background = 'green', foreground ="white",
#           font = ("Times New Roman", 15)).grid(row = 0, column = 1)
#
# # label
# ttk.Label(window, text = "Select the Month :",
#           font = ("Times New Roman", 10)).grid(column = 0,
#           row = 5, padx = 10, pady = 25)
#
# # Combobox creation
# n = tk.StringVar()
# monthchoosen = ttk.Combobox(window, width = 27, textvariable = n)
#
# # Adding combobox drop down list
# monthchoosen['values'] = (' January',
#                           ' February',
#                           ' March',
#                           ' April',
#                           ' May',
#                           ' June',
#                           ' July',
#                           ' August',
#                           ' September',
#                           ' October',
#                           ' November',
#                           ' December')
#
# monthchoosen.grid(column = 1, row = 5)
# monthchoosen.current()
# window.mainloop()

####################################################


# import tkinter as tk
#
# root=tk.Tk()
#
# # setting the windows size
# root.geometry("600x400")
#
# # declaring string variable
# # for storing name and password
# name_var=tk.StringVar()
# passw_var=tk.StringVar()
#
# # defining a function that will
# # get the name and password and
# # print them on the screen
# def submit():
#
#     name=name_var.get()
#     password=passw_var.get()
#
#     print("The name is : " + name)
#     print("The password is : " + password)
#
#     name_var.set("")
#     passw_var.set("")
#
#
# # creating a label for
# # name using widget Label
# name_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
#
# # creating a entry for input
# # name using widget Entry
# name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
#
# # creating a label for password
# passw_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
#
# # creating a entry for password
# passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'), show = '*')
#
# # creating a button using the widget
# # Button that will call the submit function
# sub_btn=tk.Button(root,text = 'Submit', command = submit)
#
# # placing the label and entry in
# # the required position using grid
# # method
# name_label.grid(row=0,column=0)
# name_entry.grid(row=0,column=1)
# passw_label.grid(row=1,column=0)
# passw_entry.grid(row=1,column=1)
# sub_btn.grid(row=2,column=1)
#
# # performing an infinite loop
# # for the window to display
# root.mainloop()

####################################################

