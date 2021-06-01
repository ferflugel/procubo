import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset("tips")
l1 = df['tip'].tolist()
l2 = df['total_bill'].tolist()
l3 = [pair for pair in zip(l1, l2)]
l3.sort()

def spikes_counter(lst):
    spikes = 0
    slope = 0
    for index in range(len(lst) - 1):
        if (lst[index+1][0] - lst[index][0]) == 0:
            slope = 1000
        else:
            slope = (lst[index+1][1] - lst[index][1]) / (lst[index+1][0] - lst[index][0])
        if abs(slope) > 790:
            print("SPIKE")
            spikes += 1
    if spikes > 10:
        print(spikes)
        return False
    return True

'''
Ideias para spikes: 

1) Definir o que é um SPIKE
2) Definir uma porcentagem "aceitavel" de SPIKES 

Ideias para districao:
1) Método dos quartiles


'''
