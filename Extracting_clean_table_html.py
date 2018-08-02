# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 18:50:16 2018

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:05:42 2018

@author: User
"""

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import lxml
import html5lib
import csv

path = 'E:/Data Science/BI/Rocket Project/0000001750/0000001750__2006-09-01.htm'
path1='E:/Data Science/BI/Rocket Project/0000001750/Output_2006.csv'

#extracting the summary compensation table from html file
dfhtml = pd.read_html(path,match="Bonus")
len(dfhtml)
dfhtml
type(dfhtml)

#Converting list to string and removing the NaN
htmltxt=str(dfhtml)
txtnew=htmltxt.replace("NaN","")
print(txtnew)

#writing the list to text file
f=open('E:/Data Science/BI/Rocket Project/0000001750/Output_2006.txt','w')
f.writelines(str(txtnew))
f.close()
















#df1=dfhtml[0].replace(np.NaN,np.nan)
df2=dfhtml[0].dropna(axis=1, how='all') 
df2=df2.dropna(thresh=1)
#df2.iloc[0:2,:]  # Displaying the Rows with the Titles only.
