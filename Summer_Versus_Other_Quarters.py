# -*- coding: utf-8 -*-
"""
Created on 

@author: Tony
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('Preprocess_Completed.csv')
mae = data.loc[data['Department'] == 'MAE']
ece = data.loc[data['Department'] == 'ECE']
cse = data.loc[data['Department'] == 'CSE']
bio = data.loc[data['Department'] == 'BENG']

def find_common_course_and_gpa(data, dep):
   '''
   First group by course number and find courses that is available in all quarters.
   Take the average of grade and plot the result. x axis with course number and ylabel with all grades in each quarters
   
   :param:
      data(pd.DataFrame): whole dataset
      dep(str): department, use to plot
   :return:
      None
   '''
   assert isinstance(data, pd.DataFrame)
   assert isinstance(dep, str)
   unique_course = data.groupby('Course Number')  # groupby each course
   data_dict = {}
   for course_num, table1 in unique_course:
       fall = table1.loc[data['Term'].str.startswith('FA')]  # find all current course open in fall
       winter = table1.loc[data['Term'].str.startswith('WI')]  # find all current course open in winter
       spring = table1.loc[data['Term'].str.startswith('SP')]  # find all current course open in spring
       summer = table1.loc[data['Term'].str.startswith('S1')]  # find all current course open in summer
       if fall.empty or winter.empty or spring.empty or summer.empty:  # if not open in all four quarter
           continue
       data_dict[course_num] = [fall['Avg Grade Received'].mean(), winter['Avg Grade Received'].mean(), spring['Avg Grade Received'].mean(), summer['Avg Grade Received'].mean()]
   compare_gpa = pd.DataFrame(data_dict, index=['FA', 'WI', 'SP', 'S1']).transpose()
   ax = compare_gpa.plot.bar(rot = 0, figsize=(10,5), title=dep + ' course gpa over each quarter')
   ax.legend(loc='upper right', bbox_to_anchor=(1, 1))
   ax.title.set_size(32)
   ax.set_xlabel('Course Number', fontsize=24)
   ax.set_ylabel('Grade Received', fontsize=24)
   
if __name__ == "__main__":
   cur_dep = "ECE"
   if cur_dep == "MAE":
      find_common_course_and_gpa(mae, cur_dep)
   elif cur_dep == "ECE":
      find_common_course_and_gpa(ece, cur_dep)
   elif cur_dep == "CSE":
      find_common_course_and_gpa(cse, cur_dep)
   else:
      find_common_course_and_gpa(bio, cur_dep)
