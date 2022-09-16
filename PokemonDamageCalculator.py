from __future__ import division
import tkinter as tk 
from tkinter import *




#def testbutton():
    #level = lvlentry.get()
    #print(level)

#50, 60, 70, 80, 1.5, 2 = 75.3
#--------------VVVdamage calculatorVVV-------------------------------------------------------

def calculatecmd():
    level = int(lvlentry.get())
    base_power = int(powerentry.get())
    atkvalue = int(ATKentry.get())
    defvalue = int(DEFentry.get())
    STABYN = int(STABvar.get())
    supereffYN = int(Supervar.get())
    STAB = 1
    supereff = 1
    if STABvar.get() == 1:
        STAB = 1.5
    else:
        STAB = 1
    if Supervar.get() == 1:
        supereff = 2
    else:
        supereff = 1
        
    damageresult.configure(text="Damage: "+ str(((((((2*level)/5)+2)*base_power*(atkvalue/defvalue))/50)+2)*(STAB*supereff)))


root = tk.Tk()
#--------------VVV main label VVV------------------------------------------------------------

prompt = tk.Label(root,
                text = 'Simple Pokemon Damage Calculator',
                fg = 'black',
                font = "Helvetica 20 bold")
prompt.grid(row = 0, column = 0)

#--------------VVV explanation text VVV-------------------------------------------------------

exp_msg = tk.Label(root, text = "This simple damage calculator will determine how much HP\n your move will subtract from the opposing pokemon", 
                            fg = 'black', 
                            font = "Arial 16")
exp_msg.grid(row = 1, column = 0)

#-----VVV input values (level, move base power, attack value/defense value) VVV---------------

lvlentry_txt = tk.Label(root, text = "Your Pokemon's Level", 
                            fg = 'black', 
                            font = "Arial 12").grid(row=3, column=0, sticky=tk.W)
lvlentry = tk.Entry(root)
lvlentry.grid(row=4, column=0, sticky=tk.W+tk.N, padx=4)

#---

powerentry_txt = tk.Label(root, text = "The Move's Base Power", 
                            fg = 'black', 
                            font = "Arial 12").grid(row=5, column=0, sticky=tk.W)
powerentry = tk.Entry(root)
powerentry.grid(row=6, column=0, sticky=tk.W+tk.N, padx=4)

#---

ATKentry_txt = tk.Label(root, text = "Your Pokemon's Attack/Sp. Attack Stat", 
                            fg = 'black', 
                            font = "Arial 12").grid(row=7, column=0, sticky=tk.W)
ATKentry = tk.Entry(root)
ATKentry.grid(row=8, column=0, sticky=tk.W+tk.N, padx=4)

#---

DEFentry_txt = tk.Label(root, text = "Opposing Pokemon's Defense/Sp. Defense Stat", 
                            fg = 'black', 
                            font = "Arial 12").grid(row=9, column=0, sticky=tk.W)
DEFentry = tk.Entry(root)
DEFentry.grid(row=10, column=0, sticky=tk.W+tk.N, padx=4)

#--------------VVV Yes/No Values (STAB, supereffective) VVV-----------------------------------------------------

STABvar = IntVar()
STABchk_txt = Checkbutton(root, text = "Does the pokemon have STAB? (Same Type Attack Bonus)", 
                            fg = 'black', 
                            font = "Arial 12",
                            variable=STABvar)
STABchk_txt.grid(row=11, column=0, sticky=tk.W, pady=10)

#---

Supervar = IntVar()
Superchk_txt = Checkbutton(root, text = "Is the move supereffective against the opponsing Pokemon?", 
                            fg = 'black', 
                            font = "Arial 12",
                            variable=Supervar)
Superchk_txt.grid(row=12, column=0, sticky=tk.W,)

#--------------VVV quit button VVV-----------------------------------------------------

quitbutton = tk.Button(root, 
                   text = "quit", 
                   fg = "red",
                   command=root.destroy
                   )
quitbutton.grid(row = 20, column = 2)

#---------------VVV calculate button VVV---------------------------------------------------------

calculate = tk.Button(root,
                            text = "Calculate",
                            fg = '#008080',
                            font = "Helvetica 14",
                            command = calculatecmd)
calculate.grid(row = 18, column = 0)

#---------------VVV Damage Result VVV----------------------------------------------------------------------------

damageresult = tk.Label(root, text = "Damage: ", 
                            fg = 'black', 
                            font = "Arial 12")
damageresult.grid(row=19, column=0) 

#-------------------------------------------------------------------------------------------

root.mainloop()