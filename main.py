from modulis import Modulis
from tkinter import *
from tkinter import ttk

class Programma:
    def __init__(self,logs):
        self.logs = logs
        self.fails = "uzturs.csv"
        self.modulis = Modulis(self.fails)
        
        self.produkti = self.modulis.iegut_nosaukumus()
        self.virsraksts = Label(window, text = "Izvēlies savu maltīti pirms sporta stundas")
        self.virsraksts.pack()

        self.produkta_izvele1 = ttk.Combobox(window, values=self.produkti)
        self.produkta_izvele1.pack()

        self.produkta_izvele2 = ttk.Combobox(window, values=self.produkti)
        self.produkta_izvele2.pack()

        self.produkta_izvele3 = ttk.Combobox(window, values=self.produkti)
        self.produkta_izvele3.pack()

        self.rezultats = Label(window)
        self.rezultats.pack()

        def izrekinat(produkts1, produkts2, produkts3):
            proteini_summa = produkts1[1]+produkts2[1]+produkts3[1]
            tauki_summa = produkts1[2]+produkts2[2]+produkts3[2]
            oglhidrati_summa = produkts1[3]+produkts2[3]+produkts3[3]
            energetiska_summa = produkts1[4]+produkts2[4]+produkts3[4]
            self.rezultats['text']=f"Jūsu izvēlētajā maltītē ir \n {proteini_summa} g proteīna \n {tauki_summa} g tauku \n {oglhidrati_summa} g ogļhidrātu \n {energetiska_summa} kJ \n (Pamatojoties uz uz 100 g konkrēta produkta)"

        def parbaudit():
            self.produkts1 = self.produkta_izvele1.get()
            self.produkts2 = self.produkta_izvele2.get()
            self.produkts3 = self.produkta_izvele3.get()
            self.produkts1_info = self.modulis.iegut_datus(self.produkts1)
            self.produkts2_info = self.modulis.iegut_datus(self.produkts2)
            self.produkts3_info = self.modulis.iegut_datus(self.produkts3)
            print(self.produkts1_info, self.produkts2_info, self.produkts3_info)
            izrekinat(self.produkts1_info, self.produkts2_info, self.produkts3_info)

        self.apstiprinasanas_poga = Button(window, text = "Pārbaudīt", command=parbaudit)
        self.apstiprinasanas_poga.pack()

window = Tk()
programma = Programma(window)
window.geometry("500x500")

window.mainloop()