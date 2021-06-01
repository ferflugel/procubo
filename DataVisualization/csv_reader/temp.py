import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


l1 = df['tip'].tolist()
l2 = df['total_bill'].tolist()
l3 = [pair for pair in zip(l1, l2)]
l3.sort()

def spikes_counter(lst):
  spikes = 0
  for index in range(len(lst)):
    m = (len[index+1][1] - len[index][1]) / (len[index+1][0] - len[index][0])
    if abs(m) > 2:
      spikes +=1
    if spikes > 10:
      return False
  return True
