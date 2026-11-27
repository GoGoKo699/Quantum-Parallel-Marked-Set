# From Watrous to exact marked-set recovery

**Educational anchor.** John Watrous, *The Theory of Quantum Information*, Cambridge University Press, 2018. [Author’s chapter downloads](https://cs.uwaterloo.ca/~watrous/TQI/) · [Publisher](https://doi.org/10.1017/9781316848142)

| Read | Carry into the project |
| --- | --- |
| §2.1, registers and states | Attach one register to each query port and a separate register to any stored workspace. Use §2.1.3 to expand a partial trace into lost-address branches. |
| §2.2, quantum channels | View a bare phase call as conjugation by a diagonal unitary. Use §2.2.2 to describe the erased port as the environment of the channel to the receiver. |
| §2.3, measurements | Construct a projective measurement onto mutually orthogonal output subspaces and include its complementary projector. |
| §3.1, quantum state discrimination | Apply the perfect-discrimination limit to the candidate states. Sections 3.1.1 and 3.1.2 connect pairwise distinguishability with the full family. |
| §7.1, permutation-invariant vectors and operators | Use orbit averaging on address labels, then track which symmetry components a known receiver preserves. |

The [30 milestones](MILESTONES.md) link these sections to the lossless results
and their flagged-erasure extension.

## Bare queries and exact discrimination

Each possible marked set $`A`$ labels a channel. Its unitary multiplies the
amplitude at an address $`a`$ by $`(-1)^{[a\in A]}`$. Every query port receives
one copy of this action in the same layer. A common phase cancels in unitary
conjugation, so complementary sets specify the same channel. A promised mark
count away from half the domain separates them.

For a four-address singleton example, start with the uniform address state
$`u=\frac{1}{2}\sum_{a=1}^{4}|a\rangle`$. The possible outputs are the four
states $`|u\rangle-|m\rangle`$. Their pairwise inner products are zero. The
fixed reflection $`2|u\rangle\langle u|-I`$ maps them to the four computational
basis states. This supplies a one-call preparation, a known measurement
circuit and a complete output. [Lossless model](../science/model.md)

## Parity and averaging

Only addresses queried an odd number of times contribute to the product of
oracle signs. For two marked sets, their output overlap is the average sign
from the odd-address subset and the symmetric difference of the sets.
Address-permutation averaging preserves all the required zero overlaps. It
leaves a probability weight for each accessible subset size, and paired
repeat queries fill any remaining ports. A coherent preparation realizes
the weights as squared amplitudes.

The layer overlap for each difference size is a normalized Krawtchouk
polynomial. Its even-degree terms turn the overlap conditions into positive
moment matching on the parity grid. The limiting binomial-square moments lead
to the fixed-mark query law. [Finite moment design](../science/moment-design.md) · [Asymptotics](../science/asymptotics.md)

## Symmetry and the decoder

The probe output is a sum of signed incidence maps from the promised
marked-set weight to each prepared layer. Each layer map commutes with
coordinate relabeling. The Schur basis resolves these permutation
representations. A known rotation brings the probe's magnetic vector back to
the promised weight, preserving the multiplicity amplitudes that carry the
mark information. Inverse transformation then gives the incidence string.
The finite moment conditions give the isometry property used by this
receiver. [Schur decoder](../science/receiver.md)

## From a lost port to branch supports

Tracing out a query port gives a positive sum of survivor branch projectors,
one for each value of the erased address. That value is hidden and the flag
identifies the port. The oracle sign on the hidden address cancels inside
each branch projector. Perfect discrimination of distinct marks requires
every branch vector for one mark to be orthogonal to every branch vector for
the other mark.

At five addresses with two survivors, group the ordered survivor pairs by
their parity subset. For one lost port, each parity class now carries a Gram
matrix on hidden addresses. The classical branch probabilities are its
diagonal entries. The two orders of a distinct survivor pair bound its Gram
rank by twice the protected tag dimension. The moment equations are enough
to force an explicit common Gram structure. [Gram identities](../science/flagged-erasure.md#the-gram-identities-at-five-addresses)

## The qutrit and coherent recovery

For each distinct survivor pair, the two rows with repeated addresses use
symmetric orientation vectors in two protected tag directions. An
antisymmetric orientation and a second phase-dependent component separate
the three distinct-address rows. With equal survivors, opposite signs cancel
the remaining collisions between branches. These choices give diagonal
single-port marginals and orthogonal mark supports.

The same probe therefore supports a coherent receiver on the span of the
queried mark states. Recovering every superposition forces the erased
subsystem's reduced state to be independent of the logical input. This is
where the requirement that the marginal be diagonal enters the lower bound.
A qutrit suffices and is optimal for this coherent task. The classical output
task permits off-diagonal marginals, and its qubit case remains open.
[Construction and coherent recovery](../science/flagged-erasure.md#a-qutrit-construction)

[Quantum Phase Gate Erasure](https://github.com/GoGoKo699/Quantum-Phase-Gate-Erasure/blob/main/science/flagged-search.md)
starts from the same partial-trace expansion. Its specified success channel
has a rank-one Choi operator, so every accepted branch must implement that
channel up to a scalar. Here the receiver instead uses orthogonal supports
for different candidate marks.
