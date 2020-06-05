import xlwt 
import glob
import os
import numpy as np
import pandas as pd
extension = "csv" 
# vyhledá všechny soubory csv ve složce
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# list of dataframes jako agrument
data = [] 
# jméno souboru do sloupce 
for csv in all_filenames:
    frame = pd.read_csv(csv)
    frame['game'] = os.path.basename(csv)
    data.append(frame)
combined_csv = pd.concat(data, ignore_index=True)
# odstranění sloupců, které nechceme 
combined_csv = combined_csv.drop(["event","link","color","val3","date;Owners;event;link;color;Price;val3;game"], axis = 1)
# odstranění .csv z názvu hry 
combined_csv = combined_csv.replace({'.csv':''}, regex=True)
# převedené do excelu 
combined_csv.to_excel( "spojeni_csv.xls", index=False, encoding='utf-8-sig')





