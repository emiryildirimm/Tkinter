import tkinter as tk

window = tk.Tk()
window.title("Python Tkinter")
window.minsize(width=450, height=300)


def click_button():
    # -> if you want to get user entry you can use it
    user_input = my_entry.get()
    print(user_input)


# label
my_label = tk.Label(text="This is a label", font=('Arial', 30, "italic"))
my_label.config(bg="black", fg="white")

# -> you can use the label for setting the label location(top middle) in the window
# my_label.pack(side="top")
# -> if you want to set specific location (without bottom left right top) you can use it
# my_label.place(x=0, y=0)
my_label.grid(row=0, column=0)

# button
# -> if you want to use command option you must define the function before command option
my_button = tk.Button(text="this is a button", command=click_button)
# my_button.pack(side="top")
# my_button.place(x=250-65, y=150-13)
# my_button.update()
# print(my_button.winfo_height())
# print(my_button.winfo_width())
my_button.grid(row=1, column=1)

# -> entry
my_entry = tk.Entry(width=40)
# my_entry.pack(side="top")
# my_entry.update()
# my_entry.place(x=110, y=100)
my_entry.grid(row=2, column=2)

window.mainloop()
