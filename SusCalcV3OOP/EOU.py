import tkinter as Tk

class TkInputLable:
    def __init__(self):
        pass

    def make(self, location, text):
        self.location = location
        self.text = text

        Tk_Label(self.location, text = f"{self.text}")
        Tk_Entry(self.location)

    def place(self, location_X, location_Y):
        self.location = location_X
        self.location_Y = location_Y

        Tk.Label.place(x = self.location_X, y = self.location_Y)
        Tk.Entry.place(x = self.location_X, y = self.location_Y)




root = Tk.Tk()

test = TkInputLable()
test.make(root, test)
test.place(5, 5)


root.mainloop()