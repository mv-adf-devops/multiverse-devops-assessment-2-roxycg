import pandas as pd
row_list = ['user_id', 'first_name', 'last_name', 'answer_1', 'answer_2', 'answer_3']
length = 6
df = pd.DataFrame(index = range(0), columns= row_list)
print(row_list)
print(df)