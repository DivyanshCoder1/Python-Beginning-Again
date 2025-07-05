from tkinter import *


def hello():
    print("Hello, The button is pressed now")

root = Tk()
root.geometry("500x400")
root.title("This is the title")
main_label = Label(text = "Ready", fg="White", bg="Blue", border="3", relief=SUNKEN, font="sansserif 20 bold")

main_label.pack(side=BOTTOM, anchor="s", fill=X)

f1 = Frame()
f1.pack()


b1 = Button(f1, text="This is button 1", border=3, command=hello)
b1.pack()

root.mainloop()