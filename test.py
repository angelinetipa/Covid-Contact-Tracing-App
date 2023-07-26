from tkinter import *

window = Tk()
window.title("Editable Entry")
window.geometry("300x100")

# Function to handle focus in event (removes default text)
def on_entry_click(event):
    if entry.get() == "Name":
        entry.delete(0, END)
        entry.config(fg='black')

# Function to handle focus out event (restores default text if entry is empty)
def on_focus_out(event):
    if not entry.get():
        entry.insert(0, "Name")
        entry.config(fg='gray')

# Create an entry widget
entry = Entry(window, width=20, bd=3, fg='gray')
entry.place(x=80, y=30)

# Insert the default text "Name" into the entry
entry.insert(0, "Name")
entry.config(fg='gray')

# Bind click and focus out events to the functions
entry.bind('<FocusIn>', on_entry_click)
entry.bind('<FocusOut>', on_focus_out)

window.mainloop()