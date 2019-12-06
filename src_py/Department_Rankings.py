
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Read in the .csv file
df = pd.read_csv('Preprocess_Completed.csv')
df.set_index(["Department"], inplace=True)

# Split the dataframes based on deartment
ece = df.loc["ECE"]
cse = df.loc["CSE"]
mae = df.loc["MAE"]
beng = df.loc["BENG"]

ece.reset_index(inplace=True)
cse.reset_index(inplace=True)
mae.reset_index(inplace=True)
beng.reset_index(inplace=True)

# Get the sum of the 'Study Hrs/wk' column for each department
ece_study = ece['Study Hrs/wk'].sum()
cse_study = cse['Study Hrs/wk'].sum()                                                                                 
mae_study = mae['Study Hrs/wk'].sum()                                                                                 
beng_study = beng['Study Hrs/wk'].sum() 

# Get the sum of the 'Avg Grade Received' column for each department
ece_grade = ece['Avg Grade Received'].sum()
cse_grade = cse['Avg Grade Received'].sum()                                                                                 
mae_grade = mae['Avg Grade Received'].sum()                                                                                 
beng_grade = beng['Avg Grade Received'].sum()

# Get the sum of the 'Rcmnd Class' column for each department
ece_class = ece['Rcmnd Class'].sum()
cse_class = cse['Rcmnd Class'].sum()                                                                                 
mae_class = mae['Rcmnd Class'].sum()                                                                                 
beng_class = beng['Rcmnd Class'].sum()

# Get the sum of the 'Rcmnd Instr' column for each department
ece_instr = ece['Rcmnd Instr'].sum()
cse_instr = cse['Rcmnd Instr'].sum()                                                                                 
mae_instr = mae['Rcmnd Instr'].sum()                                                                                 
beng_instr = beng['Rcmnd Instr'].sum()

# Find the averages for each department by dividing by the number of rows
ece_study_avg = ece_study / len(ece)
ece_grade_avg = ece_grade / len(ece)
ece_class_avg = ece_class / len(ece)
ece_instr_avg = ece_instr / len(ece)

cse_study_avg = cse_study / len(cse)
cse_grade_avg = cse_grade / len(cse)
cse_class_avg = cse_class / len(cse)
cse_instr_avg = cse_instr / len(cse)

mae_study_avg = mae_study / len(mae)
mae_grade_avg = mae_grade / len(mae)
mae_class_avg = mae_class / len(mae)
mae_instr_avg = mae_instr / len(mae)

beng_study_avg = beng_study / len(beng)
beng_grade_avg = beng_grade / len(beng)
beng_class_avg = beng_class / len(beng)
beng_instr_avg = beng_instr / len(beng)

# Sum up all of the averages
ece_total = ece_grade_avg + ece_class_avg + ece_instr_avg - ece_study_avg 
cse_total = cse_grade_avg + cse_class_avg + cse_instr_avg - cse_study_avg
mae_total = mae_grade_avg + mae_class_avg + mae_instr_avg - mae_study_avg
beng_total = beng_grade_avg + beng_class_avg + beng_instr_avg - beng_study_avg

# Create a bar chart with each total
objects = ('ECE', 'CSE', 'MAE', 'BENG')
y_pos = np.arange(len(objects))
totals = [ece_total, cse_total, mae_total, beng_total]

bar_list = plt.bar(y_pos, totals, align='center', alpha=0.5)
bar_list[0].set_color('g')
bar_list[1].set_color('b')
bar_list[2].set_color('r')
bar_list[3].set_color('y')
plt.xticks(y_pos, objects)
plt.ylabel('Department Score')
plt.xlabel('Departments')
plt.title('Best Ranked Departments')
plt.ylim(100,175)

plt.show()
