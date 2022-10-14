import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize, StandardScaler

from utils.plot import Plot

from timeit import default_timer as timer


def pca_analysis(data, suite_names):
    no_dims = np.shape(data)[3]
    no_plots_in_suite = np.shape(data)[1]
    no_suites = np.shape(data)[0]

    # plot = Plot(ylabel="A")

    mixed_data = []
    samples_data_normalized = []
    for suite_id, suite_data in enumerate(data):
        for i, curve in enumerate(suite_data):
            mixed_data.append(curve[1])
            if i == 1:
                normalized = np.copy(curve)
                normalized[1] = normalized[1] - np.average(normalized[1])
                normalized[1] = normalize([normalized[1]], norm='l2')[0]
                samples_data_normalized.append(normalized)
                # plot.add_plot(normalized, suite_names[suite_id])

    print(np.shape(data))
    print(np.shape(mixed_data))

    pca = PCA(n_components=2, svd_solver="full")
    pca.fit(mixed_data)
    print(pca.svd_solver)
    print(pca.singular_values_)
    print(pca.explained_variance_)
    print(pca.explained_variance_ratio_)

    component_data = []
    for i, component in enumerate(pca.components_):
        print(f"shapeX:{np.shape(np.copy(data[0][0][0]))}")
        print(f"shapeY:{np.shape(component)}")
        print(np.shape(np.array([np.copy(data[0][0][0]), component])))
        # plot.add_plot(np.array([np.arange(-500, 500, 1), component]), f"PC{i}")
        component_data.append([np.copy(data[0][0][0]), component])
        # component_data.append([np.copy(mixed_data[0][0]), component])

    # plot.show()

    transformed = pca.transform(mixed_data)

    # cluster_plot = Plot(xlabel="PC1", ylabel="PC2", xlim=[-1, 1], dotted=True)

    # names = ['Auchan', 'Cymes', 'Fortuna', 'Hortex', 'Tymbark']

    cluster_data = []
    for i in range(0, no_suites):
        i_min = i * no_plots_in_suite
        i_max = i_min + no_plots_in_suite
        # cluster_plot.add_plot([transformed[i_min:i_max, 0], transformed[i_min:i_max, 1]], f"{names[i]}")
        # cluster_plot.add_plot([transformed[i_min:i_max, 0], transformed[i_min:i_max, 1]], f"{i}")
        cluster_data.append(np.array([transformed[i_min:i_max, 0], transformed[i_min:i_max, 1]]))

    # cluster_plot.show()

    return {"samples_data_normalized": samples_data_normalized, "component_data": component_data,
            "cluster_data": cluster_data, "explained_variance": pca.explained_variance_ratio_}


def pca_assessment(raw, preprocessed, cfg, suite_names):
    # assess raw, preprocessed
    results_raw = pca_analysis(raw, suite_names)
    results_preprocessed = pca_analysis(preprocessed, suite_names)
    return [results_raw, results_preprocessed]
