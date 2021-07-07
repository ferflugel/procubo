import matplotlib.pyplot as plt
import seaborn as sns

class Plot:
    def __init__(self, plot_type, data, columns):
        self.plot_type = plot_type
        self.color = 'pastel'
        self.style = 'white'
        self.text = ''
        self.title = ''
        self.legend = False
        self.scale = ''
        self.transparency = 1
        self.despine = False
        self.data = data
        self.columns = columns
        self.ax = None
        
    def select_attributes(self):
        self.color = input(f'Select plot color (str):')
        self.style = input(f'Select plot style (str):')
        self.text = input(f'Insert text (str):')
        self.title = input(f'Insert title (str):')
        self.legend = input(f'Legend? (bool):')
        self.scale = input(f'Select plot scale (str):')
        self.transparency = float(input(f'Select plot transparency ([0, 1]):'))
        self.despine = input(f'Despine? (bool):')

    def plot_style(self):
        sns.set_palette(self.color)
        sns.set_style(self.style)

    def plot_adjustments(self):
        plt.text(10, 10, self.text)
        if self.scale is True:
            self.ax.set_xscale(self.scale)
            self.ax.set_yscale(self.scale)
        self.ax.set_title(self.title)
        if self.despine is True:
            sns.despine(ax=self.ax)
        if self.legend is True:
            plt.legend()
        plt.show()

class ColumnPlot(Plot):
    def __init__(self, plot_type, data, columns):
        super().__init__(plot_type, data, columns)
        self.orientation = 'h'

    def select_specific_attributes(self):
        self.orientation = int(input(f'Orientation (v or h): '))

    def plot(self):
        self.ax = sns.countplot(x = self.columns[0], data = self.data, orientation=self.orientation)

class Histogram(Plot):
    def __init__(self, plot_type, data, columns):
        super().__init__(plot_type, data, columns)
        self.width = 1

    def select_specific_attributes(self):
        self.width = int(input(f'Select bin width (0 for auto adjust): '))

    def plot(self):
        if self.width == 0:
            self.ax = sns.histplot(x = self.columns[0], data = self.data, alpha = self.transparency)
        else:
            self.ax = sns.histplot(x=self.columns[0], data=self.data, alpha=self.transparency, binwidth=self.width)

class PieChart(Plot):
    pass

class DonutChart(Plot):
    pass

class ScatterPlot(Plot):
    def __init__(self, plot_type, data, columns):
        super().__init__(plot_type, data, columns)
        self.hue = None
        self.best_fit = False
    
    def select_specific_attributes(self):
        self.hue = input(f'Select hue: ')
        self.best_fit = input(f'Show line of best fit: ')

    def plot(self):
        self.ax = sns.scatterplot(x = self.columns[0], y = self.columns[1], data = self.data, alpha = self.transparency, hue = self.hue)

class LinePlot(Plot):
    def __init__(self, plot_type, data, columns):
        super().__init__(plot_type, data, columns)
        self.line_style = '-'
        self.line_width = 1
    
    def select_specific_attributes(self):
        self.line_style = input(f'Select line style: ')
        self.line_width = input(f'Select line width: ')

    def plot(self):
        self.ax = sns.lineplot(x = self.columns[0], y = self.columns[1], data = self.data, alpha = self.transparency, lw = self.line_width, ls = self.line_style)
