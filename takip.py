'''
read a config file
in the config file where is the plaka and date information
we assume plaka -> 0
date -> 1
'''

import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta



def main():
   today = datetime.today()
   all_cars = []
   df = pd.read_excel("araclar.xlsx", usecols=[0,1], engine="openpyxl")
   for idx, row in df.iterrows():
      temp = {}
      muayene_bitis = row.iloc[1] + relativedelta(years=1) #add one year --> can be 2 years for normal cars
      kalan_gun = (muayene_bitis-today).days
      temp["plaka"] = row.iloc[0]
      temp["kalan_gun"] = kalan_gun
      if kalan_gun <= 0:
         print(f"{temp['plaka']} - MUAYENE TARIHI GECMIS!")
      all_cars.append(temp)
   sorted_data = sorted(all_cars, key=lambda x: x['kalan_gun'])
   prettyprint(sorted_data)


def prettyprint(mylist):
   print("Araclarin bir sonraki muayene gunlerine kalan vakit")
   print("----------------------")
   for data in mylist:
      print(f"{data['plaka']} -> {data['kalan_gun']} gun kaldi")
   print("")
   print("")
   input("Kapatmak icin bir tusa basin")



      
      
   



main()
