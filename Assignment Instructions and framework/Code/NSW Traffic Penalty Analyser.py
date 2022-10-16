import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk
import sqlite3
import pandas as pd

# Background Colour
bg_colour = "#F0F0F0"

# Width and Height of Program
w = 1000
h = 800


def browse_files():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("Text files",
                                                      "*.txt*"),
                                                     ("Database files",
                                                      "*.db*"),
                                                     ("All files",
                                                      "*.*")))
    label_file_explorer.configure(text="File Successfully Uploaded: " + filename)


def our_command():
    pass


# def back():


def fetch_db():
    # Database Connection
    connection = sqlite3.connect(filename)
    cursor = connection.cursor()
    cursor.execute("SELECT * "
                   "FROM Offences  "
                   "LIMIT 0,30;")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


def load_db():
    print("Placeholder")


def load_frame2():
    fetch_db()


# initialize app
root = tk.Tk()
root.title("DataAnalysisTool.exe")
# root.eval("tk::PlaceWindow . center")

# Screen width & height
ws = root.winfo_screenwidth()  # width of the screen
hs = root.winfo_screenheight()  # height of the screen

# Calculation for the x and y coords for the Tk root window
x = (ws / 2) - (w / 2)
y = (hs / 2) - (h / 2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

# frames
frame1 = tk.Frame(root, width=w, height=h, bg=bg_colour)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# frame 1 widgets

logo_img = ImageTk.PhotoImage(file="logo.jpg")
logo_widget = tk.Label(frame1, image=logo_img)
logo_widget.image = logo_img
logo_widget.pack()

# Text
label_file_explorer = tk.Label(
    frame1,
    text="Start analysing your data.",
    bg=bg_colour, fg="black",
    font=("TkMenuFont", 14)
)

label_file_explorer.pack(pady=20)

# button widget
tk.Button(
    frame1,
    text="Upload Dataset",
    font=("TkHeadingFont", 20),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=browse_files
).pack(pady=30)

# Back Button

tk.Button(
    frame1,
    text="Back",
    font=("TkHeadingFont", 20),
    # command=back
)

# Navigation Bar

my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Settings Menu
settings_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Options", command=our_command)

# Tools Menu
tools_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Tools", menu=tools_menu)
tools_menu.add_command(label="Graphs", command=our_command)
tools_menu.add_command(label="Algorithms", command=our_command)

# View Menu
view_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom In", command=our_command)
view_menu.add_command(label="Zoom Out", command=our_command)

# Help Menu
help_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Help?", command=our_command)
help_menu.add_command(label="Contact Support", command=our_command)
help_menu.add_separator()
help_menu.add_command(label="Getting Started", command=our_command)

# run app

root.mainloop()
