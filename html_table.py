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
import pickle


path = 'E:/Data Science/BI/Rocket Project/0000001750/0000001750__2006-09-01.htm'
path1='E:/Data Science/BI/Rocket Project/0000001750/Output_2006.csv'

#extracting the summary compensation table from html file
dfhtml = pd.read_html(path,match="Bonus")
len(dfhtml)
dfhtml
type(dfhtml)

#Converting list to data frame
df = pd.DataFrame(dfhtml)
type(df)

df.shape

#writing the list to csv file
with open('E:/Data Science/BI/Rocket Project/0000001750/Output_2006.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(dfhtml)
csvFile.close()
#writing the list to text file

f=open('E:/Data Science/BI/Rocket Project/0000001750/Output_2006.txt','w')
for ele in dfhtml:
    #print(ele)
    f.writelines(str(ele))
f.close()

#Cleaning the text file for removing NaN
f = open('E:/Data Science/BI/Rocket Project/0000001750/Output_2006.txt','r')
filedata = f.read()
filedata.replace("NaN","")
f.write(newdata)
f.close()













InF = open('E:/Data Science/BI/Rocket Project/0000001750/Output_2006.txt', 'w+')
#delete_list = ["NaN"]
for line in InF:
    for word in line:
        word = word.replace("NaN", '')
InF.close()

#
outF.writelines(dfhtml)
outF.close()



#df1=dfhtml[0].replace(np.NaN,np.nan)
df2=dfhtml[0].dropna(axis=1, how='all') 
df2=df2.dropna(thresh=1)
#df2.iloc[0:2,:]  # Displaying the Rows with the Titles only.
