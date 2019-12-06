import pandas as pd
import numpy as np

##########################################################################################################
# Script Name: Best_Ranked_Courses_Overall
# Script Description: This script is targeted to answer the first question in the
#					  project proposal: what are the best ranked courses overall in each department? 
#                     After the proprocessing of the data we separate the date in 4 dataframes based on 4 
#                     different departments. A new column called "student ratio" is introduced for each 
#                     dataframe. Each dataframe is then grouped by based on the course number and
#					  the one row from each group with the highest ratio is extracted.
#					  This number indicates the one unique course with the most evaluations.
#					  As a group we decided this would be the best way to get a fair answer 
#					  for our question. Next, we introduce a new column for the ranking criteria.
#					  In this column convert the grade recieved to a percentage value based on the
#					  4.0 scale and sum it up with the "recommended class" and "recommended instructor"
#					  column together. The course are then ranked based on this value and the top result
#					  from each dataframe in our opinion would indicate the best course ranked based on the 
#					  3 criteria and the available feedback given by the students.
###########################################################################################################

##########################################################################################################
########################## USE THE PREPROCESSED DATA TO SEPERATE OUT DEPARTMENTS #########################
##########################################################################################################

#import the dataframe after the preprocessing script
combined_df = pd.read_csv("Preprocess_Completed.csv")
combined_df.set_index(["Department"], inplace=True)

total_Enolled = combined_df["Enroll"].sum()
total_eval = combined_df["Evals Made"].sum()
percent_evaluated = (total_eval/total_Enolled) * 100

#seperate the dataframes by department
ece_df = combined_df.loc["ECE"]
mae_df = combined_df.loc["MAE"]
beng_df = combined_df.loc["BENG"]
cse_df = combined_df.loc["CSE"]

#would be interesting to know - get the length of each df
ece_df_length = len(ece_df)
cse_df_length = len(cse_df)
beng_df_length = len(beng_df)
mae_df_length = len(mae_df)

#reset the index to all the dataframes
ece_df.reset_index(inplace=True)
cse_df.reset_index(inplace=True)
beng_df.reset_index(inplace=True)
mae_df.reset_index(inplace=True)



##########################################################################################################
###################################### Main Analysis for the data ########################################
##########################################################################################################

#add a new column to the dataframe indicating the ratio of students who evaluated the course percentage
ece_df["student ratio"] = (ece_df["Evals Made"]/ece_df["Enroll"]) *100
cse_df["student ratio"] = (cse_df["Evals Made"]/cse_df["Enroll"]) *100
mae_df["student ratio"] = (mae_df["Evals Made"]/mae_df["Enroll"]) *100
beng_df["student ratio"] = (beng_df["Evals Made"]/beng_df["Enroll"]) *100


#group all the epartments by the course so we have a group of all the unique courses in each department
ece_course_group = ece_df.groupby(["Course Number"])
mae_course_group = mae_df.groupby(["Course Number"])
cse_course_group = cse_df.groupby(["Course Number"])
beng_course_group = beng_df.groupby(["Course Number"])

#useful to record the number of unique courses available in the capes dataset for each department
number_of_unique_ece_courses = len(ece_course_group)
number_of_unique_cse_courses = len(cse_course_group)
number_of_unique_mae_courses = len(mae_course_group)
number_of_unique_beng_courses = len(beng_course_group)

#create 4 new dataframes to store info we are about to extract from the groups with the same columns as the original dfs
ece_courses_with_highest_evaluations_df = pd.DataFrame(columns = ece_df.columns)
cse_courses_with_highest_evaluations_df = pd.DataFrame(columns = cse_df.columns)
mae_courses_with_highest_evaluations_df = pd.DataFrame(columns = mae_df.columns)
beng_courses_with_highest_evaluations_df = pd.DataFrame(columns = beng_df.columns)


#for each group get the one unique course with the highest evaluation ratio
for ratio_val, unique_course in ece_course_group:
    highest_valued_ratio = unique_course.nlargest(1, "student ratio")
    ece_courses_with_highest_evaluations_df = ece_courses_with_highest_evaluations_df.append(highest_valued_ratio)

for ratio_val, unique_course in cse_course_group:
    highest_valued_ratio = unique_course.nlargest(1, "student ratio")
    cse_courses_with_highest_evaluations_df = cse_courses_with_highest_evaluations_df.append(highest_valued_ratio)

for ratio_val, unique_course in mae_course_group:
    highest_valued_ratio = unique_course.nlargest(1, "student ratio")
    mae_courses_with_highest_evaluations_df = mae_courses_with_highest_evaluations_df.append(highest_valued_ratio)

for ratio_val, unique_course in beng_course_group:
    highest_valued_ratio = unique_course.nlargest(1, "student ratio")
    beng_courses_with_highest_evaluations_df = beng_courses_with_highest_evaluations_df.append(highest_valued_ratio)

#get the length of the new constructed dataframes for a sanity check
ece_course_group_length = len(ece_courses_with_highest_evaluations_df)
cse_course_group_length = len(cse_courses_with_highest_evaluations_df)
mae_course_group_length = len(mae_courses_with_highest_evaluations_df)
beng_course_group_length = len(beng_courses_with_highest_evaluations_df)

#ALL PRINTS BELOW RETURNED TRUE, SANITY CHECK PASSED
# print(ece_course_group_length == number_of_unique_ece_courses)
# print(cse_course_group_length == number_of_unique_cse_courses)
# print(mae_course_group_length ==number_of_unique_mae_courses)
# print(beng_course_group_length == number_of_unique_beng_courses)

#for all the new unique course dataframes contructed convert grade received to a percentage and take the average of the 3 columns we chose to define "best" in quality
for i in ece_courses_with_highest_evaluations_df:
    grade_percentage = (ece_courses_with_highest_evaluations_df["Avg Grade Received"]/4.00) *100
    final_sum = ece_courses_with_highest_evaluations_df["Rcmnd Class"] + ece_courses_with_highest_evaluations_df["Rcmnd Instr"] + grade_percentage
    ece_courses_with_highest_evaluations_df["final sum"] = final_sum

for i in cse_courses_with_highest_evaluations_df:
    grade_percentage = (cse_courses_with_highest_evaluations_df["Avg Grade Received"]/4.00) *100
    final_sum = cse_courses_with_highest_evaluations_df["Rcmnd Class"] + cse_courses_with_highest_evaluations_df["Rcmnd Instr"] + grade_percentage
    cse_courses_with_highest_evaluations_df["final sum"] = final_sum

for i in mae_courses_with_highest_evaluations_df:
    grade_percentage = (mae_courses_with_highest_evaluations_df["Avg Grade Received"]/4.00) *100
    final_sum = mae_courses_with_highest_evaluations_df["Rcmnd Class"] + mae_courses_with_highest_evaluations_df["Rcmnd Instr"] + grade_percentage
    mae_courses_with_highest_evaluations_df["final sum"] = final_sum

for i in beng_courses_with_highest_evaluations_df:
    grade_percentage = (beng_courses_with_highest_evaluations_df["Avg Grade Received"]/4.00) *100
    final_sum = beng_courses_with_highest_evaluations_df["Rcmnd Class"] + beng_courses_with_highest_evaluations_df["Rcmnd Instr"] + grade_percentage
    beng_courses_with_highest_evaluations_df["final sum"] = final_sum


#sort the values in each unique dataframe based on the final sum column and extract the top courses in each department
ece_courses_with_highest_evaluations_df.sort_values("final sum", axis=0, ascending=False, inplace=True)
cse_courses_with_highest_evaluations_df.sort_values("final sum", axis=0, ascending=False, inplace=True)
mae_courses_with_highest_evaluations_df.sort_values("final sum", axis=0, ascending=False, inplace=True)
beng_courses_with_highest_evaluations_df.sort_values("final sum", axis=0, ascending=False, inplace=True)

#visualization and plotting
#ece
fig = plt.figure(figsize=(60, 30))
ece_x = fig.add_subplot(111)
ece_x = ece_courses_with_highest_evaluations_df["Course Number"]
ece_y = ece_courses_with_highest_evaluations_df["final sum"]
colors = (0.25,0.5,1)
plt.scatter(ece_x, ece_y, s=400, c=colors, marker = "v", alpha=1)
plt.autoscale(enable=True, axis='x', tight=False)
plt.title('ECE Course Ranking', fontsize=80)
plt.xlabel('ECE Courses', fontsize=40)
plt.ylabel('Quality RANK', fontsize=40)
plt.savefig('Question1_ECE.jpg')
plt.show()

#cse
fig = plt.figure(figsize=(60, 30))
cse_x = fig.add_subplot(111)
cse_x = cse_courses_with_highest_evaluations_df["Course Number"]
cse_y = cse_courses_with_highest_evaluations_df["final sum"]
colors = (1,0,0)
plt.scatter(cse_x, cse_y, s=400, marker = "v", c=colors, alpha=1)
plt.autoscale(enable=True, axis='x', tight=False)
plt.title('CSE Course Ranking', fontsize=80)
plt.xlabel('CSE Courses', fontsize=40)
plt.ylabel('Quality RANK', fontsize=40)
plt.savefig('Question1_CSE.jpg')
plt.show()

#mae
fig = plt.figure(figsize=(60, 30))
mae_x = fig.add_subplot(111)
mae_x = mae_courses_with_highest_evaluations_df["Course Number"]
mae_y = mae_courses_with_highest_evaluations_df["final sum"]
colors = (0.8,0.3,1)
plt.scatter(mae_x, mae_y, s=400, marker="v" ,c=colors, alpha=1)
plt.autoscale(enable=True, axis='x', tight=False)
plt.title('MAE Course Ranking', fontsize=80)
plt.xlabel('MAE Courses', fontsize=40)
plt.ylabel('Quality RANK', fontsize=40)
plt.savefig('Question1_MAE.jpg')
plt.show()

#beng
fig = plt.figure(figsize=(60, 30))
beng_x = fig.add_subplot(111)
beng_x = beng_courses_with_highest_evaluations_df["Course Number"]
beng_y = beng_courses_with_highest_evaluations_df["final sum"]
colors = (0,0.9,0.3)
plt.scatter(beng_x, beng_y, s=400, c=colors, marker="v", alpha=1)
plt.autoscale(enable=True, axis='x', tight=False)
plt.title('BENG Course Ranking', fontsize=80)
plt.xlabel('BENG Courses', fontsize=40)
plt.ylabel('Quality RANK', fontsize=40)
plt.savefig('Question1_BENG.jpg')
plt.show()

