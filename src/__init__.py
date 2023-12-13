#define a function here

def read_csv(csvfile):
    #creating an empty list to append csv to
    import pandas as pd
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
                 print(row_list)
                 #print(df)
                 count_row = count_row + 1
            else:
                # using loc methods
                df.loc[len(df)] = row_list
                #print(df)
        return df

#running function - should be moved to other file
df = read_csv('results.csv')
print(df)

#remove duplicate entries based on user_id field
column_names = list(df.columns)
print(column_names)
#df_dededuped = df.drop_duplicates(subset=)
#print(df_dededuped)
#keeps first duplicate by default


