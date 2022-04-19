import matplotlib.pyplot as plt
from utils.filesystem import ensure_dir_creation


class Plot:
    def __init__(self, style='ggplot', xlabel='U [mV]', ylabel='I [uA]', xlim=None, title=None):
        if xlim is None:
            xlim = [-500, 500]
        if title is None:
            title = ""
        self.style = style
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.to_plot = []

    def add_plot(self, results, label, thick=False):
        self.to_plot.append([results, label, thick])

    def set_up(self):
        plt.figure()
        plt.style.use(self.style)
        plt.title(self.title)

        has_legend = False
        for plot in self.to_plot:
            width = 1.5
            if plot[2]:
                width = 2.5
            if plot[1] is None:
                plt.plot(plot[0][0], plot[0][1], linewidth=width)
            else:
                plt.plot(plot[0][0], plot[0][1], label=plot[1], linewidth=width)
                has_legend = True

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.xlim(self.xlim[0], self.xlim[1])

        if has_legend:
            plt.legend()

    def show(self):
        self.set_up()
        plt.show()

    def save(self, filename):
        self.set_up()
        ensure_dir_creation(filename)
        plt.savefig(filename)