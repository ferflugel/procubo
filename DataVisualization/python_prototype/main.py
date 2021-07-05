from functions import *

df = sns.load_dataset('tips')                           # Loads a test dataset

variables = get_variables(df)                           # Gets variables from user
plot_type = select_plot(len(variables))                 # Selects plot type

plot = create_plot(plot_type, df, variables)            # Creates a plot object

plot.select_attributes()                                # General attributes
plot.select_specific_attributes()                       # Specific attributes
plot.plot_style()                                       # Style and palette
plot.plot()                                             # Shows the plot to the user
plot.plot_adjustments()                                 # Adjusts extra parameters
