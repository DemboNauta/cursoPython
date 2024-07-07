from tkinter import *

root = Tk()
root.title("Hola mundo")
root.iconbitmap("favicon.ico")
root.resizable(True, True)

frame = Frame(root, width=480, height=320)
frame.pack(fill='both', expand=1)
frame.config(cursor="pirate")
frame.config(bg="lightblue")
frame.config(bd=25)
frame.config(relief="sunken")


root.config(cursor="arrow")
root.config(bg="blue")
root.config(bd=5)
root.config(relief="solid")

root.mainloop()
