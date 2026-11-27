# From Childs's quantum algorithms notes to one-round marked-set recovery

**Supplementary reading.** Andrew M. Childs, *Lecture Notes on Quantum Algorithms*, version dated 17 April 2025. [Author's page](https://www.cs.umd.edu/~amchilds/qa/) · [Full notes](https://www.cs.umd.edu/~amchilds/qa/qa.pdf)

Read the query model first, then use the sections below as each part of the project calls for them. The [Watrous bridge](WATROUS_BRIDGE.md) and [milestone map](MILESTONES.md) provide the main learning route.

| Read | Carry into the project |
|---|---|
| §§21.1–21.2, quantum query complexity and quantum queries | Separate unknown oracle operations from known circuits. In the bare-phase discussion just after Eq. (21.3), Childs identifies the complement ambiguity that determines this project's promise. |
| §§21.3–21.4, polynomials and symmetrization | Follow the phase-as-sign argument and the averaging over coordinate permutations. Here the quantities being averaged are the overlaps between two candidate outputs. |
| §19.1, unstructured search | Recall Grover's sequential use of a marked reflection and a known reflection, its query scale for finding one mark, and the role of intermediate operations. |
| §§11.1 and 15.1–15.2, representation theory and Schur decomposition | Read Schur's lemma and the decomposition under collective rotations and tensor-factor permutations. Observe what information is retained when weak Schur sampling measures only the representation label. |
| §§1.2–1.5 and §2.1, circuits, reversibility, uniformity and approximation | Track how a known preparation and uncomputation enter the circuit. Use the error accumulation bound to translate ideal rotations into finite-precision implementations. |

## The oracle access and output

Childs writes $`x_i`$ for a bit of an unknown string. Here $`x_i=1`$ means that address $`i`$ is in the marked set $`A`$, and the input promise gives $`|A|=r`$. The project returns the entire string, equivalently the complete set $`A`$. Childs's bit-response oracle can yield a phase by putting its response qubit in the appropriate eigenstate. The project receives the resulting bare action directly.

```math
O_A\lvert i\rangle=(-1)^{[i\in A]}\lvert i\rangle .
```

The address register ranges over exactly $`N`$ allowed indices. In Childs's richer phase interface the zero response provides an input-independent eigenvalue. Here every branch passes through each of the $`t`$ supplied ports. Complementing $`A`$ multiplies the entire action by $`-1`$ and leaves its channel unchanged. When $`r=N/2`$, both complements satisfy the promise and cannot be distinguished. When $`r\lt N/2`$, only one complement has the supplied weight.

In §19.1 the unknown reflection occurs in a sequence with a known reflection between uses. The present unknown layer is $`O_A^{\otimes t}`$, and the known operations occur before and after it. Here $`t`$ counts simultaneously available invocations. Preparation, address routing, decoding and measurement add their own gate costs. [Model and results](../science/model.md)

## From phase signs to probe weights

On an address tuple the phase signs multiply. Every address visited an even number of times contributes $`+1`$. Let $`S`$ be the set visited an odd number of times. If two marked sets $`A,B`$ are possible, their output overlap for a given probe is

```math
\langle\psi_A\mid\psi_B\rangle
=\mathbb E_{S}\!\left[(-1)^{\lvert S\cap(A\mathbin{\triangle}B)\rvert}\right].
```

The probability of $`S`$ in this formula is the sum of squared input amplitudes for all tuples and ancillary components with that parity set. Each overlap must vanish for exact discrimination. Permuting addresses and averaging preserves that linear condition. After averaging, the probability depends only on $`k=|S|`$, and each size-$`k`$ subset is equally likely within its layer. The available sizes satisfy $`k\le t`$ and $`k\equiv t\pmod 2`$. One can realize any such layer coherently. Query the members of $`S`$ once and fill the remaining ports with pairs of repeated addresses. Both calls in each pair count.

For a symmetric difference of size $`2j`$, the signed overlap on layer $`k`$ is a Krawtchouk polynomial in $`k`$ divided by a known combinatorial factor. The degrees $`0,2,\ldots,2r`$ form a basis for polynomials of degree at most $`r`$ in $`X=(N-2k)^2/N`$. A uniformly random subset gives zero for each nonconstant sign average, so its binomial size law supplies the target moments. Exact design amounts to reproducing those moments with nonnegative weights on the available parity grid. This is the project's counterpart to the symmetrization in Childs §21.4, where the notes average a polynomial in an unknown string over permuted coordinates. [Finite moment design](../science/moment-design.md)

### A complete four-address circuit

Let $`N=4`$ and let $`j`$ be the one marked address. Prepare the uniform state $`|u\rangle=\tfrac12\sum_{i=1}^4|i\rangle`$. One phase call produces $`|u\rangle-|j\rangle`$. The fixed reflection $`2|u\rangle\langle u|-I`$ sends this to $`|j\rangle`$, so measuring the address returns the mark. In the parity description $`t=k=1`$. For two candidate marks the symmetric difference has size two, and exactly two of the four singleton subsets produce a minus sign. This explains the zero overlap before applying the readout reflection.

At $`N=6`$ the two-call solution uses two layers. A uniform pair intersects a given two-element difference in exactly one member for eight of the fifteen pairs. Its overlap is therefore $`-1/15`$. A repeated-address tuple realizes $`S=\varnothing`$, with overlap $`+1`$. Use squared amplitudes $`15/16`$ and $`1/16`$ for the two layers. Their signed contributions cancel, while every branch uses two calls. The cancellation concerns the overlap of coherent joint states. Selecting a layer by classical sampling and exposing that choice would give a different readout problem. [Finite moment design](../science/moment-design.md) · [General coherent receiver](../science/receiver.md)

## How the moment problem gives a query law

The smallest allowed $`X`$ limits the moments that the probe weights can reproduce. A nonnegative polynomial of the form $`(X-L)q(X)^2`$ on nodes $`X\ge L`$ gives a constraint on $`L`$, because its mean must agree with the binomial target. Minimizing the resulting Rayleigh quotient finds the smallest Gaussian quadrature node. The matching construction builds positive weights on the actual parity grid. It brackets the nearby quadrature nodes, and for even $`r`$ it also uses a far endpoint. The construction and its positivity argument are supplied by the project. In the fixed-$`r`$ limit the standardized binomial square approaches the chi-square law with one degree of freedom, which links the smallest node to a generalized Laguerre zero. [Fixed-weight asymptotics](../science/asymptotics.md)

## How a coherent Schur receiver recovers the full set

Childs §15.1 separates the action of collective qubit rotations from the permutation action on the $`N`$ positions. In this project, the fixed size of a subset fixes a magnetic label within each compatible spin sector. The phase map between weight spaces commutes with position permutations. It acts on each shared permutation representation by a scalar between its two magnetic labels and preserves its multiplicity coordinate. Thus the unknown marked set determines the representation amplitudes, while a known vector across magnetic labels describes the query's layer response.

The decoder transforms the incidence register into the Schur basis, applies a spin-controlled rotation of each known layer vector to the magnetic label for weight $`r`$, and inverts the Schur transform. A computational-basis measurement reads the marked incidence string. All coherent representation registers survive until the inverse transform. Measuring the spin label alone, as in weak Schur sampling in §15.2, retains only that label. The finite moment design provides the normalization that makes the decoder exact with ideal gates. Basis transforms, address logic, and rotation synthesis remain separate known resources even though there is one oracle layer. [Schur receiver and resources](../science/receiver.md)
