import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

'''
This is just a dummy class for now, a similar (and better) architecture will be
used later to provide an easy way of personalizing graphs. 
'''

class Single_Variable_Plot:
    def __init__(self, style, palette):
        self.style = style
        self.palette = palette

Single = Single_Variable_Plot("dark", "pastel")

def main(csv_file):
    sns.set_style(Single.style)
    sns.set_palette(Single.palette)
    df = pd.read_csv(csv_file)
    # Single column analysis
    single_column(df)
    # Double column analysis
    double_column(df)


def single_column(df):
    for column in df:
        if df[column].nunique() < 7:
            sns.countplot(x = column, data = df)
            plt.show()
        else:
            sns.histplot(x = column, data = df)
            plt.show()


def double_column(df):
    comb = find_combinations(len(df.columns))
    comb = select_tuples(comb)
    for tp in comb:
        sns.scatterplot(x = df.iloc[:, tp[0]], y = df.iloc[:, tp[1]], data = df)
        plt.show()


def find_combinations(n):
    array = list(range(n))
    comb = list(itertools.combinations(array, 2))
    comb = set(comb)
    return comb


'''
This function will be responsible for choosing the tuples that make more 
sense to be plotted together. I'm not totally sure how to perform this analysis
'''
def select_tuples(tuple_set):
    return tuple_set

main("testing_data.csv")