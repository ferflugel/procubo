import pandas as pd
from classes import *

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

def create_plot(plot_type, data, variables):
    if plot_type == 'column':
        return ColumnPlot(plot_type, data, variables)
    elif plot_type == 'histogram':
        return Histogram(plot_type, data, variables)
    elif plot_type == 'pie':
        return PieChart(plot_type, data, variables)
    elif plot_type == 'donut':
        return DonutChart(plot_type, data, variables)
    elif plot_type == 'scatter':
        return ScatterPlot(plot_type, data, variables)
    elif plot_type == 'line':
        return LinePlot(plot_type, data, variables)
    else:
        print('Invalid plot type')
        return False

