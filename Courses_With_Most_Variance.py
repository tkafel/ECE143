import pandas as pd 
import numpy as np 
##########################################################################################################
# Script Name: Courses_With_Most_Variance
# Script Description: This script is targeted to answer the first question in the
#                     project proposal. After the proprocessing of the data we 
#                     seperate the date in 4 dataframes based on 4 differnt departments.
#                     A new column called "student ratio" is introduced for each dataframe.
#                     Each dataframe is then grouped by based on the course number and
#                     the one row from each group wiht the highest ratio is extracted.
#                     This number indicates the one unique course with the most evaluations
#                     As a group we decided this would be the best way to get a fair answer 
#                     for our question. Next we introduce a new column for the ranking criteria
#                     In this column convert the grade recieved to a percentage value based on the
#                     4.0 scale and sum it up with the "recommended class" and "recommended Instructor"
#                     column together. The course are then ranked based on this value and the top result
#                     from each dataframe in our opinion would indiacte the best course ranked based on the 
#                     3 critatia and the available feedback given by the students.
###########################################################################################################

##########################################################################################################
###########################USE THE PROPROCESSED DATA TO SEPERATE OUT DEPARTMENTS##########################
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
#######################################Main Analysis for the data#########################################
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
ece_over_the_Range_mask = averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"] > ece_consistancy_upper_range
ece_below_the_range_mask = averged_out_ece_unique_course_df["Grade Received/Grade Expected Ratio"] < ece_consistancy_lower_range
ece_over_the_average_df = averged_out_ece_unique_course_df[ece_over_the_Range_mask].sort_values(by=["Grade Received/Grade Expected Ratio"], ascending =False)
ece_below_the_average_df = averged_out_ece_unique_course_df[ece_below_the_range_mask].sort_values(by=["Grade Received/Grade Expected Ratio"], ascending=False)


#cse
cse_mean_grade_ratio_val = averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"].mean()
cse_var_grade_ratio_val = averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"].std()
cse_consistancy_upper_range = cse_mean_grade_ratio_val + cse_var_grade_ratio_val
cse_consistancy_lower_range = cse_mean_grade_ratio_val - cse_var_grade_ratio_val
consistency_range_mask_cse = (averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] > cse_consistancy_upper_range) & (averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] < cse_consistancy_lower_range )
cse_most_variant_courses_df = averged_out_cse_unique_course_df[consistency_range_mask_cse]
cse_over_the_Range_mask = averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] > cse_consistancy_upper_range
cse_below_the_range_mask = averged_out_cse_unique_course_df["Grade Received/Grade Expected Ratio"] < cse_consistancy_lower_range
cse_over_the_average_df = averged_out_cse_unique_course_df[cse_over_the_Range_mask].sort_values(by=["Grade Received/Grade Expected Ratio"], ascending =False)
cse_below_the_average_df = averged_out_cse_unique_course_df[cse_below_the_range_mask].sort_values(by=["Grade Received/Grade Expected Ratio"], ascending=False)



# mae
mae_mean_grade_ratio_val = averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"].mean()
mae_var_grade_ratio_val = averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"].std()
mae_consistancy_upper_range = mae_mean_grade_ratio_val + mae_var_grade_ratio_val
mae_consistancy_lower_range = mae_mean_grade_ratio_val - mae_var_grade_ratio_val
consistency_range_mask_mae = (averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] > mae_consistancy_upper_range) & (averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] < mae_consistancy_lower_range )
mae_most_variant_courses_df = averged_out_mae_unique_course_df[consistency_range_mask_mae]
mae_over_the_Range_mask = averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] > mae_consistancy_upper_range
mae_below_the_range_mask = averged_out_mae_unique_course_df["Grade Received/Grade Expected Ratio"] < mae_consistancy_lower_range
mae_over_the_average_df = averged_out_mae_unique_course_df[mae_over_the_Range_mask].sort_values(by=["Grade Received/Grade Expected Ratio"], ascending =False)
mae_below_the_average_df = averged_out_mae_unique_course_df[mae_below_the_range_mask].sort_values(by=["Grade Received/Grade Expected Ratio"], ascending=False)




#beng
beng_mean_grade_ratio_val = averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"].mean()
beng_var_grade_ratio_val = averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"].std()
beng_consistancy_upper_range = beng_mean_grade_ratio_val + beng_var_grade_ratio_val
beng_consistancy_lower_range = beng_mean_grade_ratio_val - beng_var_grade_ratio_val
consistency_range_mask_beng = (averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] > beng_consistancy_upper_range) & (averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] < beng_consistancy_lower_range )
beng_most_variant_courses_df = averged_out_beng_unique_course_df[consistency_range_mask_beng]
beng_over_the_Range_mask = averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] > beng_consistancy_upper_range
beng_below_the_range_mask = averged_out_beng_unique_course_df["Grade Received/Grade Expected Ratio"] < beng_consistancy_lower_range
beng_over_the_average_df = averged_out_beng_unique_course_df[beng_over_the_Range_mask].sort_values(by=["Grade Received/Grade Expected Ratio"], ascending =False)
beng_below_the_average_df = averged_out_beng_unique_course_df[beng_below_the_range_mask].sort_values(by=["Grade Received/Grade Expected Ratio"], ascending=False)

#visualization and plotting
#ece
ece_over_the_average_df.reset_index(inplace=True)
ece_below_the_average_df.reset_index(inplace=True)
top5_ece_df = pd.DataFrame()
last5_ece_df = pd.DataFrame()
question_3_ece_df = pd.DataFrame()
a = ece_over_the_average_df.nlargest(5, "Grade Received/Grade Expected Ratio")
b = ece_below_the_average_df.nsmallest(5, "Grade Received/Grade Expected Ratio")
top5_ece_df = top5_ece_df.append(a)
last5_ece_df = last5_ece_df.append(b)
question_3_ece_df = question_3_ece_df.append(top5_ece_df)
question_3_ece_df = question_3_ece_df.append(last5_ece_df)
ax = question_3_ece_df.plot.bar(x='Course', y='Grade Received/Grade Expected Ratio', rot=0, figsize = (20,10), title='ECE Courses with the most variance in grades expected and recieved', color='green')
ax.title.set_size(30)
ax.set_xlabel('ECE Courses', fontsize=15)
ax.set_ylabel('Expected to receieved grade ratio', fontsize=15)

#cse
cse_over_the_average_df.reset_index(inplace=True)
cse_below_the_average_df.reset_index(inplace=True)
top5_cse_df = pd.DataFrame()
last5_cse_df = pd.DataFrame()
question_3_cse_df = pd.DataFrame()
c = cse_over_the_average_df.nlargest(5, "Grade Received/Grade Expected Ratio")
d = cse_below_the_average_df.nsmallest(5, "Grade Received/Grade Expected Ratio")
top5_cse_df = top5_cse_df.append(c)
last5_cse_df = last5_cse_df.append(d)
question_3_cse_df = question_3_cse_df.append(top5_cse_df)
question_3_cse_df = question_3_cse_df.append(last5_cse_df)
ax = question_3_cse_df.plot.bar(x='Course', y='Grade Received/Grade Expected Ratio', rot=0, figsize = (20,10), title='CSE Courses with the most variance in grades expected and recieved', color='blue')
ax.title.set_size(30)
ax.set_xlabel('ECE Courses', fontsize=15)
ax.set_ylabel('Expected to receieved grade ratio', fontsize=15)

#mae
mae_over_the_average_df.reset_index(inplace=True)
mae_below_the_average_df.reset_index(inplace=True)
top5_mae_df = pd.DataFrame()
last5_mae_df = pd.DataFrame()
question_3_mae_df = pd.DataFrame()
e = mae_over_the_average_df.nlargest(5, "Grade Received/Grade Expected Ratio")
f = mae_below_the_average_df.nsmallest(5, "Grade Received/Grade Expected Ratio")
top5_mae_df = top5_mae_df.append(e)
last5_mae_df = last5_mae_df.append(f)
question_3_mae_df = question_3_mae_df.append(top5_mae_df)
question_3_mae_df = question_3_mae_df.append(last5_mae_df)
ax = question_3_mae_df.plot.bar(x='Course', y='Grade Received/Grade Expected Ratio', rot=0, figsize = (20,10), title='MAE Courses with the most variance in grades expected and recieved', color='red')
ax.title.set_size(30)
ax.set_xlabel('ECE Courses', fontsize=15)
ax.set_ylabel('Expected to receieved grade ratio', fontsize=15)

#beng
beng_over_the_average_df.reset_index(inplace=True)
beng_below_the_average_df.reset_index(inplace=True)
top5_beng_df = pd.DataFrame()
last5_beng_df = pd.DataFrame()
question_3_beng_df = pd.DataFrame()
g = beng_over_the_average_df.nlargest(5, "Grade Received/Grade Expected Ratio")
h = beng_below_the_average_df.nsmallest(5, "Grade Received/Grade Expected Ratio")
top5_beng_df = top5_beng_df.append(g)
last5_beng_df = last5_beng_df.append(h)
question_3_beng_df = question_3_beng_df.append(top5_beng_df)
question_3_beng_df = question_3_beng_df.append(last5_beng_df)
ax = question_3_beng_df.plot.bar(x='Course', y='Grade Received/Grade Expected Ratio', rot=0, figsize = (20,10), title='BENG Courses with the most variance in grades expected and recieved', color='black')
ax.title.set_size(30)
ax.set_xlabel('ECE Courses', fontsize=15)
ax.set_ylabel('Expected to receieved grade ratio', fontsize=15)
