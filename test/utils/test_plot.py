import unittest
from unittest.mock import MagicMock

import matplotlib.pyplot as plt

from utils.plot import Plot


class TestPlot(unittest.TestCase):
    def test_set_up_default_values(self):
        plt.figure = MagicMock()
        plt.style.use = MagicMock()
        plt.plot = MagicMock()
        plt.xlabel = MagicMock()
        plt.ylabel = MagicMock()
        plt.xlim = MagicMock()
        plt.legend = MagicMock()

        Plot().set_up()

        plt.figure.assert_called_once_with()
        plt.style.use.assert_called_once_with('ggplot')
        plt.plot.assert_not_called()
        plt.xlabel.assert_called_once_with('Potential [V]')
        plt.ylabel.assert_called_once_with('Current [uA]')
        plt.xlim.assert_called_once_with(-0.5, 0.5)
        plt.legend.assert_called_once_with()
