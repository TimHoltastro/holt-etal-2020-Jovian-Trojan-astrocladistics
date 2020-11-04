# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:21:25 2017


-------------------Cladistical Binning Program-----------------------

Version 1.0

@author: Tim

The aim of this program is to take continious data and put it into bins, in prperation for use in cladistical analysis. 
"""

#modules
import numpy as np
from scipy import stats
import pandas as pd
import time
import sys


'''
----------------------------Variables------------------------------
These are to be inputted
'''

#csv file
file = 'JovTrojanSubMatrixWiseGaiaSDSSMOVISL520191122-115418.csv'

#Columns to be binned - remember it starts with 0, which should be names anyway
allcol = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

#reversed columns - if the bins need to be itterated largest to smallest
revcol = [0] #or [5]                    #-----need to use 'or' oporator between them, use 0 for none. 

#r^2 threshold - the threshold for an acceptable r^2 value
r2thresh = 0.99

#max bins - maximum number of bins - Mesquite likes upto 55, TNT is being anoying and likeing 15.
#1.5 change to having minimal bin number
binamin = 0 
binsmax = 15


'''
Generated values
'''
#-importing the matrix
data = pd.read_csv(file, encoding = "ISO-8859-1")

#Current date and time
DatetimeNow = time.strftime("%Y%m%d-%H%M%S")

#sending the output to a text file. Accounting for L4 and L5 
if 'L4' in file:
    outputfile = 'CladisticsBins-L4-'+DatetimeNow
    outputtext = outputfile+'.txt'
    sys.stdout = open(outputtext,'wt') 
    data.drop('L', axis=1)
elif 'L5' in file:
    outputfile = 'CladisticsBins-L5-'+DatetimeNow
    outputtext = outputfile+'.txt'
    sys.stdout = open(outputtext,'wt') 
    data.drop('L', axis=1)   
else: 
    outputfile = 'CladisticsBins-'+DatetimeNow
    outputtext = outputfile+'.txt'
    sys.stdout = open(outputtext,'wt')
    #data.drop('L', axis=1) 
    
    

    

#---Print at the top of the Text file
print('----------Cladistics bining Program------------')
print('--Version 1.5---')
print('--Created by Timothy Holt--')
print('')
print('Bins Created:', DatetimeNow)
print('')
print('Matrix used:',file)
print('r^2 thresthold:', r2thresh)


'''
--------Matricies-------------
'''



#print(data)

binstats = np.empty((0,5))              # statics without names get's overridden

#-creating parameters based on matrix



'''
----Finding the bins------
'''
#select the columns
selcol = data.iloc[:,allcol]
revselcol = data.iloc[:,revcol]



#print(selcol)

##-do this for each of the columns-

for column in selcol:
           
    print('')
    print('-----', column, '-----')                           #Printing the column name
        
        
        #--need to deal with ? - changes them to NaN
    seleccolcol = pd.to_numeric(selcol[column], errors='coerce')
        
        #Nans need to be excluded
    selcolnonan = seleccolcol[np.isfinite(seleccolcol)]
        #print(selcolnonan)
        
        
    binNum = binamin
    
       #--- bin loop start--- 
    while True:     
        binNum = binNum + 1
        
        #Creating and assinging bins
        bins = pd.cut(selcolnonan, binNum, labels=False, retbins=True)
        binvalues = bins[0]
        bindelims = bins[1]
         
    
            
  
                    
        #------Stats ---------- 
               
        #print(binsnonan)
    
        #slope(0), intercept(1), r_value(2), p_value(3), std_err(4) = stats.linregress(x,y)
        
        m, b, r, p, err = stats.linregress(selcolnonan, binvalues)
        stat = [m,b,r,p,err]
        binstats = np.append(binstats, [stat], axis=0)
        
        ####-check the r2value- 
            #--if the r2 value is less than r2thresh, redo the binning, with numbin+1. if r2 > r2thresh, stop the loop or if the Max number of bins is reached.
        if stat[2]**2 > r2thresh or binNum == binsmax:
            break

        #--bin loop end-----
        
        
#Reversal
    if column == revselcol.columns:
        binvaluesrevv = np.flipud(binvalues)
        binvaluesrev = pd.Series(binvaluesrevv, index=binvalues.index)
        
        bindelimsrev = np.flipud(bindelims)
        
         

        
    #####-Loop values-
        #--print out the bin values to a text file, with the header and r^2 value

###---Common to forward and reverse----
    #printing the final bin numbers
    print('Bin Number:', binNum)
    #R^2 value.
    print('R^2 value:', stat[2]**2)

    
    
    
    
#Printing forward Bin delimators 
    if column != revselcol.columns:
        print('Bin deliminators:',  bindelims)
        #--update the matrix--  
        data[column].update(binvalues)
    
##---reverse-----    
    if column == revselcol.columns:
        print('Reversed')
        print('Bin deliminators:',  bindelimsrev)
        #--update the matrix--  
        data[column].update(binvaluesrev)

'''
Replacing the larger values with letters for Mesquite

'''

data.replace([10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55],
             ['A','B','C','D','E','F','G','H','K','L','M','N','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','k','l','m','n','p','q','r','s','t','u','v','w','x','y','z'],
             inplace=True)



        
        
'''
Output the data
'''
pd.set_option('max_rows', 999999)   #to make sure it doesn't truncate.
pd.set_option('max_columns', 999999)
print('')
print(data)


#--create a new csv file based on the updated matrix--

outputcsv = outputfile+'.csv'
data.to_csv(outputcsv, index=False)


















