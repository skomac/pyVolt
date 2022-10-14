import matplotlib.pyplot as plt
import numpy as np

from utils.filesystem import ensure_dir_creation


class Plot:
    def __init__(self, style='ggplot', xlabel='E [V]', ylabel='I [μA]', xlim=None, title=None, dotted=False, markersize=10., figsize=None):
        if xlim is None:
            xlim = [-0.501, 0.501]
        if title is None:
            title = ""
        if figsize is None:
            figsize = [6.4, 4.8]
        self.style = style
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.to_plot = []
        self.dotted = dotted
        self.markersize = markersize
        self.figsize = figsize

    def add_plot(self, results, label, thick=False):
        results_copy = np.copy(results)
        results_copy[0] = results_copy[0]*0.001
        self.to_plot.append([results_copy, label, thick])

    def set_up(self):
        plt.figure(tight_layout=True, figsize=self.figsize)
        plt.style.use(self.style)
        plt.title(self.title)

        has_legend = False
        for plot in self.to_plot:
            width = 1.5
            if plot[2]:
                width = 2.5
            if plot[1] is None:
                if self.dotted:
                    plt.plot(plot[0][0], plot[0][1], 'o', markersize=self.markersize)
                else:
                    plt.plot(plot[0][0], plot[0][1], linewidth=width)
            else:
                if self.dotted:
                    plt.plot(plot[0][0], plot[0][1], 'o',  label=plot[1], markersize=self.markersize)
                else:
                    plt.plot(plot[0][0], plot[0][1], label=plot[1], linewidth=width)
                has_legend = True

        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        # plt.xlim(self.xlim[0], self.xlim[1])

        if has_legend:
            plt.legend()

    def show(self):
        self.set_up()
        plt.show()

    def save(self, filename):
        self.set_up()
        ensure_dir_creation(filename)
        plt.savefig(filename)