# -*- coding: utf-8 -*-
"""

-----------Dispersal Velocity Calculator--------

@author: Tim Holt
Version 1

This program is designed to calculate the dispersal velocity of orbiral objects in semi-major axis (a), eccentricity (e), inclination (i) space. 

2019-06-17 forked to deal with Jovian Trojans rather than Satellites. 

--Input--
The input matrix must be a csv file, created from the Astdys Trojan DB. delta-a are in AU. e is a non-parametric value. Inclination is presented as sinI. 
Only values must be used in the matrix, no units. The first object is used as the reference object. Name of the reference object is taken as name of the cluster.  
The true anomaly (w) and perihelion argument (f) are from the point of impact and dispersion. As this is generally unkown, values muct be inputted. 

--Output--
A text file with the dispersal velocities for each object to the reference object. Only values are given not units. 
minimum, maximum mean and SD values for the cluster

#Versions
02 - updtated so a ficticiouse central object can be used. 
03 - chaging Gausse equ to def.
04 - Inputting new database - eg Trojan-FamilyData-20190716-144734.csv - pulls from a list rather than a file
05 - Added in the Escape velocity and the families
06 - Summary data
07 - Updated to include if any escape
075 - moved some families around and updated to 2 decimal places
0.76 - Making the individual stats output to a bunch of csv files
0.8 - updated to use a pickled version of the family sets
0.81 - new dataset using MOVIS. Update for Clone pool. 
0.82 - Selecting some of the important stuff
0.83 - updated to work on laptop and using the full dataset

"""

#modules
import numpy as np
#import matplotlib.pyplot as plt 
import pandas as pd
import math
import sys
import time
#from astroquery.jplhorizons import Horizons
#from astropy.table import vstack as astpyvstack
from datetime import datetime
import pickle


#--- input peramiters---

file = 'C:/Users/afsan/Documents/AstroTemp/Trojan-FamilyData-20200309-132525.csv'                            #csv file
data = pd.read_csv(file,low_memory=False)
data = data.set_index('Name', drop=False)

#Escape datafiles
EscapePoolData = pd.read_csv('C:/Users/afsan/Documents/AstroTemp/JovTrojanEscapesDB-CloneescapeData-20200310-161455.csv',low_memory=False)
poolnumber = 9


EscapeOrgData = pd.read_csv('C:/Users/afsan/Documents/AstroTemp/JovTrojanEscapes-OrgAstDysClean-20190903-075640.csv',low_memory=False)
EscapeOrgData = EscapeOrgData.set_index('Name', drop=False)

#Swarm Files
L4Data = data[data['L'] == 4]
L5Data = data[data['L'] == 5]

#bringing in the Pickled clan list
pickleinfile = open('C:/Users/afsan/Documents/AstroTemp/JTCladistics/SubSetClanlistChecked.pkl', 'rb')
#pickleinfile = open('SubSetClanlist.pkl', 'rb')
Familylist = pickle.load(pickleinfile)
pickleinfile.close()

pd.set_option('max_rows', 999999)   #to make sure it doesn't truncate.
pd.set_option('max_columns', 999999)

# Unkown values that need to be entered 
fdeg = 90                                       # true anomaly (f) in degrees (90)
fwdeg = 45                                      # perihelion argument (f + w) in degrees (45)
density = 800                                   # bulk density in kg/m3
G = 6.67408e-11                                 # Gravitational constant in m3 kg-1 s-2


AsumtionDiam = 1                                #if the Diameter is not know, assume it is X. In KM

VeloCE = np.sqrt(8/3*G*density*np.pi)
VeloCEDI = np.sqrt(8/3*G*density*np.pi)*500

start = datetime.now()		#start time




#add on an additional columns for the volume and dispersal velocities
#data['diameter'].fillna(AsumtionDiam, inplace=True)   #filling in the obects where no diameter is known.      
data['radius'] = (data['diameter']/2)*1000
data['vol'] = 4.0/3.0*np.pi*(data['radius'])**3
data['dVrefobj'] = np.nan
data['dVmean'] = np.nan


#escape information
#data['EscapeTime-Org'] = data['Name'].isin(EscapeOrgData['Name'])
#data.loc[data['Name'].isin(EscapeOrgData['Name']), 'EscapeTime-Org'] = EscapeOrgData['EscapeTime']
data['EscapeTime-Org'] = EscapeOrgData['EscapeTime']

#Escape Fraction
escapepoolcounts = EscapePoolData.Name.value_counts()
data['EscapePoolCount'] = escapepoolcounts
data['EscapePoolFrac'] = data['EscapePoolCount']/poolnumber

#data.to_csv('test.csv')


#dictionary of Family data
Famdata = {}
for fam, values in Familylist.items():
    valuesnew = list(map(str, values))   #converting to a list of strings
    Familylist[fam] = valuesnew
    #Making a family database
    Famdata[fam] = data[data['Name'].isin(valuesnew)] 

#-Dataframe of Family Summary data-
#Family Name, Number of objects, Escape velocity of ref obj, Mean Delta V from Ref obj, SD Delta V from Ref obj, Escape velocity of cluster, Mean Delta V from mean of cluster, SD Delta V mean of cluster, Ref object diameter, Faction of the Cluster volume of the ref obj, Number of objects in cluster over 50%  and 75%Vol, Number of objects that escape in the swarms Org is original paricle, Mean is mean of clones. 
FamDataSumColums = ['Name_fam','No-obj','V_esc-ref','Dv_Ref-Mean', 'Dv_Ref-Sd','V_esc-M','Dv_M-Mean', 'Dv_M-Sd', 'D_refobj', 'Frac_refobj', 'No.>0.5Vol', 'No.>0.75Vol', 'No.Escape_Org', 'Frac_Escape_Org', 'No.Escape_Pool','Frac_Escape_Pool']    
FamDataSum = pd.DataFrame(columns=FamDataSumColums)



#---Calculation paramiters---
#f and F+w to radians
f = math.radians(fdeg)
fw = math.radians(fwdeg)

def GauseEqu(da, de, di, ar, er, ir, p):      #d=delta, r=reference, p=period
    #period translated into seconds from days - translated into orbital frequency
    psec = p * 86400
    n = ((2 * math.pi) / psec)
    
    dvreq1 = (n*ar)/(math.sin(f)*(math.sqrt(1-er**2)))
    dvreq2 = (de*((1+er*math.cos(f))**2))/(1-er**2)
    dvreq3 = (da*(er+2*math.cos(f)+er*(math.cos(f)*math.cos(f))))/(2*ar)
    dVR = dvreq1*((dvreq2)-(dvreq3)) 
 
    
    dvteq1 = (n*ar)*(1+er*math.cos(f))
    dvteq2 = math.sqrt(1-er**2)
    dvteq3 = da/(2*ar)
    dvteq4 = (er*de)/(1-er**2)
    
    dVT = (dvteq1/dvteq2)*(dvteq3-dvteq4)
    #dVT = ((n*ar*(1+er*math.cos(f)))/(math.sqrt(1-er**2)))*((da/2*ar)-((er*de)/(1-er**2)))
    

    dVW = ((n*ar*di)/(math.sqrt(1-er**2)))*((1+er*math.cos(f))/(math.cos(fw)))

   
    #the combined velocity formula
    dV = math.sqrt(dVR**2+dVT**2+dVW**2)
    '''
    #print outputs
    print('dVR = ', dVR)    
    print('dVT =', dVT)
    print('dVW =', dVW)    
    print('dV =', dV)
    '''
    return dV




#sending the output to a text file.
DatetimeNow = time.strftime("%Y%m%d-%H%M%S")
outputfile = 'Trojan-Family-DispersalVelocity-{}'.format(DatetimeNow)
orig_stdout = sys.stdout
outputtext = outputfile+'.txt'
sys.stdout = open(outputtext,'wt')





print('---------------- Jovian Trojan Families & clusters ----------------')
#--reference values--
print('')
print ('---Reference values---')
print ('f = ',fdeg, 'degrees ---- f + w = ', fwdeg, 'degrees')

#working on each family
for famname, clusterdata in Famdata.items():
    print('')
    print('------', famname, 'cluster -------')
    print('')
    print('-----', famname, '-----', file=sys.stderr)
    JTtime = datetime.now() - start  
    print('Startime: ', JTtime, file=sys.stderr)
    #print(clusterdata)
    clustersize = len(clusterdata.index)
    print('Cluster size: ', clustersize)
    print('')
    #selecting the reference object
    refobject = clusterdata.loc[clusterdata['diameter'].idxmax()]
    print('-Reference object-')
    print(refobject['full_name'])
    #ar = 1000*data.iloc[0][ 'da(AU)']                     #Semimajor axis in km to m
    arefobj = 149597870700*refobject['da(AU)']                     #Semimajor axis in au to m
    erefobj = refobject['e_astdys']                          #eccentricity
    irefobj = refobject['sinI']
    prefojt = refobject['per']
    #escape velocity of reference object
    refobjmass = refobject['vol']*density
    refvescapte = np.sqrt((2*G*refobjmass)/(refobject['radius']))

    print('Semi-major axis:', arefobj, 'm')
    print('Eccentricity:', erefobj)
    print('Sine Inclination:', irefobj)
    print('Period:', prefojt, 'days')
    print('Escape Velocity:', refvescapte, 'm/s')
    print('')    

    #mean of cluster
    armean = 149597870700*clusterdata['da(AU)'].mean()            #Semimajor axis in au to m
    ermean = clusterdata['e_astdys'].mean()
    irmean = clusterdata['sinI'].mean()
    pmean = clusterdata['per'].mean() 
    #escape velocity of the cluster
    clustervol = clusterdata['vol'].sum()
    clusterrad = sum(clusterdata['radius'])
    clusterescape = VeloCE*clusterrad
    
    print('-mean-')
    print('Semi-major axis:', armean, 'm')
    print('Eccentricity:', ermean)
    print('Sine Inclination:', irmean)
    print('Peroid:', pmean, 'days')
    print('Cluster Escape Velocity',clusterescape,'m/s')
        
    print ('')
    
    #difference between means and reference
    print('-Difference-')
    adiff = abs(arefobj-armean)
    ediff = abs(erefobj-ermean)
    idiff = abs(irefobj-irmean)
    pdiff = abs(prefojt-pmean)

    print('Semi-major axis:', adiff, 'm')
    print('Eccentricity:', ediff)
    print('Sine Inclination:', idiff)
    print('Peroid:', pdiff, 'days')
    print ('')
    
    #loop through each of the lines in the array
    for index, row in clusterdata.iterrows():
        #Reference object
        #da = (1000*row[ 'da(AU)'])-ar                     ##Semimajor axis in km to m
        daRef = (149597870700*row[ 'da(AU)'])-arefobj              ##Semimajor axis in au to m    
        deRef = row['e_astdys']-erefobj                            #eccentricity
        diRef = row['sinI']-irefobj                     #inclination, givin that it is already in sin i
        #di = math.sin(math.radians(row['i']))-ir    #inclination in deg to radians
        #gause equation
        dVrefobj = GauseEqu(daRef, deRef, diRef, arefobj, erefobj, irefobj, prefojt)
        Famdata[famname].loc[index,'dVrefobj'] = dVrefobj  #updating the velocity into the dataframe
 
        #mean of the set
        #da = (1000*row[ 'da(AU)'])-ar                     ##Semimajor axis in km to m
        daMean = (149597870700*row[ 'da(AU)'])-armean              ##Semimajor axis in au to m    
        deMean = row['e_astdys']-ermean                            #eccentricity
        diMean = row['sinI']-irmean                     #inclination, givin that it is already in sin i
        #di = math.sin(math.radians(row['i']))-ir    #inclination in deg to radians    
        #gause equation
        dVmean = GauseEqu(daMean, deMean, diMean, armean, ermean, irmean, pmean)
        Famdata[famname].loc[index,'dVmean'] = dVmean   #updating the velocity into the dataframe
                   
        
        '''
        #print outputs
        print('--{}--'.format(row['full_name']))
        print('-reference object-')
        print('da = ',daRef)
        print('de = ',deRef)
        print('di = ',diRef)
        print('')
        print('-Mean of Set-')
        print('da = ',daMean)
        print('de = ',deMean)
        print('di = ',diMean)
        '''
    #--end of loop--
    #-----Updated dataframe-------    
    print ('--Summary and statistics --')
    Clusterindistats = clusterdata[['full_name','diameter','dVrefobj', 'dVmean', 'EscapePoolFrac']].round(2)

    
    print ('')
    print (Clusterindistats)
    print ('')
    

    #----Statistics-----
    #minimum, maximum mean and SD values for the cluster
    #print them, perhaps output to a text file. 
    
    NumescapeOrg = clusterdata['EscapeTime-Org'].count()
    NumescapePool = clusterdata['EscapePoolCount'].sum()
    fracescapeOrg = round(NumescapeOrg/clustersize, 3)
    fracescapePool = round(NumescapePool/poolnumber/clustersize, 3)
    
    print('Number of original objects that escape: ', NumescapeOrg)
    print('Fraction of original objects that escape: ',fracescapeOrg)
    print('Number of Pool clones that escape: ', NumescapePool)
    print('Fraction of Pool clones that escape: ', fracescapePool)
        
    clusterdata = clusterdata.replace(0, np.NaN)              #to get rid of the '0' value for the reference 
    print('-Reference object-')
    RefObVolFrac = round(refobject['vol']/clustervol,3)
    print('Ref obj fraction of cluster:', RefObVolFrac)
    
    #number of objects larger than a specific volume
    NoObj50 = len(clusterdata[clusterdata['vol']>0.5*refobject['vol']])-1
    NoObj75 = len(clusterdata[clusterdata['vol']>0.75*refobject['vol']])-1 
    NoObj100 = len(clusterdata[clusterdata['diameter']>100])
    
    obj50 = clusterdata['full_name'][(clusterdata['vol']>0.50*refobject['vol']) & (clusterdata['full_name'] != refobject['full_name'])]  
    obj75 = clusterdata['full_name'][(clusterdata['vol']>0.75*refobject['vol']) & (clusterdata['full_name'] != refobject['full_name'])]

    
    
    print('Number of Objects larger than 50% of Ref obj:',NoObj50)
    print('Objects: ',obj50.to_string(index=False))
    print('Number of Objects larger than 75% of Ref obj:',NoObj75)
    print('Objects: ',obj75.to_string(index=False))
    print('No of Objects >100km diameter: ', NoObj100)
    Vmin = clusterdata['dVrefobj'].min()
    print ('Minimum deltaV value', Vmin, 'm/s')    
    Vmax = clusterdata['dVrefobj'].max()
    print ('Maximum deltaV value', Vmax, 'm/s')
       
    Vmean = clusterdata['dVrefobj'].mean()
    print ('Mean deltaV value', Vmean, 'm/s')    
    Vstd = clusterdata['dVrefobj'].std()
    print ('Standard deviation of deltaV value', Vstd, 'm/s')   

    
    print('')
    print('-mean of Set-')
    Vclustmin = clusterdata['dVmean'].min()
    print ('Minimum deltaV value', Vclustmin, 'm/s')    
    Vclustmax = clusterdata['dVmean'].max()
    print ('Maximum deltaV value', Vclustmax, 'm/s')    
    Vclustmean = clusterdata['dVmean'].mean()
    print ('Mean deltaV value',Vclustmean, 'm/s')    
    Vcluststd = clusterdata['dVmean'].std()
    print ('Standard deviation of deltaV value', Vcluststd, 'm/s')
    
    #['Name_fam','V_esc-ref','Dv_Ref-Mean', 'Dv_Ref-Sd','V_esc-M','Dv_M-Mean', 'Dv_M-Sd', 'D_refobj', 'No.>0.5Vol', 'No.>0.75Vol']    
    famsum = pd.DataFrame([[famname, clustersize, refvescapte, Vmean, Vstd, clusterescape, Vclustmean, Vcluststd, refobject['diameter'], RefObVolFrac, NoObj50, NoObj75,NumescapeOrg,fracescapeOrg,NumescapePool, fracescapePool]], columns=FamDataSumColums)
    FamDataSum = FamDataSum.append(famsum, ignore_index=True)
    
    
    #output to a CSV
       
    clusterheader= ['full_name','$D$','$\Delta V_{ref}$', '$\Delta V_{cent.}$', '$F_{esc}$']
    Clusterindistats['EscapePoolFrac'] = Clusterindistats['EscapePoolFrac'].map('{:.2E}'.format)
    Clusterindistats['EscapePoolFrac'] = Clusterindistats['EscapePoolFrac'].replace('NAN','-')
    clustercsvfilename = 'JTCluster-{}-{}.csv'.format(famname,clustersize)
    clusterlatexfilename = 'JTClusterTable-{}-{}.txt'.format(famname,clustersize)
    
    Clusterindistats.to_csv(clustercsvfilename, index=False, header=clusterheader)
    Clusterindistats.to_latex(clusterlatexfilename, index=False, header=clusterheader)
    
FamDataSum = FamDataSum.set_index('Name_fam')
print("")
print('---------------------Summary of all Families------------------')
print('Family Name, Number of objects,Escape velocity of ref obj, Mean Delta V from Ref obj, SD Delta V from Ref obj, Escape velocity of cluster, Mean Delta V from mean of cluster, SD Delta V mean of cluster, Ref object diameter, Faction of the Cluster volume of the ref obj, Number of objects in cluster over 50%  and 75%Vol, Number and fraction of objects that escape in the swarms Org is original paricle, Pool is pool of clones. ')
print("")
print(FamDataSum)

#some cleaning up
FamDataSum = FamDataSum.round(2)   #rounding to 2 decimal places
FamDataSum['Dv_Ref'] = FamDataSum[['Dv_Ref-Mean', 'Dv_Ref-Sd']].astype(str).apply(lambda x: '±'.join(x), axis=1)
FamDataSum['Dv_M'] = FamDataSum[['Dv_M-Mean', 'Dv_M-Sd']].astype(str).apply(lambda x: '±'.join(x), axis=1)
FamDataSum.to_csv(outputfile+'-Sum.csv')

#important info
FamDataImpSum = FamDataSum[['No-obj', 'D_refobj','V_esc-ref', 'Frac_Escape_Pool','Dv_Ref', 'Dv_M']]
FamDataImpSum['Frac_Escape_Pool'] = FamDataImpSum['Frac_Escape_Pool'].fillna('-')
FamDataImpSum.to_csv(outputfile+'-ImportSum.csv')
   
'''

#----Graphs----
#a vs e
plt.figure(1) 
plt.grid()
plt.scatter(data[ 'da(AU)'], data['e'])  
#plt.annotate((data[ 'da(AU)'], data['e']), data['Name'])
plt.title(family+' family: Semimajor axis vs Eccentricty')
plt.xlabel('a (km)')
plt.ylabel('e')
saveae = outputfile+'.ae.pdf'
plt.savefig(saveae)
#plt.show()

#a vs i
plt.figure(2) 
plt.grid()
plt.scatter(data[ 'da(AU)'], data['i'])  
#plt.annotate((data[ 'da(AU)'], data['e']), data['Name'])
plt.title(family+' family: Semimajor axis vs Inclination')
plt.xlabel('a (km)')
plt.ylabel('i (degrees)')
saveai = outputfile+'.ai.pdf'
plt.savefig(saveai)
#plt.show()


#a vs e vs i (3d)
threedee = plt.figure().gca(projection='3d')
threedee.scatter(data[ 'da(AU)'], data['e'], data['i'])
threedee.set_title(family+' family: Semimajor axis vs Eccentricity vs Inclination')
threedee.set_xlabel('a (km)')
threedee.set_ylabel('e')
threedee.set_zlabel('i (degrees)')
saveaei = outputfile+'.aei.pdf'
plt.savefig(saveaei)
#plt.show()




'''

end = datetime.now()
print("")
print("Total Run Time:", end - start)	
print("Total Run Time:", end - start, file=sys.stderr)

#closing the textfile
sys.stdout.close()
sys.stdout=orig_stdout 

