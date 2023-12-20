#Testing each funtion
#Importing Functions

import sys
import pytest
import pandas

#Testing Ticket 1 - Is it a Pandas Dataframe? 
def test_read_csv():
    #Setting up test
    from __init__ import read_csv
    file = 'results.csv'
    object_type = pandas.core.frame.DataFrame

    #running function being tested
    function_result = read_csv(file)

    #Checking Test Output
    assert type(function_result) == object_type


#Testing Ticket 2 - Does it take out duplicates? 
def test_remove_duplicate():
    #Setting up test
    #from src.extract.__init__ import *
    #from extract.__init__ import read_csv
    from __init__ import read_csv
    from __init__ import remove_duplicate 
    #from src.extract import remove_duplicate
    file = 'results.csv'
    df = read_csv(file)
    #Running Test
    function_output = remove_duplicate(df)
    #Checking Test Output
    assert function_output.values.tolist() == [['1', 'Charissa', 'Clark', 'yes', 'c', '7'], ['2', 'richard', 'McKinney', 'yes', 'b', '7'], ['', '', '', '', '', ''], ['3', 'patience', 'reeves', 'yes', 'b', '9'], ['4', 'Harding', 'Estrada', 'no', 'b', '14'], ['5', 'India', 'Gentry', 'yes', 'c', '7'], ['6', 'Abra', 'Sheppard', 'yes', 'b', '6'], ['7', 'Bryar', 'cooley', 'yes', 'a', '11'], ['8', 'Diana', 'Cameron', 'yes', 'b', '9'], ['9', 'Alexander', 'Herring', 'no', 'b', '4'], ['10', 'Graiden', 'Cannon', 'no', 'b', '13'], ['11', 'Uma', 'Glass', 'yes', 'a', '2'], ['12', 'Brittany', 'Weeks', 'yes', 'b', '8'], ['13', 'Roth', 'Stout', 'yes', 'c', '10'], ['14', 'Amos', 'Daniel', 'yes', 'a', '5'], ['15', 'Caesar', 'Rivers', 'yes', 'b', '7'], ['16', 'Eugenia', 'Nichols', 'yes', 'b', '6'], ['17', 'dieter', 'alvarado', 'yes', 'b', '6'], ['18', 'Roary', 'Frank', 'yes', 'c', '7'], ['19', 'Ulric', 'Hensley', 'no', 'b', '9'], ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8']]


#Testing Ticket 3 - Does it remove empty lines? 
def test_ignore_empty_lines():
    #Setting up test
    from __init__ import read_csv
    from __init__ import remove_duplicate 
    from __init__ import ignore_empty_lines
    file = 'results.csv'
    df = read_csv(file)
    df = remove_duplicate(df)
    #Running Test
    function_output = ignore_empty_lines(df)
    #Checking Test Output
    assert function_output.values.tolist() == [['1', 'Charissa', 'Clark', 'yes', 'c', '7'], ['2', 'richard', 'McKinney', 'yes', 'b', '7'], ['3', 'patience', 'reeves', 'yes', 'b', '9'], ['4', 'Harding', 'Estrada', 'no', 'b', '14'], ['5', 'India', 'Gentry', 'yes', 'c', '7'], ['6', 'Abra', 'Sheppard', 'yes', 'b', '6'], ['7', 'Bryar', 'cooley', 'yes', 'a', '11'], ['8', 'Diana', 'Cameron', 'yes', 'b', '9'], ['9', 'Alexander', 'Herring', 'no', 'b', '4'], ['10', 'Graiden', 'Cannon', 'no', 'b', '13'], ['11', 'Uma', 'Glass', 'yes', 'a', '2'], ['12', 'Brittany', 'Weeks', 'yes', 'b', '8'], ['13', 'Roth', 'Stout', 'yes', 'c', '10'], ['14', 'Amos', 'Daniel', 'yes', 'a', '5'], ['15', 'Caesar', 'Rivers', 'yes', 'b', '7'], ['16', 'Eugenia', 'Nichols', 'yes', 'b', '6'], ['17', 'dieter', 'alvarado', 'yes', 'b', '6'], ['18', 'Roary', 'Frank', 'yes', 'c', '7'], ['19', 'Ulric', 'Hensley', 'no', 'b', '9'], ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8']]




#Testing Ticket 4 - Does it capitalise names? 
def test_capitalise():
    #Setting up test
    from __init__ import read_csv
    from __init__ import remove_duplicate 
    from __init__ import ignore_empty_lines
    from __init__ import capitalise
    file = 'results.csv'
    df = read_csv(file)
    df = remove_duplicate(df)
    df = ignore_empty_lines(df)
    #Running Test
    function_output = capitalise(df)
    #Checking Test Output
    assert function_output.values.tolist() == [['1', 'Charissa', 'Clark', 'yes', 'c', '7'], ['2', 'Richard', 'Mckinney', 'yes', 'b', '7'], ['3', 'Patience', 'Reeves', 'yes', 'b', '9'], ['4', 'Harding', 'Estrada', 'no', 'b', '14'], ['5', 'India', 'Gentry', 'yes', 'c', '7'], ['6', 'Abra', 'Sheppard', 'yes', 'b', '6'], ['7', 'Bryar', 'Cooley', 'yes', 'a', '11'], ['8', 'Diana', 'Cameron', 'yes', 'b', '9'], ['9', 'Alexander', 'Herring', 'no', 'b', '4'], ['10', 'Graiden', 'Cannon', 'no', 'b', '13'], ['11', 'Uma', 'Glass', 'yes', 'a', '2'], ['12', 'Brittany', 'Weeks', 'yes', 'b', '8'], ['13', 'Roth', 'Stout', 'yes', 'c', '10'], ['14', 'Amos', 'Daniel', 'yes', 'a', '5'], ['15', 'Caesar', 'Rivers', 'yes', 'b', '7'], ['16', 'Eugenia', 'Nichols', 'yes', 'b', '6'], ['17', 'Dieter', 'Alvarado', 'yes', 'b', '6'], ['18', 'Roary', 'Frank', 'yes', 'c', '7'], ['19', 'Ulric', 'Hensley', 'no', 'b', '9'], ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8']]


#Ticket 5
#from __init__ import validate_answer_3
def test_validate_answer_3():
    #Setting up test
    from __init__ import read_csv
    from __init__ import remove_duplicate 
    from __init__ import ignore_empty_lines
    from __init__ import capitalise
    from __init__ import validate_answer_3
    file = 'results.csv'
    df = read_csv(file)
    df = remove_duplicate(df)
    df = ignore_empty_lines(df)
    df = capitalise(df)
    #Running Test
    function_output = validate_answer_3(df)
    #Checking Test Output
    assert function_output.values.tolist() == [['1', 'Charissa', 'Clark', 'yes', 'c', 7], ['2', 'Richard', 'Mckinney', 'yes', 'b', 7], ['3', 'Patience', 'Reeves', 'yes', 'b', 9], ['5', 'India', 'Gentry', 'yes', 'c', 7], ['6', 'Abra', 'Sheppard', 'yes', 'b', 6], ['8', 'Diana', 'Cameron', 'yes', 'b', 9], ['9', 'Alexander', 'Herring', 'no', 'b', 4], ['11', 'Uma', 'Glass', 'yes', 'a', 2], ['12', 'Brittany', 'Weeks', 'yes', 'b', 8], ['13', 'Roth', 'Stout', 'yes', 'c', 10], ['14', 'Amos', 'Daniel', 'yes', 'a', 5], ['15', 'Caesar', 'Rivers', 'yes', 'b', 7], ['16', 'Eugenia', 'Nichols', 'yes', 'b', 6], ['17', 'Dieter', 'Alvarado', 'yes', 'b', 6], ['18', 'Roary', 'Frank', 'yes', 'c', 7], ['19', 'Ulric', 'Hensley', 'no', 'b', 9], ['20', 'Felicia', 'Wilkins', 'yes', 'b', 8]]

#Ticket 6
#from __init__ import cleaned_output
#def test_cleaned_output():
    #Setting up test
#    from __init__ import read_csv
#    from __init__ import remove_duplicate 
#    from __init__ import ignore_empty_lines
#    from __init__ import capitalise
#    from __init__ import validate_answer_3
#    from __init__ import cleaned_output
#    file = 'results.csv'
#    df = read_csv(file)
#    df = remove_duplicate(df)
#    df = ignore_empty_lines(df)
#    df = capitalise(df)
#    df = validate_answer_3(df)
    #Running Test
#    function_output = cleaned_output(df)
    #Checking Test Output
#    assert 'cleaned_results.csv' == 'cleaned_results_test.csv'

#Ticket 7
def test_print_clean_results():
    from __init__ import list_clean_results
    file = 'cleaned_results.csv'
    #Running Test
    function_output = list_clean_results('cleaned_results.csv')
    #Checking Test Output
    assert function_output == [['1', 'Charissa', 'Clark', 'yes', 'c', '7'], ['2', 'Richard', 'Mckinney', 'yes', 'b', '7'], ['3', 'Patience', 'Reeves', 'yes', 'b', '9'], ['5', 'India', 'Gentry', 'yes', 'c', '7'], ['6', 'Abra', 'Sheppard', 'yes', 'b', '6'], ['8', 'Diana', 'Cameron', 'yes', 'b', '9'], ['9', 'Alexander', 'Herring', 'no', 'b', '4'], ['11', 'Uma', 'Glass', 'yes', 'a', '2'], ['12', 'Brittany', 'Weeks', 'yes', 'b', '8'], ['13', 'Roth', 'Stout', 'yes', 'c', '10'], ['14', 'Amos', 'Daniel', 'yes', 'a', '5'], ['15', 'Caesar', 'Rivers', 'yes', 'b', '7'], ['16', 'Eugenia', 'Nichols', 'yes', 'b', '6'], ['17', 'Dieter', 'Alvarado', 'yes', 'b', '6'], ['18', 'Roary', 'Frank', 'yes', 'c', '7'], ['19', 'Ulric', 'Hensley', 'no', 'b', '9'], ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8']]
    



