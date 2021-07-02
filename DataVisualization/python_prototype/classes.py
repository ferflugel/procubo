class Plot:
    def __init__(self, plot_type):
        self.plot_type = plot_type
        self.color = 'pastel'

    def select_color(self):
        self.color = input(f'Select plot color:')

class ColumnPlot(Plot):
    pass

class Histogram(Plot):
    pass

class PieChart(Plot):
    pass

class DonutChart(Plot):
    pass

class ScatterPlot(Plot):
    pass

class LinePlot(Plot):
    pass