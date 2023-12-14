#define a function here
#to be taken out when running from Input
import pandas as pd
import numpy as np

#Ticket 1
def read_csv(csvfile):
    #creating an empty list to append csv to
    #import pandas as pd
    import csv
    count_row = 0
    with open(csvfile, newline='') as csvfile:
        for row in csvfile:
            row_list= row.strip().split(',')
            if count_row == 0:
                 #df = pd.Dataframe({})
                 column_headers = row_list
                 length =len(row_list)
                 df = pd.DataFrame(index = range(0), columns= column_headers)
                 #print(row_list)
                 #print(df)
                 count_row = count_row + 1
            else:
                # using loc methods
                df.loc[len(df)] = row_list
                #print(df)
    return df
    
#To be taken out
#df = read_csv('results.csv')
#print(df)

#Ticket 2
def remove_duplicate(df): 
    df = df.drop_duplicates(subset='user_id')
    return df
#remove duplicate entries based on user_id field
#keeps first duplicate by default
#df = remove_duplicate(df)
#print(df)


#Ticket 3 - remove empty rows
def ignore_empty_lines(df):
    df = df.replace('', np.nan)
    df.dropna(inplace=True) 
    return df

#running function 
#df = ignore_empty_lines(df)
#print(df)


#Ticket 4
def capitalise(df):
    df['first_name'] = df['first_name'].str.title()
    df['last_name'] = df['last_name'].str.title()
    return df


#running function
#df = capitalise(df)
#print(df)

#Ticket 5
#validate_answer_3
#running function
#df = validate_answer_3(df)
#print(df)

#Ticket 6
def cleaned_output(df):
    df.to_csv('cleaned_results.csv')
    return 

#running function
#df = cleaned_output(df)
#print(df)





