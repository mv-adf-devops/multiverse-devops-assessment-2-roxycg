#define a function here

#def read_csv():
    #creating an empty list to append csv to
import pandas as pd
import csv
count_row = 0
with open('results.csv', newline='') as csvfile:
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
           # df = df.append(pd.Series(row_list, index = column_headers), ignore_index=True)
           # df = pd.concat([df, pd.Series(row_list, index = column_headers]), ignore_index=True)
            # using loc methods
            df.loc[len(df)] = row_list
            #print(df)
    print(df)


#import csv
#with open('eggs.csv', newline='') as csvfile:
#    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#    for row in spamreader:
#        print(', '.join(row))


