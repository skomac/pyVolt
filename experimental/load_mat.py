import numpy as np
import scipy.io

from utils.plot import Plot


def import_juices():
    directory = '/data/mgrProject/pyVolt/experimental/'

    names = [
             'Auchan1',
             # 'Auchan2',
             'ChampionK',
             # 'Cymes',
             'Fortuna',
             # 'Fortunam',
             # 'Hipp',
             'Hortex',
             'LigolK',
             'LigolW',
             'ONatury',
             # 'PrincK',
             'PrincW',
             # 'Tymbark1',
             'Tymbark2',
             'Tymbark3',
             'Wosana'
             ]

    raw_data = []

    plot_samples = Plot(title="Przykładowe rzeczywiste sygnały dla soków jabłkowych")
    # names_legend = ['Auchan', 'Auchan2', 'Cymes', 'Fortuna', 'Hortex', 'Tymbark']
    names_legend = names

    for i, name in enumerate(names):
        raw_data.append([])
        filename = f"Ir_{name}.mat"
        keyA = f"Ir{name}A"
        keyK = f"Ir{name}K"

        data = scipy.io.loadmat(directory + filename)
        # print(data[keyA])
        # print(data[keyK])
        # print(data['xa'])
        # print(data['xk'])
        # print(data['y'])
        print(filename)

        for j, curve in enumerate(data['xa']):
            if data['y'][j] == 0 :
                print(np.shape(data[keyA][0]))
                print(np.shape(curve))
                raw_data[i].append([data[keyA][0], curve])
                if j == 0:
                    plot_samples.add_plot([data[keyA][0], curve], names_legend[i])

    plot_samples.show()

    print("out of data")
    print(np.shape(raw_data))
    plot = Plot()
    for suite in raw_data:
        for curve in suite:
            plot.add_plot(curve, "a")
    # plot.show()
    return raw_data


# ir_auchan1 = scipy.io.loadmat('Ir_Auchan1.mat')
#
# # print(ir_auchan1)
# print(ir_auchan1['IrAuchan1A'])
# print(ir_auchan1['IrAuchan1K'])
# print(ir_auchan1['xa'])
# print(ir_auchan1['xk'])
# print(ir_auchan1['y'])

# ir_auchan2 = scipy.io.loadmat('Ir_Auchan2.mat')

# print(ir_auchan2)
# print(ir_auchan2['IrAuchan2A'])
# print(ir_auchan2['IrAuchan2K'])
# print(ir_auchan2['xa'])
# print(ir_auchan2['xk'])
# print(ir_auchan2['y'])

# ir_championK = scipy.io.loadmat('Ir_ChampionK.mat')
#
# print(ir_championK)
# print(ir_championK['IrChampionKA'])
# print(ir_championK['IrChampionKK'])
# print(ir_championK['xa'])
# print(ir_championK['xk'])
# print(ir_championK['y'])


# ir_hipp = scipy.io.loadmat('Ir_Hipp.mat')
#
# print(ir_hipp)
# print(ir_hipp['IrHippA'])
# print(ir_hipp['IrHippK'])
# print(ir_hipp['xa'])
# print(ir_hipp['xk'])
# print(ir_hipp['y'])

if __name__ == '__main__':
    import_juices()
