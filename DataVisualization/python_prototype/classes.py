class Plot:
    def __init__(self, plot_type):
        self.plot_type = plot_type
        self.color = 'pastel'

    def select_color(self):
        color = input(f'Select plot color:')
        self.color = color