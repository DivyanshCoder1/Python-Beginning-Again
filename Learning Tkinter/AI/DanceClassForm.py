from tkinter import *

root = Tk()
root.title("Dance Class Form")
root.geometry("500x450")
root.configure(bg="#2E2E2E")  # Set background color

# Variables
user_name = StringVar()
user_age = IntVar()
user_address = StringVar()
slot = StringVar()
slot.set("Slot1")  # default value

# Title Frame
f1 = Frame(bg="#2E2E2E", height=50)
f1.pack(side=TOP, fill=X, padx=20, pady=20)

l1 = Label(f1, text="Please enter the following details", bg="#2E2E2E", fg="white", font="Helvetica 18 bold")
l1.place(relx=0.5, rely=0.5, anchor=CENTER)

# Form Frame
f2 = Frame(bg="#2E2E2E", padx=10, pady=10)
f2.pack()

# Labels
Label(f2, text="Name:", font="Helvetica 14 bold", fg="white", bg="#2E2E2E").grid(row=1, column=0, sticky="w", pady=5)
Label(f2, text="Age:", font="Helvetica 14 bold", fg="white", bg="#2E2E2E").grid(row=2, column=0, sticky="w", pady=5)
Label(f2, text="Address:", font="Helvetica 14 bold", fg="white", bg="#2E2E2E").grid(row=3, column=0, sticky="w", pady=5)
Label(f2, text="Slot for classes:", font="Helvetica 14 bold", fg="white", bg="#2E2E2E").grid(row=4, column=0, sticky="w", pady=5)

# Entries
Entry(f2, textvariable=user_name, font="Helvetica 12").grid(row=1, column=1, pady=5)
Entry(f2, textvariable=user_age, font="Helvetica 12").grid(row=2, column=1, pady=5)
Entry(f2, textvariable=user_address, font="Helvetica 12").grid(row=3, column=1, pady=5)

# Slot Selection
f3 = Frame(f2, bg="#2E2E2E")
f3.grid(row=4, column=1)

Radiobutton(f3, text="Slot1", variable=slot, value="Slot1", font="Helvetica 12", fg="white", bg="#2E2E2E", selectcolor="#4ECDC4", activebackground="#2E2E2E").grid(row=0, column=0, padx=10)
Radiobutton(f3, text="Slot2", variable=slot, value="Slot2", font="Helvetica 12", fg="white", bg="#2E2E2E", selectcolor="#4ECDC4", activebackground="#2E2E2E").grid(row=0, column=1, padx=10)

# Submit Action
def submit():
    print("---- Form Data ----")
    print("Name:", user_name.get())
    print("Age:", user_age.get())
    print("Address:", user_address.get())
    print("Slot:", slot.get())

# Submit Button - centered using columnspan
submit_btn = Button(f2, text="Submit", command=submit, bg="#FF6B6B", fg="white", font="Helvetica 12 bold", padx=10, pady=5)
submit_btn.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()
