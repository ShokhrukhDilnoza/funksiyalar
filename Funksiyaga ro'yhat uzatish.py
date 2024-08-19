# -*- Funksiyaga ro'yxat uzatish-*-
"""
Created on Mon Aug  5 16:12:32 2024

@author: user
"""
def bahola(ismlar):
    baholar={}
    while ismlar:
        ism=ismlar.pop()
        baho=input(f"Talaba {ism.title()}ning bahosini kiriting:>> ")
        baholar[ism]=int(baho)
    return baholar

talabalar=['ali', 'vali', 'hasan', 'husan']
baholar=bahola(talabalar)
print(f"Talabalaring baholari quyidagicha: \n{baholar}")
