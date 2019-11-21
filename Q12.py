def get_feedback(df):
    '''
    This function computes the total enrolled students in each department
    and the number of feedbacks received in that deparment
    Input: Data Frame of each department with Columns having Enroll and Evals Made
    Output: Total evaluation received, total enrollment and percentage evals in the course 
    '''
    assert isinstance(df,pd.DataFrame) and ('Enroll' in df.columns) and ('Evals Made' in df.columns)
    total_enroll = int(df.agg({'Enroll' : 'sum'}))
    total_evalls = int(df.agg({'Evals Made' : 'sum'}))
    feedback_ratio = total_evalls / total_enroll
    return total_evalls,total_enroll,feedback_ratio*100
