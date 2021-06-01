import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


l1 = df['tip'].tolist()
l2 = df['total_bill'].tolist()
l3 = [pair for pair in zip(l1, l2)]
l3.sort()
