#Create options
import ctypes
from secrets import choice
from this import d
import tkinter as tk
from wsgiref.util import application_uri
ctypes.windll.shcore.SetProcessDpiAwareness(1)


COST = 0.51
D_I_Y = 365
CARBON = 0.2333

#home page
root = tk.Tk()
root.geometry("1000x600")
root.title("Sussy")
root.resizable(True,True)
root.configure(bg="light blue")

appliances = ["Computer", "Phone", "Lamp", "Other" ]


#dropdown menu
choiceapp = tk.StringVar(root)
choiceapp.set("Press an appliance, please.") #starting value
dropdownapliance = tk.OptionMenu(root, choiceapp, *appliances)
dropdownapliance.place(x = 10, y = 20)

#add whatever you input into the entry box as a saved option
#appliances.append("apple")  WORK ON THIS

#input your own KWh (kilawatt per hour)
kwh_input_v1 = tk.Entry(root)
kwh_input_v1.place(x=60, y=80)

#input hours
hour_input_v1 = tk.Entry(root)
hour_input_v1.place(x=60, y=110)

hourslbl = tk.Label(root, text="Hours")
hourslbl.place(x= 10, y=110)

kwhlbl =tk.Label(root, text = "Kwh")
kwhlbl.place(x=10, y=80)

items = {
    
    "Computer": 0.8,
    "Phone": 0.4,
    "Lamp": 0.1,
    "Other": kwh_input_v1.get
}




def press():
    #kwh_input_float = float(kwh_input_v1.get())
    #print(kwh_input_float)
    if choiceapp.get() == "Other":
        th = float(hour_input_v1.get())* D_I_Y
        tp = float(kwh_input_v1.get()) * th
        tc = tp * COST 
        tcb = tp * CARBON
    else:
        th = float(hour_input_v1.get())* D_I_Y
        tp = float(items[choiceapp.get()])* th
        tc = tp * COST
        tcb = tp * CARBON
    
    outputpower.config (text=str(tp)+" kw of power has been used in the year. "+ 
        "£" + str(round((tc), 2))+" Has been spent this year using that appliance "
         + "You've also used " + str(round((tcb), 2))+ " grams of carbon.")

myButton = tk.Button(root, text="submit", command=press)
myButton.place(x=10, y=300)

#output choice
outputpower = tk.Label(root,text="RESULTS WILL APPEAR HERE")
outputpower.place(x=10, y=500)

root.mainloop()