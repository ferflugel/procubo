import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List

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

'''     HELPER FUNCTIONS      '''

def distance_between_x_data(x_data: List[int]) -> bool:
    x_data.sort()
    maximum, minimum = x_data[-1], x_data[0]
    partition = 0.2 * (maximum - minimum)
    buckets = [0, 0, 0, 0, 0]
    for index, item in enumerate(x_data):
        i = 0
        for threshold in np.arange(minimum + partition, maximum + partition, partition):
            i += 1
            if item <= threshold:
                buckets[i] += 1
                break
    print(buckets)
    return True










def select_correlations(df):
    best_correlations = set()
    correlations = df.corr()
    np.fill_diagonal(correlations.values, 0)
    for column in correlations:
        correlations[column] = abs(correlations[column])
    max_correlations = correlations.idxmax()
    for column in correlations:
        best_correlations.add(tuple(sorted([column, max_correlations[column]])))
    print(best_correlations)
    return best_correlations