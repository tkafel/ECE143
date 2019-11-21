import numpy as np
import pandas as pd


def compute_grade_deviation(df,top_dev=10,good_dev=5,neg_dev=5):
    '''
    The following function computes the grade deviation 
    1. Difference of Expected grade - Actual grade 
    2. Expected grade - Actual grade
    3. List the top subjects in the current department with most abs deviation
    4. List the top_dev subjects with most difference
    5. List the good_dev, neg_dev course with most positive deviation and negative deviation
    
    Input: Data frame with Course Number, Expected Grade and Received Grade
    Ouput: Data frame with top_dev number of courses and their deviations
    '''
    assert isinstance(df,pd.DataFrame) and isinstance(good_dev,int) \
            and isinstance(top_dev,int) and isinstance(neg_dev,int)
    assert good_dev > 0 and top_dev > 0 and neg_dev > 0
    
    df['Grade_dev_abs'] = np.absolute(df['Avg Grade Expected'] - df['Avg Grade Received'])    
    df_sel = df[['Course Number','Grade_dev_abs','Term']]
    df_sel = df_sel.sort_values(by=['Grade_dev_abs'],ascending=False)
    df_sel.index = np.arange(1, len(df_sel)+1)
    unique_course = []
    unique_deviation = []
    i,j = (0,0)
    #Get unique courses
    while(i < top_dev):
        course = df_sel['Course Number'].iloc[j]
        deviation = df_sel['Grade_dev_abs'].iloc[j]
        j = j + 1
        if(course in unique_course):
            pass
        else:
            unique_course.append(course)
            unique_deviation.append(deviation)
            i = i + 1
    d = {'Course':unique_course,'Grad Deviation':unique_deviation}
    
    return pd.DataFrame(d,index=range(1,top_dev+1))
