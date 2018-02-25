#This code works

import pandas as pd
from datetime import datetime

file=pd.read_csv(r'C:\Users\Shravya.Shanmukh\Desktop\Work\Watson\ZTE\LG.csv',encoding='iso-8859-1')

con=file['Contents']
i=0
#con.head(5)
datestring_clean = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
for index, row in con.iteritems():
    if i > len(con):
        break
    else:
        out = open(r'C:\Users\Shravya.Shanmukh\Desktop\Work\Watson\ZTE\input_LG\lg' + str(i)+ '.txt', 'w',encoding='iso-8859-1')
        out.write(row)
        out.close()
        i+=1