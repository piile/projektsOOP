import pandas as pd


class Modulis:
    def __init__(self):
       ...
    def iegut_nosaukumus(self):
        dati = pd.read_csv('uzturs.csv')
        product_list = dati['Products'].tolist()
        return product_list
    def iegut_datus(self, nosaukums):
        dati = pd.read_csv('uzturs.csv')
        info_produkts = dati[dati['Products']==nosaukums].iloc[0]
        info_produkts = info_produkts.tolist()
        return info_produkts