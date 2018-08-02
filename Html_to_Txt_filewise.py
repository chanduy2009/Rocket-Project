# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 16:04:34 2018

@author: User
"""


import pandas as pd
import numpy as np
import xlwt
import re
import cgi
import os #os module imported here
import csv
import io
file='E:/Data Science/BI/Rocket Project/0000001750/0000001750__2008-08-29.txt' # get present working directory location here
for line in file:   
        #print(file)
        table_data=[]       
        test_file=open(file, 'r')
        lines = test_file.readlines()
       
        
#print(html)
        tag_re = re.compile(r'(<!--.*?-->|<[^>]*>)')
        
        
        f= open("E:/Data Science/BI/Rocket Project/0000001750/0000001750__2008-08-29_output.txt","w+")
         #f.write(str(func(file))
        for i in lines:
                 no_tags = tag_re.sub('',i) 
                 no_tags = no_tags.replace("&nbsp;" , '')
                 table_data.append(no_tags)
                 f.write(no_tags)



