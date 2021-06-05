#%% Importing packages

import pandas as pd          # Used to manipulate dataframes
import seaborn as sns        # Used to get data sets and plotting

#%% User columns selection

df = sns.load_dataset('tips')        # Opens a made up data set
usr_columns = input(f'Select columns: \n {list(df.columns)}')

usr_columns = [string for string in usr_columns.split()]
df = df[usr_columns]                 # Filter dataframe with selected columns
print(df.head())                     # Just check if it worked

#%% Type of graph selection

one_col_graphs = ['column',
                  'pie',
                  'histogram']          # One column graphs
two_col_graphs = ['scatter',
                  'line']          # Two column graphs

if df.shape == 1:
    pass
elif df.shape == 2:
    pass
else:
    print('Not available yet :(')

#%% Style


#%% Color


#%% Adjustments

