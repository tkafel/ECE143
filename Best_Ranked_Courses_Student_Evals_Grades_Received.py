import pandas as pd 
import numpy as np 

##########################################################################################################
# Script Name: Best_Ranked_Courses_Student_Evals_Grades_Received
# Script Description: This script is targeted to answer the second question in the
#					  project proposal: what are the best ranked courses in each department based on 
#                     student evalutions and grades received? After the proprocessing of the data we 
#					  separate the date in 4 dataframes based on 4 different departments.
#					  A new column called "student ratio" is introduced for each dataframe.
#					  Each dataframe is then grouped by based on the course number and
#					  the one row from each group wiht the highest ratio is extracted.
#					  This number indicates the one unique course with the most evaluations
#					  As a group we decided this would be the best way to get a fair answer 
#					  for our question. Next we introduce a new column for the ranking criteria
#					  In this column convert the grade recieved to a percentage value based on the
#					  4.0 scale and sum it up with the "recommended class" and "recommended instructor"
#					  column together. The courses are then ranked based on this value and the top result
#					  from each dataframe in our opinion would indiacte the best course ranked based on the 
#					  3 criteria and the available feedback given by the students.
###########################################################################################################

##########################################################################################################
########################## USE THE PROPROCESSED DATA TO SEPERATE OUT DEPARTMENTS #########################
##########################################################################################################
#import the combined dataframe
combined_df = pd.read_csv("Preprocess_Completed.csv")
combined_df.set_index(["Department"], inplace=True)

#seperate the dataframes based on the departments
ece_df = combined_df.loc["ECE"]
cse_df = combined_df.loc["CSE"]
mae_df = combined_df.loc["MAE"]
beng_df = combined_df.loc["BENG"]

#reset the index for all the combined dataframes
ece_df.reset_index(inplace=True)
cse_df.reset_index(inplace=True)
mae_df.reset_index(inplace=True)
beng_df.reset_index(inplace=True)

#create new column to hold all the grades expected to grades received ratio for eachd department
ece_df["Final Grade Ratio"] = ece_df["Avg Grade Received"]/ece_df["Avg Grade Expected"]
cse_df["Final Grade Ratio"] = cse_df["Avg Grade Received"]/cse_df["Avg Grade Expected"]
mae_df["Final Grade Ratio"] = mae_df["Avg Grade Received"]/mae_df["Avg Grade Expected"]
beng_df["Final Grade Ratio"] = beng_df["Avg Grade Received"]/beng_df["Avg Grade Expected"]

#cerate groups based on the unique course numbers
ece_course_group = ece_df.groupby(["Course Number"])
cse_course_group = cse_df.groupby(["Course Number"])
mae_course_group = mae_df.groupby(["Course Number"])
beng_course_group = beng_df.groupby(["Course Number"])

#create new dataframes with same columns to store the averaged out results for each group
averged_out_ece_unique_course_df = pd.DataFrame(columns =["Course", "Total Enrolled", "Average Hours Studied" , "Avrg Grade Expected", "Avrg Grade Received"])
averged_out_cse_unique_course_df = pd.DataFrame(columns =["Course", "Total Enrolled", "Average Hours Studied" , "Avrg Grade Expected", "Avrg Grade Received"])
averged_out_mae_unique_course_df = pd.DataFrame(columns =["Course", "Total Enrolled", "Average Hours Studied" , "Avrg Grade Expected", "Avrg Grade Received"])
averged_out_beng_unique_course_df = pd.DataFrame(columns =["Course", "Total Enrolled", "Average Hours Studied" , "Avrg Grade Expected", "Avrg Grade Received"])

#create dictionaries and lists to hold the results for avergae values for each department
#for ece
average_enrolled_ece_dict = {}
average_grade_expected_ece_dict = {}
average_grade_receieved_ece_dict = {}
average_hours_studied_ece_dict = {}
ece_course_name = []
ece_total_enrolled = []

#for cse
average_enrolled_cse_dict = {}
average_grade_expected_cse_dict = {}
average_grade_receieved_cse_dict = {}
average_hours_studied_cse_dict = {}
cse_course_name = []
cse_total_enrolled = []

#for mae
average_enrolled_mae_dict = {}
average_grade_expected_mae_dict = {}
average_grade_receieved_mae_dict = {}
average_hours_studied_mae_dict = {}
mae_course_name = []
mae_total_enrolled = []

#for beng
average_enrolled_beng_dict = {}
average_grade_expected_beng_dict = {}
average_grade_receieved_beng_dict = {}
average_hours_studied_beng_dict = {}
beng_course_name = []
beng_total_enrolled = []


##########################################################################################################
###################################### Main Analysis for the data ########################################
##########################################################################################################

#get the averge for each column in each group - This will give us an averaged out column for hours studied,
# grades receieved and expected and total entrolled students for each unique course in the dataset
#for ece
for course, data in ece_course_group:
    total_enrolled_val = data["Enroll"].sum()
    average_grade_per_course_receieved = data["Avg Grade Received"].mean()
    average_grade_per_course_expected = data["Avg Grade Expected"].mean()
    average_hours_studied = data["Study Hrs/wk"].mean()
    average_enrolled_ece_dict[course] = total_enrolled_val
    average_grade_receieved_ece_dict[course] = average_grade_per_course_receieved
    average_grade_expected_ece_dict[course] = average_grade_per_course_expected
    average_hours_studied_ece_dict[course] = average_hours_studied 

ece_course_name = average_enrolled_ece_dict.keys()
ece_total_enrolled = average_enrolled_ece_dict.values()
ece_average_grade_expected = average_grade_expected_ece_dict.values()
ece_average_grade_receieved = average_grade_receieved_ece_dict.values()
ece_average_hours_studied = average_hours_studied_ece_dict.values()

averged_out_ece_unique_course_df["Course"] = ece_course_name
averged_out_ece_unique_course_df["Total Enrolled"] = ece_total_enrolled
averged_out_ece_unique_course_df["Avrg Grade Expected"] = ece_average_grade_expected
averged_out_ece_unique_course_df["Avrg Grade Received"] = ece_average_grade_receieved
averged_out_ece_unique_course_df["Average Hours Studied"] = ece_average_hours_studied

#for cse
for course, data in cse_course_group:
    total_enrolled_val = data["Enroll"].sum()
    average_grade_per_course_receieved = data["Avg Grade Received"].mean()
    average_grade_per_course_expected = data["Avg Grade Expected"].mean()
    average_hours_studied = data["Study Hrs/wk"].mean()
    average_enrolled_cse_dict[course] = total_enrolled_val
    average_grade_receieved_cse_dict[course] = average_grade_per_course_receieved
    average_grade_expected_cse_dict[course] = average_grade_per_course_expected
    average_hours_studied_cse_dict[course] = average_hours_studied 

cse_course_name = average_enrolled_cse_dict.keys()
cse_total_enrolled = average_enrolled_cse_dict.values()
cse_average_grade_expected = average_grade_expected_cse_dict.values()
cse_average_grade_receieved = average_grade_receieved_cse_dict.values()
cse_average_hours_studied = average_hours_studied_cse_dict.values()

averged_out_cse_unique_course_df["Course"] = cse_course_name
averged_out_cse_unique_course_df["Total Enrolled"] = cse_total_enrolled
averged_out_cse_unique_course_df["Avrg Grade Expected"] = cse_average_grade_expected
averged_out_cse_unique_course_df["Avrg Grade Received"] = cse_average_grade_receieved
averged_out_cse_unique_course_df["Average Hours Studied"] = cse_average_hours_studied

#for mae
for course, data in mae_course_group:
    total_enrolled_val = data["Enroll"].sum()
    average_grade_per_course_receieved = data["Avg Grade Received"].mean()
    average_grade_per_course_expected = data["Avg Grade Expected"].mean()
    average_hours_studied = data["Study Hrs/wk"].mean()
    average_enrolled_mae_dict[course] = total_enrolled_val
    average_grade_receieved_mae_dict[course] = average_grade_per_course_receieved
    average_grade_expected_mae_dict[course] = average_grade_per_course_expected
    average_hours_studied_mae_dict[course] = average_hours_studied 

mae_course_name = average_enrolled_mae_dict.keys()
mae_total_enrolled = average_enrolled_mae_dict.values()
mae_average_grade_expected = average_grade_expected_mae_dict.values()
mae_average_grade_receieved = average_grade_receieved_mae_dict.values()
mae_average_hours_studied = average_hours_studied_mae_dict.values()

averged_out_mae_unique_course_df["Course"] = mae_course_name
averged_out_mae_unique_course_df["Total Enrolled"] = mae_total_enrolled
averged_out_mae_unique_course_df["Avrg Grade Expected"] = mae_average_grade_expected
averged_out_mae_unique_course_df["Avrg Grade Received"] = mae_average_grade_receieved
averged_out_mae_unique_course_df["Average Hours Studied"] = mae_average_hours_studied

#for beng
for course, data in beng_course_group:
    total_enrolled_val = data["Enroll"].sum()
    average_grade_per_course_receieved = data["Avg Grade Received"].mean()
    average_grade_per_course_expected = data["Avg Grade Expected"].mean()
    average_hours_studied = data["Study Hrs/wk"].mean()
    average_enrolled_beng_dict[course] = total_enrolled_val
    average_grade_receieved_beng_dict[course] = average_grade_per_course_receieved
    average_grade_expected_beng_dict[course] = average_grade_per_course_expected
    average_hours_studied_beng_dict[course] = average_hours_studied 

beng_course_name = average_enrolled_beng_dict.keys()
beng_total_enrolled = average_enrolled_beng_dict.values()
beng_average_grade_expected = average_grade_expected_beng_dict.values()
beng_average_grade_receieved = average_grade_receieved_beng_dict.values()
beng_average_hours_studied = average_hours_studied_beng_dict.values()

averged_out_beng_unique_course_df["Course"] = beng_course_name
averged_out_beng_unique_course_df["Total Enrolled"] = beng_total_enrolled
averged_out_beng_unique_course_df["Avrg Grade Expected"] = beng_average_grade_expected
averged_out_beng_unique_course_df["Avrg Grade Received"] = beng_average_grade_receieved
averged_out_beng_unique_course_df["Average Hours Studied"] = beng_average_hours_studied


#divide the averged out grades received by grades expected; this will give us a good frame of reference to see consistency of the grades
averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"] = averged_out_ece_unique_course_df["Avrg Grade Received"]/averged_out_ece_unique_course_df["Avrg Grade Expected"] 
averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] = averged_out_cse_unique_course_df["Avrg Grade Received"]/averged_out_cse_unique_course_df["Avrg Grade Expected"] 
averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] = averged_out_mae_unique_course_df["Avrg Grade Received"]/averged_out_mae_unique_course_df["Avrg Grade Expected"] 
averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] = averged_out_beng_unique_course_df["Avrg Grade Received"]/averged_out_beng_unique_course_df["Avrg Grade Expected"] 

#find mean and vairance for the ratio column to extract the most consistent grades overall
#ece
ece_mean_grade_ratio_val = averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"].mean()
ece_var_grade_ratio_val = averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"].std()
ece_consistancy_upper_range = ece_mean_grade_ratio_val + ece_var_grade_ratio_val
ece_consistancy_lower_range = ece_mean_grade_ratio_val - ece_var_grade_ratio_val
consistency_range_mask_ece = (averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"] < ece_consistancy_upper_range) & (averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"] > ece_consistancy_lower_range )
lower_than_consistancy_mask_ece = averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"] < ece_consistancy_lower_range
higher_than_consistancy_mask_ece = averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"] > ece_consistancy_upper_range
most_consistant_ece_course_df = averged_out_ece_unique_course_df[consistency_range_mask_ece]
least_consistant_low_grade_df = averged_out_ece_unique_course_df[lower_than_consistancy_mask_ece]
least_consistant_high_grade_df = averged_out_ece_unique_course_df[higher_than_consistancy_mask_ece]
ece_course_percentage_goal_consistancy_percentage = (len(most_consistant_ece_course_df) / len(averged_out_ece_unique_course_df)) *100
ece_course_percentage_low_consistancy_percentage = (len(least_consistant_low_grade_df) / len(averged_out_ece_unique_course_df)) *100
ece_course_percentage_high_consistancy_percentage = (len(least_consistant_high_grade_df) / len(averged_out_ece_unique_course_df)) *100

#cse
cse_mean_grade_ratio_val = averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"].mean()
cse_var_grade_ratio_val = averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"].std()
cse_consistancy_upper_range = cse_mean_grade_ratio_val + cse_var_grade_ratio_val
cse_consistancy_lower_range = cse_mean_grade_ratio_val - cse_var_grade_ratio_val
consistency_range_mask_cse = (averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] < cse_consistancy_upper_range) & (averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] > cse_consistancy_lower_range )
lower_than_consistancy_mask_cse = averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] < cse_consistancy_lower_range
higher_than_consistancy_mask_cse = averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] > cse_consistancy_upper_range
most_consistant_ece_course_df_cse = averged_out_cse_unique_course_df[consistency_range_mask_cse]
least_consistant_low_grade_df_cse = averged_out_cse_unique_course_df[lower_than_consistancy_mask_cse]
least_consistant_high_grade_df_cse = averged_out_cse_unique_course_df[higher_than_consistancy_mask_cse]
cse_course_percentage_goal_consistancy_percentage = (len(most_consistant_ece_course_df_cse) / len(averged_out_cse_unique_course_df)) *100
cse_course_percentage_low_consistancy_percentage = (len(least_consistant_low_grade_df_cse) / len(averged_out_cse_unique_course_df)) *100
cse_course_percentage_high_consistancy_percentage = (len(least_consistant_high_grade_df_cse) / len(averged_out_cse_unique_course_df)) *100

# mae
mae_mean_grade_ratio_val = averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"].mean()
mae_var_grade_ratio_val = averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"].std()
mae_consistancy_upper_range = mae_mean_grade_ratio_val + mae_var_grade_ratio_val
mae_consistancy_lower_range = mae_mean_grade_ratio_val - mae_var_grade_ratio_val
consistency_range_mask_mae = (averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] < mae_consistancy_upper_range) & (averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] > mae_consistancy_lower_range )
lower_than_consistancy_mask_mae = averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] < mae_consistancy_lower_range
higher_than_consistancy_mask_mae = averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] > mae_consistancy_upper_range
most_consistant_ece_course_df_mae = averged_out_mae_unique_course_df[consistency_range_mask_mae]
least_consistant_low_grade_df_mae = averged_out_mae_unique_course_df[lower_than_consistancy_mask_mae]
least_consistant_high_grade_df_mae = averged_out_mae_unique_course_df[higher_than_consistancy_mask_mae]
mae_course_percentage_goal_consistancy_percentage = (len(most_consistant_ece_course_df_mae) / len(averged_out_mae_unique_course_df)) *100
mae_course_percentage_low_consistancy_percentage = (len(least_consistant_low_grade_df_mae) / len(averged_out_mae_unique_course_df)) *100
mae_course_percentage_high_consistancy_percentage = (len(least_consistant_high_grade_df_mae) / len(averged_out_mae_unique_course_df)) *100

#beng
beng_mean_grade_ratio_val = averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"].mean()
beng_var_grade_ratio_val = averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"].std()
beng_consistancy_upper_range = beng_mean_grade_ratio_val + beng_var_grade_ratio_val
beng_consistancy_lower_range = beng_mean_grade_ratio_val - beng_var_grade_ratio_val
consistency_range_mask_beng = (averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] < beng_consistancy_upper_range) & (averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] > beng_consistancy_lower_range )
lower_than_consistancy_mask_beng = averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] < beng_consistancy_lower_range
higher_than_consistancy_mask_beng = averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] > beng_consistancy_upper_range
most_consistant_ece_course_df_beng = averged_out_beng_unique_course_df[consistency_range_mask_beng]
least_consistant_low_grade_df_beng = averged_out_beng_unique_course_df[lower_than_consistancy_mask_beng]
least_consistant_high_grade_df_beng = averged_out_beng_unique_course_df[higher_than_consistancy_mask_beng]
beng_course_percentage_goal_consistancy_percentage = (len(most_consistant_ece_course_df_beng) / len(averged_out_beng_unique_course_df)) *100
beng_course_percentage_low_consistancy_percentage = (len(least_consistant_low_grade_df_beng) / len(averged_out_beng_unique_course_df)) *100
beng_course_percentage_high_consistancy_percentage = (len(least_consistant_high_grade_df_beng) / len(averged_out_beng_unique_course_df)) *100

#ploting and visualization
#ece
ece_pie_plot_sizes = [ece_course_percentage_goal_consistancy_percentage, ece_course_percentage_low_consistancy_percentage,ece_course_percentage_high_consistancy_percentage]
ece_pie_plot_labels = ['Whitin the consistency range', 'Below the consistency range', 'Over the consistency range']
fig1, ax1 = plt.subplots()
ax1.pie(ece_pie_plot_sizes, labels=ece_pie_plot_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Electrical Engineering Course Consistency', fontsize=20)
plt.savefig('Question2_ECE.jpg')
plt.show()

#cse
cse_pie_plot_sizes = [cse_course_percentage_goal_consistancy_percentage, cse_course_percentage_low_consistancy_percentage,cse_course_percentage_high_consistancy_percentage]
cse_pie_plot_labels = ['Whitin the consistency range', 'Below the consistency range', 'Over the consistency range']
fig1, ax1 = plt.subplots()
ax1.pie(cse_pie_plot_sizes, labels=cse_pie_plot_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Computer Science and Engineering Course Consistency', fontsize=20)
plt.savefig('Question2_CSE.jpg')
plt.show()

#mae
mae_pie_plot_sizes = [mae_course_percentage_goal_consistancy_percentage, mae_course_percentage_low_consistancy_percentage,mae_course_percentage_high_consistancy_percentage]
mae_pie_plot_labels = ['Whitin the consistency range', 'Below the consistency range', 'Over the consistency range']
fig1, ax1 = plt.subplots()
ax1.pie(mae_pie_plot_sizes, labels=mae_pie_plot_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Mechanical Engineering Course Consistency', fontsize=20)
plt.savefig('Question2_MAE.jpg')
plt.show()
#beng
beng_pie_plot_sizes = [beng_course_percentage_goal_consistancy_percentage, beng_course_percentage_low_consistancy_percentage,beng_course_percentage_high_consistancy_percentage]
beng_pie_plot_labels = ['Whitin the consistency range', 'Below the consistency range', 'Over the consistency range']
fig1, ax1 = plt.subplots()
ax1.pie(beng_pie_plot_sizes, labels=beng_pie_plot_labels, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Bioengineering Course Consistency', fontsize=20)
plt.savefig('Question2_BENG.jpg')
plt.show()
