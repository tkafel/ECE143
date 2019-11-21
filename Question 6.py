#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


# Read in the .csv file
df = pd.read_csv('Preprocess_Completed.csv')
df.set_index(['Department'], inplace=True)


# In[3]:


# Split the dataframe into the different departments
ece = df.loc['ECE']
cse = df.loc['CSE']
mae = df.loc['MAE']                                                                                            
beng = df.loc['BENG']

ece.reset_index(inplace=True)
cse.reset_index(inplace=True)                                                                                        
mae.reset_index(inplace=True)                                                                                        
beng.reset_index(inplace=True)


# In[4]:


# Get the sum of the 'Rcmnd Instr' column for each department
ece_total = ece['Rcmnd Instr'].sum()
cse_total = cse['Rcmnd Instr'].sum()                                                                                 
mae_total = mae['Rcmnd Instr'].sum()                                                                                 
beng_total = beng['Rcmnd Instr'].sum() 

# Find the average by dividing by the number of rows
ece_avg = ece_total / len(ece)
cse_avg = cse_total / len(cse)                                                                                       
mae_avg = mae_total / len(mae)                                                                                       
beng_avg = beng_total / len(beng)


# In[5]:


# Create a bar chart with each average
objects = ('ECE', 'CSE', 'MAE', 'BENG')
y_pos = np.arange(len(objects))
# Subtract each average from 100 to get not recommended average
avgs = [100 - ece_avg, 100 - cse_avg, 100 - mae_avg, 100 - beng_avg]

plt.bar(y_pos, avgs, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Percentages')
plt.title('Average Percentage of Not Recommending Instructor')
plt.ylim(0,20)

plt.show()

