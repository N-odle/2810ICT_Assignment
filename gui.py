import tkinter as tk
from PIL import ImageTk
import sqlite3

bg_colour = "#F0F0F0"


def our_command():
    pass


def fetch_db():
    connection = sqlite3.connect("OffenceDB.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sqlite_schema WHERE type='table';")
    all_tables = cursor.fetchall()
    print(all_tables[0])
    connection.close()


def load_frame2():
    fetch_db()


# initialize app
root = tk.Tk()
root.title("DataAnalysisTool.exe")
root.eval("tk::PlaceWindow . center")

# frames
frame1 = tk.Frame(root, width=1200, height=800, bg=bg_colour)
frame1.grid(row=0, column=0)
frame1.pack_propagate(False)

# frame 1 widgets

logo_img = ImageTk.PhotoImage(file="logo.jpg")
logo_widget = tk.Label(frame1, image=logo_img)
logo_widget.image = logo_img
logo_widget.pack()

# tk.Label(frame1, text="Start analysing your data.", bg=bg_colour, fg="white", font=("TkMenuFont", 14)).pack()

# button widget
tk.Button(
    frame1,
    text="Analyse Dataset",
    font=("TkHeadingFont", 20),
    bg="#28393a",
    fg="white",
    cursor="hand2",
    activebackground="#badee2",
    activeforeground="black",
    command=lambda: load_frame2()).pack(pady=50)

# Navigation Bar

my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Menu Items

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
my_menu.add_cascade(label="View", menu=help_menu)
help_menu.add_command(label="Help?", command=our_command)
help_menu.add_command(label="Contact Support", command=our_command)
help_menu.add_separator()
help_menu.add_command(label="Getting Started", command=our_command)


# run app

root.mainloop()
