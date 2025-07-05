from tkinter import *

root = Tk()
root.title("Dance Class Form")
root.geometry("500x400")

#Defining frame 1
f1 = Frame(bg = "grey", height="40px")
f1.pack(side=TOP, fill=X, padx = 20, pady=20)

l1 = Label(f1, text="Please enter the following details", bg="grey", fg="White", font="sansserif 20 bold")
# l1.grid(row=0, column=2)
l1.place(relx=0.5, rely=0.5, anchor=CENTER)

#Defining frame 2
f2 = Frame(bg="grey", padx = 10, pady=10)
f2.pack()

name_label = Label(f2, text="Name: ", font="comicsansms 15 bold", fg="white", bg="grey")
age_label = Label(f2, text="Age: ", font="comicsansms 15 bold", fg="white", bg="grey")
address_label = Label(f2, text="Address: ", font="comicsansms 15 bold", fg="white", bg="grey")
slot_label = Label(f2, text="Slot for classes: ", font="comicsansms 15 bold", fg="white", bg="grey")

name_label.grid(row=1, column=0, sticky="w")
age_label.grid(row=2, column=0, sticky="w")
address_label.grid(row=3, column=0, sticky="w")
slot_label.grid(row=4, column=0, sticky="w")


# name_label1.place(relx = 0, rely = 0)
# age_label.place(rely = 0.25, relx = 0)
# address_label.place(rely = 0.5, relx = 0)
# slot_label.place(rely = 0.75, relx = 0)

user_name = StringVar()
user_age = IntVar()
user_address = StringVar()

e1 = Entry(f2, textvariable=user_name)
e2 = Entry(f2, textvariable=user_age)
e3 = Entry(f2, textvariable=user_address)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)

f3 = Frame(f2, bg="grey")
f3.grid(row=4, column = 1)

slot1btn = Button(f3, text="Slot1", font="comicsansms 10 bold", fg="white", bg="grey", border=2, relief=SUNKEN)
slot2btn = Button(f3, text="Slot2", font="comicsansms 10 bold", fg="white", bg="grey", border = 2, relief = SUNKEN)

slot1btn.grid(row=0, column=0, padx=20)
slot2btn.grid(row=0, column=1)

f4 = Frame(f2)
f4.grid(row=5)

submit_btn = Button(f2, text="Submit", border=0)
submit_btn.grid(row=5)

root.mainloop()