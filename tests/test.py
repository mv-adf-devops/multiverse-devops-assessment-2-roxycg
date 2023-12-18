#Testing each funtion
#Importing Functions
#from src/__init__ import *
#import pytest
import pandas
#Testing Ticket 1 - Is it a Pandas Dataframe? 
def test_read_csv():
    #Setting up test
    file = 'results.csv'
    object_type = pandas.core.frame.DataFrame

    #running function being tested
    function_result = read_csv(file)

    #Checking Test Output
    assert type(function_result) == object_type

#running test
#test_read_csv()


#Testing Ticket 2 - Does it take out duplicates? 
#def test_remove_duplicate():
#Setting up test
 #   file = 'results.csv'
 #   deduped_results_df = pd.DataFrame({"user_id":['1', '2', '', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
#    "first_name": ['Charissa', 'richard', '', 'patience', 'Harding', 'India', 'Abra', 'Bryar', 'Diana', 'Alexander', 'Graiden', 'Uma', 'Brittany', 'Roth', 'Amos', 'Caesar', 'Eugenia', 'dieter', 'Roary', 'Ulric', 'Felicia'],
#    "last_name": ['Clark', 'McKinney', '', 'reeves', 'Estrada', 'Gentry', 'Sheppard', 'cooley', 'Cameron', 'Herring', 'Cannon', 'Glass', 'Weeks', 'Stout', 'Daniel', 'Rivers', 'Nichols', 'alvarado', 'Frank', 'Hensley', 'Wilkins'], 
#    "answer_1": ['yes', 'yes', '', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'no', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes'],
#    "answer_2": ['c', 'b', '', 'b', 'b', 'c', 'b', 'a', 'b', 'b', 'b', 'a', 'b', 'c', 'a', 'b', 'b', 'b', 'c', 'b', 'b'],
#    "answer_3": ['7', '7', '', '9', '14', '7', '6', '11', '9', '4', '13', '2', '8', '10', '5', '7', '6', '6', '7', '9', '8']})

    #running function being tested    #read_csv(file)
    #df = read_csv(file)
#    function_output = remove_duplicate(df)
    
    #Checking Test Output
    #assert function_output == deduped_results_df
#    print(function_output)
#    print(deduped_results_df)

#running test
#file = 'results.csv'
#df = read_csv(file)

#test_remove_duplicate()
#count_duplicates = df.pivot_table(index=['user_id'], aggfunc='size')
#count_duplicates = count_duplicates[['size'] > 1]
#print(count_duplicates)

#Importing Ticket 3
#from __init__ import ig
    #inore_empty_lines
#Testing Ticket 3 - Does it remove empty lines? 
#def test_ignore_empty_lines():



#Importing Ticket 4
#from __init__ import capitalise
#Testing Ticket 4 - Does it capitalise names? 
#def test_capitalise():


#Ticket 5
#from __init__ import validate_answer_3


#Ticket 6
#from __init__ import cleaned_output







#def test_remove_duplicates():
    #Arrange
#    test_array = [[4,"Harding","Estrada","no",14],[5,"India","Gentry","yes",7],
#                  [6,"Abra","Sheppard","yes",6],[6,"Abra","Sheppard","no",8]]
    #Act
#    array_deduped = remove_duplicates(test_array)
    #Assert
#    assert array_deduped == [[4,"Harding","Estrada","no",14],[5,"India","Gentry","yes",7],
#                  [6,"Abra","Sheppard","yes",6]]

#def test_remove_duplicates_from_results():
    #Arrange
#    filename = 'results.csv'
#    input = get_input(filename) 
#    #Act
#    array_deduped = remove_duplicates(input)
#    #Assert
#    assert array_deduped == [['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3'], ['1', 'Charissa', 'Clark', 'yes', 'c', '7'], ['2', 'richard', 'McKinney', 'yes', 'b', '7'], ['', '', '', '', '', ''], ['3', 'patience', 'reeves', 'yes', 'b', '9'], ['4', 'Harding', 'Estrada', 'no', 'b', '14'], ['5', 'India', 'Gentry', 'yes', 'c', '7'], ['6', 'Abra', 'Sheppard', 'yes', 'b', '6'], ['7', 'Bryar', 'cooley', 'yes', 'a', '11'], ['8', 'Diana', 'Cameron', 'yes', 'b', '9'], ['9', 'Alexander', 'Herring', 'no', 'b', '4'], ['10', 'Graiden', 'Cannon', 'no', 'b', '13'], ['11', 'Uma', 'Glass', 'yes', 'a', '2'], ['12', 'Brittany', 'Weeks', 'yes', 'b', '8'], ['13', 'Roth', 'Stout', 'yes', 'c', '10'], ['14', 'Amos', 'Daniel', 'yes', 'a', '5'], ['15', 'Caesar', 'Rivers', 'yes', 'b', '7'], ['16', 'Eugenia', 'Nichols', 'yes', 'b', '6'], ['17', 'dieter', 'alvarado', 'yes', 'b', '6'], ['18', 'Roary', 'Frank', 'yes', 'c', '7'], ['19', 'Ulric', 'Hensley', 'no', 'b', '9'], ['20', 'Felicia', 'Wilkins', 'yes', 'b', '8']]

#def test_remove_empty_lines():
     #Arrange
#    test_array = [[4,"Harding","Estrada","no",14],["","","","",],
#                  [6,"Abra","Sheppard","yes",6],[6,"Abra","Sheppard","no",8]]
    #Act
#    array_deduped = remove_duplicates(test_array)
#    array_clean = remove_empty_lines(array_deduped)
    #Assert
#    assert array_clean == [[4,"Harding","Estrada","no",14],
 #                 [6,"Abra","Sheppard","yes",6]]

# Ticket 4

#def test_capitalize_names():
    # Arrange (Define input data)
#    headers = ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3']
 #   data = [
  #      [1, 'john', 'doe', 'yes', 'no', 'yes'],
   #     [2, 'jane', 'smith', 'no', 'yes', 'no'],
    #]

    # Act (Apply the function to the data)
    #result = capitalize_names(headers, data)

    # Assert (Check if the first_name and last_name fields are capitalized)
    #for entry in result:
     #   assert entry[headers.index('first_name')] == entry[headers.index('first_name')].capitalize()
      #  assert entry[headers.index('last_name')] == entry[headers.index('last_name')].capitalize()

# Ticket 5

#def test_validate_answer_3():
    # Arrange (Define input data)
#    data = [
#        [1, 'John', 'Doe', 'yes', 'no', 5],
#        [2, 'Jane', 'Smith', 'no', 'yes', 12],
#        [3, 'Alice', 'Johnson', 'yes', 'yes', 'invalid'],
#        [4, 'Bob', 'Brown', 'no', 'no', 8],
#    ]

    # Act (Apply the function to the data)
#    result = validate_answer_3(data)

    # Assert (Check if the result contains only valid rows)
#    for entry in result:
#        assert 1 <= entry[5] <= 10  # Directly access 'answer_3' by index (assuming it's at index 5)

# Ticket 6

#def test_output_exists():
    # arrange
#    in_file = "results.csv"
#    out_file = "results_output_test.csv"
    # act
#    in_data = get_input(in_file)
#    output_to_file(out_file,in_data)
#    out_data = get_input(out_file)
    # assert
#    assert out_data == in_data)