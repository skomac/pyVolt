import unittest

import numpy as np

from utils.math import get_gram_polynomial


class TestGramPolynomials(unittest.TestCase):
    def when_mk(self, m, k):
        self.result = get_gram_polynomial(m, k)

    def expect(self, expected_polynomial):
        np.testing.assert_allclose(self.result, expected_polynomial, rtol=0.0001, atol=0)

    def test_getPolynomial_0_minus1(self):
        self.when_mk(0, -1)
        self.expect([])

    def test_getPolynomial_0_0(self):
        self.when_mk(0, 0)
        self.expect([1.])

    def test_getPolynomial_1_1(self):
        self.when_mk(1, 1)
        self.expect([1., 0.])

    def test_getPolynomial_3_1(self):
        self.when_mk(3, 1)
        self.expect([1. / 3., 0.])

    def test_getPolynomial_3_2(self):
        self.when_mk(3, 2)
        self.expect([1. / 5., 0., -4. / 5.])

    def test_getPolynomial_5_0(self):
        self.when_mk(5, 0)
        self.expect([1])

    def test_getPolynomial_5_1(self):
        self.when_mk(5, 1)
        self.expect([1./5., 0])

    def test_getPolynomial_5_2(self):
        self.when_mk(5, 2)
        self.expect([1./15., 0., -2./3.])

    def test_getPolynomial_5_3(self):
        self.when_mk(5, 3)
        self.expect([1./36., 0., -10./36.-13./60., 0.])


if __name__ == '__main__':
    unittest.main()
