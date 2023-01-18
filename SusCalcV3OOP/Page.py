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

root = tk.Tk()
root.geometry("1000x1000")
root.title("Sustainability calculator Version TWO (DIFF PAGE)")
root.resizable(False,False)
root.configure(bg="gray")

Home= tk.Frame(root, background="Red")
dtapage= tk.Frame(root, background="gray")

#what does the command p1 do
def p1():
    Home.place(x=0, y=0, width=1000, height=1000)
    dtapage.place_forget()
    page2button.place(x=250, y=450, width= 500, height=50)

#what does the command p2 do
def p2():
    dtapage.place(x=0, y=0, width=1000, height=1000)
    Home.place_forget()
    page2button.place_forget()


#p1but.place(x=10, y=0)
#p1but= tk.Button(root, text="Page 1", command=p1)

page2button= tk.Button(root, text="Page 2", command=p2)

#load onto Page 1 instantly
p1()



wellabl = tk.Label(Home, text="Welcome! Press the button below to enter the calculator", font=("times", "22"))
wellabl.place(x=0, y=320, width=1000)


#PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2


appliances = ["Computer", "Phone", "Lamp", "Other" ]


#dropdown menu
choiceapp = tk.StringVar(dtapage)
choiceapp.set("Press an appliance, please.") #starting value
dropdownapliance = tk.OptionMenu(dtapage, choiceapp, *appliances)
dropdownapliance.place(x = 10, y = 20)

#add whatever you input into the entry box as a saved option
appliances.append("apple") 
print(appliances)

#input your own KWh (kilawatt per hour)
kwh_input_v1 = tk.Entry(dtapage)
kwh_input_v1.place(x=65, y=80)

#input hours
hour_input_v1 = tk.Entry(dtapage)
hour_input_v1.place(x=65, y=110)

hourslbl = tk.Label(dtapage, text="Hours")
hourslbl.place(x= 5, y=110, width= 60)

kwhlbl =tk.Label(dtapage, text = "Kwh")
kwhlbl.place(x=5, y=80, width= 60)

items = {
    
    "Computer": 0.8,
    "Phone": 0.4,
    "Lamp": 0.1,
    "Other": kwh_input_v1.get
}


def check():
    if choiceapp.get() == None:
        print ("Please select")

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
    
    #outputpower.config (text=str(tp)+" kw of power has been used in the year. "+ 
        #"£" + str(round((tc), 2))+" Has been spent this year using that appliance "
        # + "You've also used " + str(round((tcb), 2))+ " grams of carbon.")
    totalKWH.config (text="You've used " + str(round((tp), 2))+ " Kw of Power")
    totalcarb.config (text="You've produced " + str(round((tcb), 2))+ " Grams of Carbon") #MAKE SURE YOU KEEP THE SPACE ON LINE WITH 108 AND 107 AS THAT MAKES IT LOOK READABLE!
    totalmoney.config (text="You've spent " + "£" + str(round((tc), 2)))


calculat = tk.Button(dtapage, text="submit", command=press)
calculat.place(x=5, y=150)

#output choice
totalKWH = tk.Label(dtapage, text="Your total KWH will show here:")
totalKWH.place(x=5, y=200)
totalcarb = tk.Label(dtapage ,text="Your total Carbon will show here:")
totalcarb.place(x=5, y=240)
totalmoney = tk.Label(dtapage ,text="Your total money will show here:")
totalmoney.place(x=5, y=280)

root.mainloop()