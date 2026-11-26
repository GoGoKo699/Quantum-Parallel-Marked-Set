"""Check the exact layer conditions and the Schur multipliers on small instances.

Run with Python 3 and NumPy. The layer feasibility checks use rational
arithmetic. NumPy is used for numerical spectra of explicit Gram matrices.
"""

from fractions import Fraction
from itertools import combinations, product
from math import comb, sqrt

import numpy as np


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def krawtchouk(n, degree, weight):
    return sum(
        (-1) ** j * choose(weight, j) * choose(n - weight, degree - j)
        for j in range(degree + 1)
    )


def binomial_moments(n, degree):
    # The unscaled variable (n - 2k)^2 avoids a common denominator n.
    return [
        Fraction(sum(comb(n, k) * (n - 2 * k) ** (2 * j) for k in range(n + 1)), 2**n)
        for j in range(degree + 1)
    ]


def interpolated_weights(nodes, moments):
    weights = []
    for node in nodes:
        coefficients = [1]
        denominator = 1
        for other in nodes:
            if other == node:
                continue
            coefficients = [
                high - other * low
                for low, high in zip(coefficients + [0], [0] + coefficients)
            ]
            denominator *= node - other
        weights.append(sum(c * m for c, m in zip(coefficients, moments)) / denominator)
    return weights


def first_feasible(n, r):
    moments = binomial_moments(n, r)
    for queries in range(n):
        layers = {}
        for k in range(queries % 2, queries + 1, 2):
            layers.setdefault((n - 2 * k) ** 2, k)

        # A feasible distribution has a basic support of at most r+1 points.
        # Any smaller support can be extended by allowing zero weights.
        for nodes in combinations(sorted(layers), min(r + 1, len(layers))):
            weights = interpolated_weights(nodes, moments)
            if any(weight < 0 for weight in weights):
                continue
            if all(
                sum(weight * node**j for node, weight in zip(nodes, weights)) == moment
                for j, moment in enumerate(moments)
            ):
                support = [(layers[node], weight) for node, weight in zip(nodes, weights) if weight]
                return queries, support
    raise AssertionError(f"No feasible layer weights for N={n}, r={r}")


def multiplier_squared(n, r, k, j):
    if j > min(k, n - k):
        return Fraction(0)
    h, a, b = n - 2 * j, k - j, r - j
    return Fraction(
        4**j * comb(h, a) * krawtchouk(h, b, a) ** 2,
        comb(h, b) * comb(n, k),
    )


def check_feasible_minima():
    cases = 0
    for n in range(3, 31):
        for r in range(1, min(4, (n - 1) // 2) + 1):
            queries, layers = first_feasible(n, r)
            if r == 1:
                expected = 2 if n == 3 else next(
                    t for t in range(n) if 4 * t * (n - t) >= n * (n - 1)
                )
                assert queries == expected, (n, r, queries, expected)

            for j in range(1, r + 1):
                assert sum(w * krawtchouk(n, 2 * j, k) for k, w in layers) == 0
            for j in range(r + 1):
                assert sum(w * multiplier_squared(n, r, k, j) for k, w in layers) == 1

            if n in (9, 16, 25, 30):
                print(f"N={n:2}, r={r}, t={queries:2}: {[(k, str(w)) for k, w in layers]}")
            cases += 1
    return cases


def check_thirty_address_obstruction():
    n, queries = 30, 13
    low, middle, high = Fraction(8, 15), Fraction(24, 5), Fraction(128, 15)

    def polynomial(x):
        return (x - low) * (x - middle) * (x - high)

    allowed = [Fraction((n - 2 * k) ** 2, n) for k in range(1, queries + 1, 2)]
    assert all(polynomial(x) >= 0 for x in allowed)
    expectation = sum(
        Fraction(comb(n, k), 2**n) * polynomial(Fraction((n - 2 * k) ** 2, n))
        for k in range(n + 1)
    )
    assert expectation == Fraction(-54, 125)


def masks(n, weight, start=0):
    return [sum(1 << i for i in indices) for indices in combinations(range(start, n), weight)]


def pair_singlet_support(n, weight, j):
    support = []
    for choices in product((0, 1), repeat=j):
        paired = sum(1 << (2 * pair + side) for pair, side in enumerate(choices))
        sign = (-1) ** sum(choices)
        support.extend(
            (paired | residual, sign) for residual in masks(n, weight - j, start=2 * j)
        )
    return support


def check_signed_matrix_element(n, r, k, j):
    # Compare the unnormalized matrix element to preserve the sign information.
    target = pair_singlet_support(n, k, j)
    source = pair_singlet_support(n, r, j)
    actual = sum(
        target_sign * source_sign * (-1) ** (target_mask & source_mask).bit_count()
        for target_mask, target_sign in target
        for source_mask, source_sign in source
    )
    h, a, b = n - 2 * j, k - j, r - j
    expected = (-4) ** j * comb(h, a) * krawtchouk(h, b, a)
    assert actual == expected, (n, r, k, j, actual, expected)


def check_explicit_layers():
    spectra = 0
    signed_elements = 0
    for n in range(3, 9):
        for r in range(1, (n - 1) // 2 + 1):
            marks = masks(n, r)
            for k in range(n + 1):
                subsets = masks(n, k)
                matrix = np.array([
                    [(-1) ** (subset & mark).bit_count() for mark in marks]
                    for subset in subsets
                ]) / sqrt(len(subsets))
                expected = []
                for j in range(r + 1):
                    multiplicity = comb(n, j) - choose(n, j - 1)
                    expected.extend([float(multiplier_squared(n, r, k, j))] * multiplicity)
                    if j <= min(k, n - k):
                        check_signed_matrix_element(n, r, k, j)
                        signed_elements += 1

                np.testing.assert_allclose(
                    np.linalg.eigvalsh(matrix.T @ matrix), sorted(expected), atol=2e-12, rtol=0
                )
                spectra += 1
    return spectra, signed_elements


def main():
    check_thirty_address_obstruction()
    cases = check_feasible_minima()
    spectra, signed_elements = check_explicit_layers()
    print(f"Checked {cases} exact rational feasibility minima and {spectra} full Gram spectra.")
    print(f"Checked {signed_elements} signed Schur matrix elements by exact enumeration.")


if __name__ == "__main__":
    main()
