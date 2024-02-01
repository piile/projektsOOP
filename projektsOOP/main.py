from modulis import Modulis
import pandas as pd
from tkinter import *
from tkinter import ttk


window = Tk()
window.geometry("500x500")

modulis = Modulis()
produkti = modulis.iegut_nosaukumus()

virsraksts = Label(window, text = "Izvēlies savu maltīti")
virsraksts.pack()

produkta_izvele1 = ttk.Combobox(window, values=produkti)
produkta_izvele1.pack()

produkta_izvele2 = ttk.Combobox(window, values=produkti)
produkta_izvele2.pack()

produkta_izvele3 = ttk.Combobox(window, values=produkti)
produkta_izvele3.pack()

rezultats = Label(window)
rezultats.pack()

def izrekinat(produkts1, produkts2, produkts3):
    proteini_summa = produkts1[1]+produkts2[1]+produkts3[1]
    tauki_summa = produkts1[2]+produkts2[2]+produkts3[2]
    oglhidrati_summa = produkts1[3]+produkts2[3]+produkts3[3]
    energetiska_summa = produkts1[4]+produkts2[4]+produkts3[4]
    rezultats['text']=f"Jūsu izvēlētajā maltītē ir \n {proteini_summa} proteīni \n {tauki_summa} tauki \n {oglhidrati_summa} ogļhidrāti \n {energetiska_summa} enerģētiskā vērtība"

def parbaudit():
    produkts1 = produkta_izvele1.get()
    produkts2 = produkta_izvele2.get()
    produkts3 = produkta_izvele3.get()
    produkts1_info = modulis.iegut_datus(produkts1)
    produkts2_info = modulis.iegut_datus(produkts2)
    produkts3_info = modulis.iegut_datus(produkts3)
    print(produkts1_info, produkts2_info, produkts3_info)
    izrekinat(produkts1_info, produkts2_info, produkts3_info)

apstiprinasanas_poga = Button(window, text = "Pārbaudīt", command=parbaudit)
apstiprinasanas_poga.pack()



window.mainloop()