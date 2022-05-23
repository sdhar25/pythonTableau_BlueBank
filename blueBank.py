# -*- coding: utf-8 -*-
"""
Created on Sat May  7 15:35:17 2022

@author: Shreya
"""

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#open the file
json_file = open('loan_data_json.json') #read the file
data = json.load(json_file) #load the file in python

#method 2 to read json file
with open('loan_data_json.json') as json_file:
    data = json.load(json_file)

#transform to dataframe
loandata = pd.DataFrame(data) #from list to dataframes

#finding unique values for the purpose clean
loandata['purpose'].unique()

#describe the data
loandata.describe()

#describe any column
loandata['credit.policy'].describe()

loandata['fico'].describe()

loandata['dti'].describe()

#using EXP() to get annual income
income = np.exp(loandata['log.annual.inc'])
loandata['annualincome'] = income

# fico >= 300 and < 400:
# 'Very Poor'
# fico >= 400 and ficoscore < 600:
# 'Poor'
# fico >= 601 and ficoscore < 660:
# 'Fair'
# fico >= 660 and ficoscore < 780:
# 'Good'
# fico >=780:
# 'Excellent'

#fico score
fico=400

if fico >= 300 and fico < 400:
    ficocat = 'Very Poor'
elif fico >= 400 and fico < 600:
    ficocat = 'Poor'
elif fico >= 601 and fico < 660:
    ficocat = 'Fair'
elif fico >= 660 and fico < 780:
    ficocat = 'Good'
elif fico >= 780:
    ficocat='Excellent'
else:
    ficocat='Unknown'
print(ficocat)

#for loop
fruits = ['apple','banana','pear','cherry']
for x in fruits:
    print(x)
    y=x+ ' fruit'
    print(y)

for x in range(0,4):
    y=fruits[x] + ' for sale'
    print(y)
    
#applying for loops to loan data
#try catch

length = len(loandata)
ficocat=[]
for x in range(0,length):
    category = loandata['fico'][x]
    try:
        if category >= 300 and category < 400:
            cat = 'Very Poor'
        elif category >= 400 and category < 600:
            cat = 'Poor'
        elif category >= 601 and category < 660:
            cat = 'Fair'
        elif category >= 660 and category < 780:
            cat = 'Good'
        elif category >= 780:
            cat='Excellent'
        else:
            cat='Unknown'
    except:
        cat='Unknown'
    ficocat.append(cat)
    
#convert to series from list
#SERIES IS A COLUMN IN DATA FRAME
ficocat = pd.Series(ficocat)
loandata['fico.category'] = ficocat

#df.loc as conditional statement
#df.loc[df[columnname] condition,newcolumnname] = 'value if the condition is met'
#for interest rate, a new column is wanted, rate >0.12 then high, else low

loandata.loc[loandata['int.rate'] > 0.12, 'int.rate.type'] = 'High'  
loandata.loc[loandata['int.rate'] < 0.12, 'int.rate.type'] = 'Low'

#number of loans/rows by fico.category
catplot = loandata.groupby(['fico.category']).size()

#groupby for column purpose
purposeGroupBy = loandata.groupby(['purpose']).size()

#plotting bar graph for catplot
catplot.plot.bar()
plt.show()

#plotting bar graph for purpose
purposeGroupBy.plot.bar()
plt.show()

#change color, width
catplot.plot.bar(color='green',width=0.1)
plt.show()

#scatter plt
#income and debt

yaxis = loandata['annualincome']
xaxis = loandata['dti']

plt.scatter(xaxis,yaxis,color='#FFA500')
plt.show()


#writing to csv
loandata.to_csv('loan_cleaned.csv',index=True)
   




























