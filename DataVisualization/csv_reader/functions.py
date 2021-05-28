import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import itertools

def read_file(csv_file):
    df = pd.read_csv(csv_file)
    return df

def single_column(df):
    for column in df:
        if df[column].nunique() < 7:
            sns.countplot(x = column, data = df)
            plt.show()
        else:
            sns.histplot(x = column, data = df)
            plt.show()

def double_column(df, trend):
    combinations = select_correlations(df)
    for tp in combinations:
        sns.regplot(x = df[tp[0]], y = df[tp[1]], fit_reg = trend, data = df)
        plt.show()

def select_correlations(df):
    best_correlations = set()
    correlations = df.corr()
    np.fill_diagonal(correlations.values, 0)
    for column in correlations:
        correlations[column] = abs(correlations[column])
    max_correlations = correlations.idxmax()
    for column in correlations:
        best_correlations.add(tuple(sorted([column, max_correlations[column]])))
    return best_correlations