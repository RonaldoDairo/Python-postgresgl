from tkinter import Tk, Canvas, Label, Frame, Entry, Button , W , E
import psycopg2

root = Tk()
root.title("Python & PostgresSQL")

def save_new_student(name, age, address):
    psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="password",
        host="localhost",
        port="5432"
    )


# Canvas
canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Add a Student')
label.grid(row=0, column=1)
# Name Input
label = Label(frame, text="Name")
label.grid(row=1, column=0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Age Input
label = Label(frame, text="Age")
label.grid(row=2, column=0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Address Input
label = Label(frame, text="Address")
label.grid(row=3, column=0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button = Button(frame, text="Add", command=lambda:save_new_student(
    entry_name.get(),
    entry_age.get(),
    entry_address.get()
    ))
button.grid(row=4, column=1, sticky= W+E)




root.mainloop()