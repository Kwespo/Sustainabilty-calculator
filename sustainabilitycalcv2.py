#Create options
import ctypes
from secrets import choice
from this import d
import tkinter as Tk
from wsgiref.util import application_uri
ctypes.windll.shcore.SetProcessDpiAwareness(1)


COST = 0.51
D_I_Y = 365
CARBON = 0.2333

root = Tk.Tk()
root.geometry("1000x1000")
root.title("Sustainability calculator Version TWO (DIFF PAGE)")
root.resizable(False,False)
root.configure(bg="gray")

Home= Tk.Frame(root, background="Midnight Blue")
dtapage= Tk.Frame(root, background="gray")

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
#p1but= Tk.Button(root, text="Page 1", command=p1)

page2button= Tk.Button(root, text="Page 2", command=p2)

#load onto Page 1 instantly
p1()



wellabl = Tk.Label(Home, text="Welcome! Press the button below to enter the calculator", font=("times", "22"))
wellabl.place(x=0, y=320, width=1000)


#PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2 PAGE 2


appliances = ["Computer", "Phone", "Lamp", "Other" ]


#dropdown menu
choiceapp = Tk.StringVar(dtapage)
choiceapp.set("Press an appliance, please.") #starting value
dropdownapliance = Tk.OptionMenu(dtapage, choiceapp, *appliances)
dropdownapliance.place(x = 10, y = 20)

dev_inp = Tk.Entry(dtapage)
dev_inp.place(x= 65, y= 100)
dev_lbl = Tk.Label(dtapage, text = "Device")
dev_lbl.place(x=5, y= 100, width= 60)

#input your own KWh (kilawatt per hour)
kwh_input_v1 = Tk.Entry(dtapage)
kwh_input_v1.place(x=65, y=130)

#input hours
hour_input_v1 = Tk.Entry(dtapage)
hour_input_v1.place(x=65, y=160)

hourslbl = Tk.Label(dtapage, text="Hours")
hourslbl.place(x= 5, y=160, width= 60)

kwhlbl =Tk.Label(dtapage, text = "Kwh")
kwhlbl.place(x=5, y=130, width= 60)

items = {
    
    "Computer": 0.8,
    "Phone": 0.4,
    "Lamp": 0.1,
    "Other": kwh_input_v1.get
}


def check():
    if hour_input_v1.get() == "": #checks if Hours is empty
        Hours_Null = Tk.Label(dtapage, text=  "Please input your hours")
        Hours_Null.place(x= 5, y= 370, width= 300, height= 40)
    else:
        if kwh_input_v1.get() == "": #checks if Kwh is empty
            Kwh_Null = Tk.Label(dtapage, text=  "Please input the Kwh of your device") 
            Kwh_Null.place(x= 5, y= 370, width= 300, height= 40)
        else:
            if choiceapp.get() == "Press an appliance, please.": #checks if an appliance is selected
                Hours_Null = Tk.Label(dtapage, text=  "Please select your device")
                Hours_Null.place(x= 5, y= 370, width= 300, height= 40)
            else:
                appliances.append(dev_inp.get()) 
                print(appliances)
                press() #runs the calculations
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


calculat = Tk.Button(dtapage, text="submit", command=check)
calculat.place(x=5, y=200)

#output choice
totalKWH = Tk.Label(dtapage, text="Your total KWH will show here:")
totalKWH.place(x=5, y=250)
totalcarb = Tk.Label(dtapage ,text="Your total Carbon will show here:")
totalcarb.place(x=5, y=290)
totalmoney = Tk.Label(dtapage ,text="Your total money will show here:")
totalmoney.place(x=5, y=330)

root.mainloop()