#pip install pandas #run in command line ahead of file
import pandas as pd


#Ticket 1
from __init__ import read_csv
#from src import read_csv

#running function 
df = read_csv('results.csv')
#print(df)

#Ticket 2
from __init__ import remove_duplicate
#running function
df = remove_duplicate(df)
#print(df)

#Ticket 3
from __init__ import ignore_empty_lines
#running function 
df = ignore_empty_lines(df)
#print(df)


#Ticket 4
from __init__ import capitalise
#running function
df = capitalise(df)
#print(df)

#Ticket 5
#from __init__ import validate_answer_3
#running function
#df = validate_answer_3(df)
#print(df)

#Ticket 6
from __init__ import cleaned_output
#running function
df = cleaned_output(df)
#print(df)

