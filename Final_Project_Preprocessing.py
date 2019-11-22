#import pandas 
import pandas as pd
import numpy as np

#define necessary functions for clean up
def get_course_number(course):
    course_num = course.split("-")
    return course_num[0]

def get_course_description(course):
    course_description = course.split("-")
    final_course_description = course_description[1].split("(")
    return final_course_description[0]

def grade_cleaner(grade):
    temp =  grade.split("(")
    temp_grade = temp[1]
    temp_grade_2 = temp_grade.split(")")
    final_grade = temp_grade_2[0]
    return final_grade

def percent_cleaner(percent):
    temp = percent.split(" ")
    return temp[0]

def get_department(name):
    department = name.split(" ")
    return department[0]

#check dataframe size before clean up
df = pd.read_csv("143Data.csv")


#read the dataframe, apply cleanup to data and convert data accordingly
df.dropna(inplace = True)
df["Course Number"] = df["Course"].apply(get_course_number)
df["Course Description"] = df["Course"].apply(get_course_description)
df["Avg Grade Received"] = df["Avg Grade Received"].apply(grade_cleaner)
df["Avg Grade Expected"] = df["Avg Grade Expected"].apply(grade_cleaner)
df["Rcmnd Class"] = df["Rcmnd Class"].apply(percent_cleaner)
df["Rcmnd Instr"] = df["Rcmnd Instr"].apply(percent_cleaner)
df["Department"] = df["Course Number"].apply(get_department)
df["Rcmnd Class"] = df["Rcmnd Class"].astype(float)
df["Rcmnd Instr"] = df["Rcmnd Instr"].astype(float)
df["Avg Grade Received"] = df["Avg Grade Received"].astype(float)
df["Avg Grade Expected"] = df["Avg Grade Expected"].astype(float)
df["Term"] = df["Term"].astype("category")
df["Department"] = df["Department"].astype("category")


df.drop(columns="Course", inplace=True)

df[["Instructor", "Course Number", "Course Description", "Term", "Enroll", "Evals Made", "Rcmnd Class", "Rcmnd Instr", "Study Hrs/wk", "Avg Grade Expected", "Avg Grade Received"]]
df.index = np.arange(0, len(df))

selected = df.groupby(["Department", "Course Number", "Instructor", "Term"])

new = selected.agg({"Enroll" : "sum",
                    "Evals Made": "sum",
                    "Rcmnd Class": "mean",
                    "Rcmnd Instr" : "mean",
                    "Study Hrs/wk": "mean",
                    "Avg Grade Expected": "mean",
                    "Avg Grade Received": "mean"
                  })
new.to_csv("Preprocess_Completed.csv")