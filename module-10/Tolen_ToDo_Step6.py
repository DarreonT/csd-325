
from tkinter import *
from tkinter import messagebox

# Function to add tasks
def add_task(event=None):
    task = entry.get()
    if task:
        listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete selected task with right-click
def delete_task(event):
    try:
        index = listbox.nearest(event.y)
        if messagebox.askyesno("Delete Task", "Delete selected task?"):
            listbox.delete(index)
    except:
        pass

# Function to exit the app
def exit_app():
    root.destroy()

# Create main window
root = Tk()
root.title("Tolen-ToDo")
root.geometry("400x300")

# Menu setup with complementary colors
menu = Menu(root, bg='lightblue', fg='darkblue')
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0, bg='lightblue', fg='darkblue')
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=exit_app)

# Label with instructions
label = Label(root, text="Enter a task. Right-click a task to delete it.", font=('Arial', 10))
label.pack(pady=5)

# Entry box
entry = Entry(root, width=40)
entry.pack(pady=5)
entry.bind("<Return>", add_task)

# Add task button
add_button = Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

# Scrollbar and Listbox
frame = Frame(root)
frame.pack(pady=5)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(frame, width=50, yscrollcommand=scrollbar.set)
listbox.pack()

scrollbar.config(command=listbox.yview)

# Right-click delete binding
listbox.bind("<Button-3>", delete_task)

root.mainloop()
