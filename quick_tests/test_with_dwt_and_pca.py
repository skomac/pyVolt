import dwt_test
import numpy as np

from quick_tests.pca_poc import pca_analysis


def main():
    normalized_coefficients_data = dwt_test.main()
    print("dwt/pca test entry")
    print(np.shape(normalized_coefficients_data))
    pca_analysis(normalized_coefficients_data)
    pass


if __name__ == '__main__':
    main()