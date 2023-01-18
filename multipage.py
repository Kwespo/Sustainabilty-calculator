import tkinter as tk

root = tk.Tk()
root.geometry("600x600")

#pages

Page1 = tk.Frame(root, background="Black")
page2 = tk.Frame(root, background="White")

def p1():
    Page1.place(x=150, y=0, width=350, height=400)
    page2.place_forget()

def p2():
    page2.place(x=150, y=0, width=350, height=400)
    Page1.place_forget()

p1but= tk.Button(root, text="Page 1", command=p1)
p1but.place(x=10, y=0)

p2but= tk.Button(root, text="Page 2", command=p2)
p2but.place(x=10, y=30)

#add to pages

p1txt = tk.Label(Page1, text="Hello", bg="black", fg="white")
p1txt.place(x=50,y=10)

p2txt = tk.Label(page2, text="Goodbye")
p2txt.place(x=50,y=10)
root.mainloop()                           