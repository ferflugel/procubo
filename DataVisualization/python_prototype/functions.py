import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def get_variables(df):
    usr_columns = input(f'Select columns: \n {list(df.columns)}')
    usr_columns = [string for string in usr_columns.split()]
    return usr_columns

def select_plot(number_of_variables):
    one_variable = ['column', 'histogram', 'pie', 'donut']
    two_variables = ['histogram', 'scatter', 'line']
    if number_of_variables == 1:
        type_of_plot = input(f'Select plot type: \n {one_variable}')
    elif number_of_variables == 2:
        type_of_plot = input(f'Select plot type: \n {two_variables}')
    else:
        print('Not available yet :(')
        type_of_plot = 'None'
    return type_of_plot

def select_color(plot):
    color = input(f'Select plot color:')
    plot.color = color

