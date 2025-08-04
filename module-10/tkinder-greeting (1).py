
import tkinter as tk
from tkinter import messagebox, simpledialog

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

app = tk.Tk()
app.title("To-Do List")
app.geometry("400x300")

frame = tk.Frame(app)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=(0, 10))

add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

task_listbox = tk.Listbox(app, width=50)
task_listbox.pack(pady=10)

remove_button = tk.Button(app, text="Remove Selected Task", command=remove_task)
remove_button.pack()

app.mainloop()
