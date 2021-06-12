#%% Importing packages

from tree_functions import *            # Imports functions and libraries

#%% User columns selection

df = sns.load_dataset('tips')                                       # Opens a made up data set
usr_columns = input(f'Select columns: \n {list(df.columns)}')       # Asks for columns to be plotted

usr_columns = [string for string in usr_columns.split()]
df = df[usr_columns]                                                # Filter dataframe with selected columns
print(df.head())                                                    # Just check if it worked

#%% Type of graph selection

one_col_graphs = ['column',
                  'pie',
                  'histogram']          # One column graph types

two_col_graphs = ['scatter',
                  'line']               # Two column graph types

if df.shape[1] == 1:                                                       # User is analyzing one column
    plot_type = input(f'Select the plot type: {one_col_graphs}')
elif df.shape[1] == 2:                                                     # User is analyzing two columns
    plot_type = input(f'Select the plot type: {two_col_graphs}')
else:
    plot_type = None
    print('Not available yet :(')                                       # Only one and two columns are accepted

#%% Style

styles_options = ['white', 'dark', 'whitegrid', 'darkgrid']      # Available styles for seaborn
usr_style = input(f'Choose style: {styles_options}')             # Asks for style
sns.set_style(usr_style)                                         # Adds the style to the plot

#%% Color

palette = input('Select your color palette (e.g. "crest", "pastel", "flare")')      # Asks for palette
sns.set_palette(palette)                                                            # Adds color palette

#%% Plot the figure

'''
It would probably be good to add the adjustments inside of these
conditionals, once each plot type has specific types of kwargs. To 
be done in the future.  
'''

if plot_type == 'column':
    sns.countplot(x = usr_columns[0], data = df)                            # Basic column chart
elif plot_type == 'pie':
    print('Plot type not available :(')                                     # Pie charts are currently not available
elif plot_type == 'histogram':
    sns.histplot(x = usr_columns[0], data = df)                             # Histogram
elif plot_type == 'scatter':
    sns.scatterplot(x = usr_columns[0], y = usr_columns[1], data=df)        # Scatter can have LOTS of adjustments
elif plot_type == 'line':
    sns.lineplot(x = usr_columns[0], y = usr_columns[1], data=df)           # Basic line (what about multiple lines?)
else:
    print('Plot type not available :(')                                     # Other plot types

#%% Title, axis, and showing plot

set_title()           # Adds a nice title
set_axis()            # Adds axis labels
plt.show()            # Shows the plot