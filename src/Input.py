#pip install pandas #run in command line ahead of file
import pandas as pd

from __init__ import *
#Ticket 1
#from src import read_csv
#from src import read_csv

#running function 
df = read_csv('results.csv')
#print(df)

#Ticket 2
#from src import remove_duplicate
#running function
df = remove_duplicate(df)
#print(df)

#Ticket 3
#from src import ignore_empty_lines
#running function 
df = ignore_empty_lines(df)
#print(df)


#Ticket 4
#from src import capitalise
#running function
df = capitalise(df)
#print(df)

#Ticket 5
from __init__ import validate_answer_3
#running function
df = validate_answer_3(df)
print(df.values.tolist())

#Ticket 6
#from src import cleaned_output
#running function
df = cleaned_output(df)
#print(df)

