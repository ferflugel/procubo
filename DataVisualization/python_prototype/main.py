from functions import *
from classes import *

df = sns.load_dataset('tips')              # Loads a test dataset

variables = get_variables(df)              # Gets variables from user
plot_type = select_plot(len(variables))    # Selects plot type

plot = Plot(plot_type)                     # Creates a plot object

plot.select_color()                        # Selects color palette
