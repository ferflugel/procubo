class Plot:
    def __init__(self, plot_type, data, columns):
        self.plot_type = plot_type
        self.color = 'pastel'
        self.style = 'white'
        self.text = ''
        self.title = ''
        self.legend = ''
        self.scale = ''
        self.transparency = 1
        self.despine = False
        self.data = data
        self.columns = columns
        
    def select_attributes(self):
        self.color = input(f'Select plot color:')
        self.style = input(f'Select plot style:')
        self.text = input(f'Insert text:')
        self.title = input(f'Insert title:')
        self.legend = input(f'Insert legend:')
        self.scale = input(f'Select plot scale:')
        self.transparency = input(f'Select plot transparency:')
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
    def __init__(self, plot_type):
        super().__init__(plot_type)
        self.line_style = '-'
        self.line_width = 1
    
    def select_style(self):
        self.line_style = input(f'Select line style: ')
    def select_width(self):
        self.line_width = input(f'Select line width: ')
