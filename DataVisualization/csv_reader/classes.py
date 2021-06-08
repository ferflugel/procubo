import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#e.g. Plot: Plot("dark", "crest")
class Plot:
    def __init__(self, style, palette, charType=sns.lineplot, X_axis_index=0, trend_line=False):
        self.style = style
        self.palette = palette
        self.trend_line = trend_line   #Whether or not to show a best-fit line
        self.graph = charType          #Determines the type of graph this class belongs to
        self.X_axis = X_axis_index     #The index of the fixed (X) axis on the csv columns order

    def load_attributes(self, data):
        sns.set_style(self.style)      #Sets the current plot style
        sns.set_palette(self.palette)  #Sets the current plot palette
        self.data = data
        #Processes the data according to the type of graph and info provided
        if self.graph == sns.lineplot:
            self.data_preproc = pd.melt(self.data, [self.data.keys()[self.X_axis]])


        self.ax = self.graph(x=self.data.keys()[self.X_axis],
                            y='value',
                            hue='variable',
                            data=self.data_preproc)

    def savePlot(self, x_label=self.data.keys()[self.X_axis], y_label='value', index=1):
        self.ax.set(xlabel=x_label, ylabel=y_label)
        plt.savefig("plot_%.3d"%(0+index))

    def show(self):
        plt.show()
