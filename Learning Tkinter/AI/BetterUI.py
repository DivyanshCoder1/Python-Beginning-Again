from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Modern Glassy UI")
root.geometry("600x500")
root.configure(bg="#1e1e1e")

# Outer Frame for glass look
outer_frame = Frame(root, bg="#2C2C2C", bd=0, relief=FLAT)
outer_frame.place(relx=0.5, rely=0.5, anchor=CENTER, width=450, height=400)

# Title
title = Label(outer_frame, text="Sexy Tkinter UI", font=("Helvetica", 24, "bold"), bg="#2C2C2C", fg="#00FFFF")
title.pack(pady=20)

# Stylish Entry
style = ttk.Style()
style.theme_use('default')

style.configure("TEntry",
                foreground="white",
                fieldbackground="#3D3D3D",
                background="#3D3D3D",
                borderwidth=1,
                padding=10,
                relief="flat")

entry = ttk.Entry(outer_frame, width=30, font=("Helvetica", 12))
entry.pack(pady=10)

# Sexy Button
style.configure("TButton",
                foreground="#1e1e1e",
                background="#00FFFF",
                padding=10,
                font=("Helvetica", 12, "bold"),
                borderwidth=0)

btn = ttk.Button(outer_frame, text="Click Me 😘", style="TButton")
btn.pack(pady=20)

# Footer
footer = Label(outer_frame, text="Tkinter… but make it hot 🔥", bg="#2C2C2C", fg="grey", font=("Helvetica", 10))
footer.pack(side=BOTTOM, pady=10)

root.mainloop()
