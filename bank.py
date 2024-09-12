import tkinter
from tkinter import messagebox
from tkinter import *

root=Tk()
root.geometry("600x500")
root.title("Banking Tutorial")
root.configure(bg="#326158")
root.resizable(False,False)
font = ("arial", 10, "bold")
balance = 0.0

def depositAmmount():
    global balance
    try:
        ammount = float(AmmountEntry.get())
        if ammount > 0:
            balance+=ammount
            BalanceLabel.config(text=f"Your balance is {balance}$")
            messagebox.showinfo("Success", "Deposit done")
        else:
            messagebox.showerror("Error", "Ammount must be greater then 0$")
    except:
        messagebox.showerror("Error", "Error occured while depositing !")

def whithdrawAmmount():
    global balance
    try:
        ammount = float(AmmountEntry.get())
        if ammount > 0 and ammount <= balance:
            balance-=ammount
            BalanceLabel.config(text=f"Your balance is {balance}$")
            messagebox.showinfo("Success", "Whithdraw done")
        else:
            messagebox.showerror("Error", "Ammount must be greater then 0$ and less then Balance")
    except:
        messagebox.showerror("Error", "Error occured while whihtdrawing !")        

BalanceLabel = Label(root, font=font, text=f"Your balance is {balance}$", width=25, height=5)
BalanceLabel.place(x=100,y=20)

AmmountEntry = Entry(root, font=font, width=15)
AmmountEntry.place(x=100,y=140)

Button(root, text="Deposit here", font=font, width=10, command= depositAmmount).place(x=100,y=200)
Button(root, text="Whithdraw here", font=font, width=10, command= whithdrawAmmount).place(x=100,y=260)


root.mainloop()