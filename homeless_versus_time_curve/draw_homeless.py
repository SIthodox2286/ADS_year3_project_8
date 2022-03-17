# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


'''
1.Load the data
'''
data=pd.read_excel('data.xlsx')


'''
2.Draw the first 3 regions
'''
plt.figure(dpi=600)

#(1) Get the regions' names
region_names=data.iloc[0:3,0]

#(2) Start a loop for plotting the data from Month: 1-3, 4-6, 7-9
xlabel_names=['1-3','4-6','7-9'] #Because the xlabel should be the month ranges
colors=['y','b','k']#Set the colors for 3 regions
legends=[];

for i in range(0,3):
    region_now=region_names[i]
    
    #<1> Plot the region's data of 'Total owed a prevention or relief duty'
    y=data.iloc[i,range(1,6,2)]#Get the data of 'Total owed a prevention or relief duty'
    x = range(0,len(xlabel_names),1)
    plt.plot(x, y, color=colors[i],marker="o",markersize=6)
    
    #<2> Plot the region's data of 'Homeless - Relief duty owed'
    y=data.iloc[i,range(2,7,2)]#Get the data of 'Homeless - Relief duty owed'
    x = range(0,len(xlabel_names),1)
    plt.plot(x, y, color=colors[i],marker="x",markersize=6)
    
    # Generate the legends for the lines
    k=len(legends)
    legends[k:k+2]=[region_now+': Total owed a prevention or relief duty',region_now+': Homeless - Relief duty owed']
    
plt.ylabel('Number')
plt.xlabel('Month')
plt.legend(legends,bbox_to_anchor=(2.1,1))
plt.xticks(x, xlabel_names, rotation=45)
plt.show()



'''
3.Draw the rest 6 regions
'''
plt.figure(dpi=600)

#(1) Get the regions' names
region_names=data.iloc[3:9,0]

#(2) Start a loop for plotting the data from Month: 1-3, 4-6, 7-9
xlabel_names=['1-3','4-6','7-9'] #Because the xlabel should be the month ranges
colors=['y','b','k','r','g','c']#Set the colors for 3 regions
legends=[];

for i in range(3,9):
    region_now=region_names[i]
    
    #<1> Plot the region's data of 'Total owed a prevention or relief duty'
    y=data.iloc[i,range(1,6,2)]#Get the data of 'Total owed a prevention or relief duty'
    x = range(0,len(xlabel_names),1)
    plt.plot(x, y, color=colors[i-3],marker="o",markersize=6)
    
    #<2> Plot the region's data of 'Homeless - Relief duty owed'
    y=data.iloc[i,range(2,7,2)]#Get the data of 'Homeless - Relief duty owed'
    x = range(0,len(xlabel_names),1)
    plt.plot(x, y, color=colors[i-3],marker="x",markersize=6)
    
    # Generate the legends for the lines
    k=len(legends)
    legends[k:k+2]=[region_now+': Total owed a prevention or relief duty',region_now+': Homeless - Relief duty owed']
    
plt.ylabel('Number')
plt.xlabel('Month')
plt.legend(legends,bbox_to_anchor=(2.1,1))
plt.xticks(x, xlabel_names, rotation=45)
plt.show()