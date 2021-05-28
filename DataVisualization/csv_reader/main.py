#%% Importing packages

from functions import *
from classes import *

#%% Defining the main function

plot = Plot("dark", "crest", False)

def main(csv_file):
    df = sns.load_dataset("tips")
    sns.set_style(plot.style); sns.set_palette(plot.palette)
    print(df)
    single_column(df)
    double_column(df, plot.trend)

main("testing_data.csv")