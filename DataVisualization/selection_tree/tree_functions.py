import pandas as pd                 # Used to manipulate dataframes
import matplotlib.pyplot as plt     # Used to plotting basics
import seaborn as sns               # Used to get data sets and plotting style

def set_title():
    title = input('Choose a title for your plot')        # Asks for title
    plt.title(title)                                    # Adds title to plot

def set_axis():
    x_axis = input('x-axis name')                       # Asks for axis labels
    y_axis = input('y-axis name')
    plt.xlabel(x_axis)                                  # Set axis labels
    plt.ylabel(y_axis)