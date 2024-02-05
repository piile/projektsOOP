import pandas as pd

class Modulis:
    def __init__(self, fails):
        self.fails = fails
        self.fails = pd.read_csv(self.fails)
    def iegut_nosaukumus(self):
        product_list = self.fails['Products'].tolist()
        return product_list
    def iegut_datus(self, nosaukums):
        info_produkts = self.fails[self.fails['Products']==nosaukums].iloc[0]
        info_produkts = info_produkts.tolist()
        return info_produkts