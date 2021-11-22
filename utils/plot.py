import matplotlib.pyplot as plt
from utils.filesystem import ensure_dir_creation


class Plot:
    def __init__(self, style='ggplot', xlabel='Potential [V]', ylabel='Current [uA]', xlim=None):
        if xlim is None:
            xlim = [-0.5, 0.5]
        self.style = style
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.to_plot = []

    def add_plot(self, results, label):
        self.to_plot.append([results, label])

    def set_up(self):
        plt.figure()
        plt.style.use(self.style)

        for plot in self.to_plot:
            plt.plot(plot[0][0], [i * 1.0e6 for i in plot[0][1]], label=plot[1])

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.xlim(self.xlim[0], self.xlim[1])
        plt.legend()

    def show(self):
        self.set_up()
        plt.show()

    def save(self, filename):
        self.set_up()
        ensure_dir_creation(filename)
        plt.savefig(filename)