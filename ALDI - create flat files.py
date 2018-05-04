#check row number to be 0

import pandas as pd
import os
import csv
import glob
wr=r'C:\Users\Shravya.Shanmukh\Desktop\Work\ALDI\Output\Flat_CSV3.csv'
DIR=r'C:\Users\Shravya.Shanmukh\Desktop\Work\ALDI\\'
os.chdir(r'C:\Users\Shravya.Shanmukh\Desktop\Work\ALDI\\')
results = pd.DataFrame([])
item = pd.DataFrame([])
result = pd.DataFrame([])
for counter, file in enumerate(glob.glob(os.path.join('',"*.csv"))):
    num_of_files=len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    #print(num_of_files)
    i=0
    j=0
    #if (counter==0):
    f=pd.read_csv(file,skiprows=9)
    h=pd.read_csv(file,index_col=0,usecols=[0,1],skiprows=3,nrows=5,header=None)
    results=results.append(f)
    while (j<len(f.index)):
        item=item.append(h.iloc[3])
        j+=1
    
    result = pd.concat([results.reset_index(drop=True),item.reset_index(drop=True)], axis=1)

#result         
result.to_csv(wr)     