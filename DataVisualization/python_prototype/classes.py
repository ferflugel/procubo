class Plot:
    def __init__(self, plot_type, xdata, ydata):
        self.plot_type = plot_type
        self.color = 'pastel'
        self.style = 'white'
        self.text = ''
        self.title = ''
        self.legend = ''
        self.scale = ''
        self.transprency = 1
        self.despine = False

    def select_attributes(self):
        self.color = input(f'Select plot color:')
        self.style = input(f'Select plot style:')
        self.text = input(f'Insert text:')
        self.title = input(f'Insert title:')
        self.legend = input(f'Insert legend:')
        self.scale = input(f'Select plot scale:')
        self.transprency = input(f'Select plot transparency:')
        self.despine = input(f'Select plot despine:')
        
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
