import tkinter as tk

# Functions go here:
def decision():
    try:
        fee_monthly = float(ent_monthly.get())
    except:
        fee_monthly = 0
    try:
        fee_once = float(ent_once.get())
    except:
        fee_once = 0
    try:
        gymfreq = 30/(float(ent_freq.get()))
    except:
        gymfreq = 0
    fee = gymfreq * fee_once
    if fee >= fee_monthly:
        ans = "It is recommended to take up the monthly membership."
    elif fee < fee_monthly:
        ans = "You're better off just paying per entry."
    ftp = "Fee to pay per month: RM{:.2f}".format(fee)
    lbl_ans["text"] = ans
    lbl_ftp["text"] = ftp

win = tk.Tk()
win.title("To go or not to go?")

# Time to put in the GUI parts!
frm1 = tk.Frame(master=win)
frm2 = tk.Frame(master=win)

lbl_monthly = tk.Label(master=frm1,
text="Gym monthly membership fee: ")
ent_monthly = tk.Entry(master=frm1)
lbl_once = tk.Label(master=frm1, text="Gym single entry fee: ")
ent_once = tk.Entry(master=frm1)
lbl_freq = tk.Label(master=frm1, text="Go to gym once per how many days?: ")
ent_freq = tk.Entry(master=frm1)

btn_magic = tk.Button(master=frm2, text="Make the judgement", command=decision)
lbl_ans = tk.Label(master=frm2)
lbl_ftp = tk.Label(master=frm2)

# The .grid() stuff
lbl_monthly.grid(row=0, column=0, sticky="e")
ent_monthly.grid(row=0, column=1, padx=10, sticky="w")
lbl_once.grid(row=1, column=0, sticky="e")
ent_once.grid(row=1, column=1, padx=10, sticky="w")
lbl_freq.grid(row=2, column=0, sticky="e")
ent_freq.grid(row=2, column=1, padx=10, sticky="w")
frm1.grid(row=0, column=0, padx=10)

btn_magic.grid(row=0, column=0)
lbl_ans.grid(row=1, column=0, sticky="w")
lbl_ftp.grid(row=2, column=0, sticky="w")
frm2.grid(row=1, column=0, padx=10)

win.mainloop()
