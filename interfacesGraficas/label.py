from tkinter import *

root = Tk()

# texto = StringVar()
# texto.set("Un nuevo texto")
# root.title("Hola mundo")
# root.iconbitmap("favicon.ico")
# root.resizable(True, True)

# Label(root, text="Hola mundo").pack(anchor="nw")
# label = Label(root, text="Otra etiqueta")
# label.pack(anchor="center")
# Label(root, text="Hola mundo").pack(anchor="se")

# label.config(bg="green", fg="blue", font=("Verdana", 24))
# label.config(textvariable=texto)

imagen = PhotoImage(file="Animation.gif")

Label(root, image=imagen, bd=0).pack(side="left")
root.mainloop()
