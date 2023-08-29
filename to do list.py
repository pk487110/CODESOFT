#importing the modules and packages

from tkinter import *
import ipywidgets as widgets
from tkinter import messagebox

#defining the functions to add the tasks
def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
#creating the window
    
root = Tk()
root.geometry('500x500+750+250')
root.title('To Do List')
root.config(bg='#FAEBD7')
root.resizable(0,0)

frame = Frame(root)
frame.pack(pady=10)



lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_list = [""]

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    root,
    font=('times', 24)
    )

my_entry.pack(pady=20)

#Creating the buttons

button_frame = Frame(root)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#0aa0c2',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#fc5826',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


root.mainloop()


