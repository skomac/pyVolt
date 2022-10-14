import sklearn
from matplotlib import pyplot as plt

from evaluation.evaluate import load_data, preprocess_all
from evaluation.pca_evalutation import pca_assessment
from experimental.load_mat import import_juices
from results.results import results_eval_dir
from utils.filesystem import save_csv_dict

from timeit import default_timer as timer

import numpy as np
from sklearn.decomposition import PCA

from utils.plot import Plot


def pca_analysis(data):
    print("PCA")
    print(f"Data dimensions: {np.shape(data)}")

    no_dims = np.shape(data)[3]
    no_plots_in_suite = np.shape(data)[1]
    no_suites = np.shape(data)[0]

    plot = Plot(xlim=[0, no_dims])

    mixed_data = []
    mixed_solution = []
    for suite_id, suite_data in enumerate(data):
        for i, curve in enumerate(suite_data):
            # if i >= no_dims: #really?
            #     break
            mixed_data.append(curve[1])
            mixed_solution.append(suite_id)
            if i == 1:
                plot.add_plot(curve, f"curve-{suite_id}-{i}")

    print(np.shape(mixed_data))
    print(np.shape(mixed_solution))

    pca = PCA(n_components=2, svd_solver="full")
    start = timer()
    pca.fit(mixed_data)
    end = timer()
    print(f"Time in seconds: {end-start}")
    print(pca)
    print(pca.n_components)
    print(pca.svd_solver)
    print(pca.singular_values_)
    # print(pca.components_)
    print(pca.explained_variance_)
    print(pca.explained_variance_ratio_)

    for i, component in enumerate(pca.components_):
        plot.add_plot(np.array([np.arange(0, no_dims), component]), f"component-{i}")

    plot.show()

    transformed = pca.transform(mixed_data)

    # proposed_solution = np.argmax(transformed, 1)
    # for expected, actual in zip(mixed_solution, proposed_solution):
    #     print(expected, actual)

    print("Transformed:")
    print(np.shape(transformed))

    # cluster_plot = Plot(xlim=[-1, 1])
    cluster_plot = Plot(xlabel = "PC1", ylabel="PC2", xlim=[-1, 1], dotted=True)

    names = ['Auchan', 'Cymes', 'Fortuna', 'Hortex', 'Tymbark']

    # for i in range(0, no_suites):
    #     i_min = i * no_plots_in_suite
    #     i_max = i_min + no_plots_in_suite
    #     cluster_plot.add_plot([transformed[i_min:i_max, 0], transformed[i_min:i_max, 1]], f"{names[i]}")

    cluster_plot.show()

    # cluster_plot.add_plot([transformed[0:no_plots_in_suite, 0], transformed[0:no_plots_in_suite, 1]], "clusters")
    # cluster_plot.show()
    #
    # cluster_plot.add_plot([transformed[no_plots_in_suite:2*no_plots_in_suite, 0], transformed[no_plots_in_suite:2*no_plots_in_suite, 1]], "clusters")
    # cluster_plot.show()
    #
    # cluster_plot.add_plot([transformed[2*no_plots_in_suite:3*no_plots_in_suite, 0], transformed[2*no_plots_in_suite:3*no_plots_in_suite, 1]], "clusters")
    # cluster_plot.show()

    # cluster_plot.add_plot([transformed[:, 0], transformed[:, 1]], "clusters")
    cluster_plot.show()

    # transformed.append([0, 0])
    retransformed = pca.inverse_transform(transformed)
    zero_retransformed = pca.inverse_transform([0,0])

    plot = Plot(xlim=[0, no_dims])
    for i, curve in enumerate(retransformed):
        plot.add_plot(np.array([np.arange(0, no_dims), curve]), f"retransformed: {i}")
        print(i)
    plot.add_plot(np.array([np.arange(0, no_dims), zero_retransformed]), f"retransformed: {i}")

    plot.show()

    plot2 = Plot(xlim=[0, no_dims])

    for i, component in enumerate(pca.components_):
        X = np.zeros(np.size(pca.components_, 0))
        X[i] = 1
        print(X)
        single_component = pca.inverse_transform(X)
        plot2.add_plot(np.array([np.arange(0, no_dims), single_component]), f"component-{i}")

    plot2.show()
    # save_csv_dict(pca_assessment(data, preprocessed, None),
    #               f"{results_eval_dir}/pca_poc")


def sample_pca():
    # initial_data = [
    #     "pca_sample_dataset_0",
    #     "pca_sample_dataset_1",
    #     "pca_sample_dataset_2"
    # ]
    #
    # data = load_data(initial_data)

    data = import_juices()

    print(np.shape(data))

    preprocessing_instructions = [
        [
            "SAVITZKY_GOLAY",
            17,
            2
        ],
        [
            "POLYNOMIAL_BASELINE",
            0.1,
            0.8,
            3
        ],
        # [
        #     "REDUCE_DIMENSIONALITY_AVERAGING",
        #     20
        # ],
        [
            "NORMALIZE"
        ]
    ]

    preprocessed = preprocess_all(data, preprocessing_instructions, "preparing")

    # averaged = reduce_dim_averaging(data, 35)
    # normalized = normalize_data(preprocessed)
    pca_analysis(preprocessed)


if __name__ == '__main__':
    sample_pca()