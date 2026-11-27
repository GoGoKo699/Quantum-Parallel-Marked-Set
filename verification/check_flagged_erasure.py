"""Check the five-address qutrit construction and the finite converses.

Run with Python 3.10 or later. All checks use integer or rational arithmetic.
"""

from fractions import Fraction
from itertools import combinations, permutations, product


def reduced_rows(rows):
    """Return the nonzero rows of the rational reduced row echelon form."""
    matrix = [list(map(Fraction, row)) for row in rows]
    pivot_count = 0
    for column in range(len(matrix[0])):
        pivot_index = next(
            (i for i in range(pivot_count, len(matrix)) if matrix[i][column]),
            None,
        )
        if pivot_index is None:
            continue
        matrix[pivot_count], matrix[pivot_index] = matrix[pivot_index], matrix[pivot_count]
        lead = matrix[pivot_count][column]
        pivot = [entry / lead for entry in matrix[pivot_count]]
        matrix[pivot_count] = pivot
        for i, row in enumerate(matrix):
            if i != pivot_count and row[column]:
                matrix[i] = [entry - row[column] * basis for entry, basis in zip(row, pivot)]
        pivot_count += 1
        if pivot_count == len(matrix):
            break
    return matrix[:pivot_count]


def parity_sign(addresses, difference):
    return (-1) ** sum(address in difference for address in addresses)


def tuple_sign(addresses):
    inversions = sum(left > right for left, right in combinations(addresses, 2))
    return (-1) ** inversions


def qutrit_tag(addresses):
    """Describe the vector a|A> + b|B> + c(|A>+sqrt(2) omega**f |C>)/sqrt(3)."""
    labels = set(addresses)
    if len(labels) == 1:
        return 0, 0, 0, 0
    if len(labels) == 2:
        majority, minority = sorted(labels, key=addresses.count, reverse=True)
        difference = (minority - majority) % 5
        return {
            1: (1, 0, 0, 0),
            2: (1, 0, 0, 0),
            3: (0, 1, 0, 0),
            4: (0, -1, 0, 0),
        }[difference]
    triple = tuple(sorted(addresses))
    offset = {
        (0, 1, 3): 1,
        (0, 1, 4): 2,
        (0, 2, 4): 1,
        (1, 2, 3): 1,
        (1, 3, 4): 2,
        (2, 3, 4): 1,
    }.get(triple, 0)
    sign = tuple_sign(addresses)
    exponent = (addresses.index(max(addresses)) + sign * offset) % 3
    return 0, 0, sign, exponent


def scaled_inner(left, right):
    """Represent 3 <left|right> by its coefficients in (1, sqrt(3), omega)."""
    a, b, c, f = left
    aa, bb, cc, ff = right
    # The three possible powers use omega^2 = -1 - omega.
    real, root = ((1, 0), (0, 1), (-1, -1))[(ff - f) % 3]
    return 3 * (a * aa + b * bb) + c * cc * (1 + 2 * real), a * cc + c * aa, 2 * c * cc * root


def insert_lost(surviving, port, lost_address):
    return surviving[:port] + (lost_address,) + surviving[port:]


def check_qutrit_protocol():
    """Check normalized preparation and all branch-support orthogonalities."""
    tags = {addresses: qutrit_tag(addresses) for addresses in product(range(5), repeat=3)}
    norm = sum(scaled_inner(tag, tag)[0] for tag in tags.values())
    assert norm == 3 * 120
    for port in range(3):
        for first_label, second_label in product(range(5), repeat=2):
            differences = [(), *combinations(range(5), 2)]
            for difference in differences:
                overlap = [0, 0, 0]
                for surviving in product(range(5), repeat=2):
                    first = tags[insert_lost(surviving, port, first_label)]
                    second = tags[insert_lost(surviving, port, second_label)]
                    sign = parity_sign(surviving, difference)
                    for i, coefficient in enumerate(scaled_inner(first, second)):
                        overlap[i] += sign * coefficient
                expected = 3 * 120 // 5 if not difference and first_label == second_label else 0
                assert overlap == [expected, 0, 0], (port, first_label, second_label, difference)
    print("Qutrit protocol: 750 cross-mark branch overlaps vanish and each port marginal is I/5.")


def check_five_address_converse_inputs():
    """Check the moment nullspace used in the no-register proof."""
    pairs = list(combinations(range(5), 2))
    parity_groups = [(), *pairs]
    moments = [
        [parity_sign(group, difference) for group in parity_groups]
        for difference in pairs
    ]
    single_port_weights = [2, *([1] * len(pairs))]
    assert len(reduced_rows(moments)) == 10
    assert all(sum(entry * weight for entry, weight in zip(row, single_port_weights)) == 0
               for row in moments)

    addresses = list(product(range(5), repeat=3))
    moments = [
        [int(t[port] == lost) * parity_sign(t[:port] + t[port + 1:], difference)
         for t in addresses]
        for port in range(3) for lost in range(5) for difference in pairs
    ]
    particular = [int(len(set(t)) > 1) for t in addresses]
    alternating = [
        [tuple_sign(t) if tuple(sorted(t)) == triple else 0 for t in addresses]
        for triple in combinations(range(5), 3)
    ]
    # These 11 independent vectors occupy all of the nullspace. The alternating
    # vectors have disjoint support and vanish on the repeated entries.
    assert len(reduced_rows(moments)) == len(addresses) - 1 - len(alternating)
    assert all(sum(entry * weight for entry, weight in zip(row, vector)) == 0
               for row in moments for vector in [particular, *alternating])
    print("Five-address converse: parity nullspace and forced repeated-entry weights verified.")


def check_six_addresses():
    """Check the negative orbit mass required by every feasible diagonal."""
    tuples = list(product(range(6), repeat=3))
    classes = [[t for t in tuples if len(set(t)) == k] for k in range(1, 4)]
    equations = [[1, 1, 1, 1]]
    for difference in ((0, 1), (1, 2)):
        row = [
            Fraction(sum(parity_sign(t[1:], difference) for t in group if t[0] == 0), len(group))
            for group in classes
        ]
        equations.append([*row, 0])
    result = reduced_rows(equations)
    assert [row[:3] for row in result] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    masses = [row[-1] for row in result]
    assert masses == [Fraction(-3, 32), Fraction(15, 32), Fraction(5, 8)]
    print("Six addresses: exact orbit masses force a negative probability.")


if __name__ == "__main__":
    check_qutrit_protocol()
    check_five_address_converse_inputs()
    check_six_addresses()
