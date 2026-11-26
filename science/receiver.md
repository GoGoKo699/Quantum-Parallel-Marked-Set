# A Schur-transform receiver

Fix the number of marks $`1\le r \lt N/2`$ and write $`A\subseteq[N]`$ for the unknown marked set. The protocol prepares a superposition of subset sizes, applies one parallel layer of bare phase calls, and decodes the resulting incidence register. The decoder uses known controlled rotations and the spin Schur transform. Its output is the incidence string of $`A`$.

## Prepare the probe and route the calls

Let $`w_k`$ be feasible layer weights for an available call budget $`t`$. On an $`N`$-qubit incidence register, prepare

```math
\sum_k \sqrt{w_k}\,|D_k\rangle,
\qquad
|D_k\rangle=\frac{1}{\sqrt{\binom Nk}}\sum_{|S|=k}|S\rangle.
```

One preparation uses the inverse Schur transform. Set the total spin to $`N/2`$, set its unique multiplicity label, and prepare the known magnetic-label superposition with amplitude $`\sqrt{w_k}`$ at $`m=k-N/2`$.

The protocol uses $`t`$ fresh address registers. A reversible scan of the incidence bits writes the addresses in $`S`$ in increasing order. Initialize all address registers to a fixed valid address, encoded as all zeros, and leave the last $`t-k`$ registers at that address. This count is even, so the phases from those registers multiply to one for every $`A`$, including sets that contain the padding address. Every address register receives one call to the same phase oracle $`O_A`$ in the parallel layer. Inverting the scan clears the address registers and its work registers. The remaining state is

```math
M|A\rangle:=\sum_k \sqrt{w_k}\,M_{k,r}|A\rangle,
\qquad
M_{k,r}|A\rangle=\frac{1}{\sqrt{\binom Nk}}
\sum_{|S|=k}(-1)^{|S\cap A|}|S\rangle.
```

Here $`M_{k,r}`$ is a linear map from the weight-$`r`$ subspace to the weight-$`k`$ subspace. The weight-$`r`$ ket in the formula labels an input column. The protocol prepares only the probe.

## Compute the effect on the Schur labels

Use the spin convention in which a $`1`$ increases the magnetic label. In the tensor product of $`N`$ spin-$`1/2`$ systems, let $`j`$ denote the spin defect, so the total spin is $`J=N/2-j`$. The weight-$`k`$ permutation representation contains one copy of each two-row irreducible representation $`(N-j,j)`$ with $`0\le j\le\min(k,N-k)`$. In Schur coordinates, that copy has fixed magnetic label $`k-N/2`$ and a multiplicity register carrying the permutation representation.

Each $`M_{k,r}`$ commutes with simultaneous coordinate relabeling of its rows and columns. Schur's lemma gives a scalar action on each common irreducible representation, after identifying the multiplicity spaces using the same Schur basis at both magnetic labels. The map acts as zero on source irreducible representations that are absent at weight $`k`$.

For the common representations, set $`h=N-2j`$, $`a=k-j`$ and $`b=r-j`$. The scalar is

```math
f_j(k,r)=(-2)^j
\sqrt{\frac{\binom{h}{a}}{\binom{h}{b}\binom Nk}}
K_b^{(h)}(a),
\qquad
K_b^{(h)}(a)=\sum_{\ell=0}^b(-1)^\ell\binom{a}{\ell}\binom{h-a}{b-\ell}.
```

To evaluate it, take $`j`$ disjoint pairs in the normalized singlet $`(|10\rangle-|01\rangle)/\sqrt{2}`$ and place the other $`h`$ coordinates in a symmetric Dicke state. The source and target use residual weights $`b`$ and $`a`$. These vectors have the same multiplicity direction. The collective spin raising operator annihilates the singlets and acts with positive Dicke ladder coefficients on the other coordinates, fixing the relative magnetic phases used in this calculation.

In the matrix element of $`M_{k,r}`$, each pair contributes $`-2`$. For each of the four choices of source and target pair strings, the product of the two singlet signs and the intersection phase is $`-1`$, and the normalization contributes $`1/2`$. On the remaining coordinates, each fixed target subset of size $`a`$ gives the source sum $`K_b^{(h)}(a)`$. There are $`\binom{h}{a}`$ such target subsets. Dividing by the two Dicke normalizations and the column normalization of $`M_{k,r}`$ gives the displayed scalar.

## Decode the marked set

In the Schur basis, on the source spin defect $`j`$, the map $`M`$ replaces the source magnetic basis state by the vector

```math
|v_j\rangle=\sum_k\sqrt{w_k}\,f_j(k,r)|k-N/2\rangle
```

and leaves the multiplicity vector unchanged. The moment conditions give $`M^\dagger M=I`$ on the weight-$`r`$ label space, so every $`|v_j\rangle`$ in that space has norm one. Different source labels can occupy the same spin sector and are distinguished by the multiplicity register. The decoder therefore applies the Schur transform, applies a known unitary controlled by $`j`$ that sends $`|v_j\rangle`$ to $`|r-N/2\rangle`$ with the displayed signs, and applies the inverse Schur transform. This gives exactly $`|A\rangle`$. Measuring the incidence register yields all marked addresses.

## Circuit resources and precision

- **Calls and width.** The oracle layer contains exactly $`t`$ calls on disjoint address registers of $`\lceil\log_2N\rceil`$ qubits each. The incidence register, Schur labels and work registers can be arranged using $`O(N+t\log(N+1))`$ qubits in total, including addresses. Work internal to the physical oracle is an interface cost.
- **Address routing.** A reversible counter tracks the number of set bits already scanned. At each position, conditioned on its incidence bit and the counter, XOR the known address into the designated output word, starting from the fixed padding address. A direct compilation iterates over all $`t`$ counter values at each of the $`N`$ positions. Equality tests, controlled increments and bitwise writes give a conservative bound of $`O(Nt\log^2(N+1))`$ known elementary gates, including reversal. This route uses no external address lookup.
- **Schur rotations.** The qubit Schur circuit follows the sequential spin-$`1/2`$ Clebsch–Gordan decomposition. At step $`s`$ there are $`O(s^2)`$ possible spin and magnetic labels, with at most a two-dimensional rotation per block. Enumerating the blocks and compiling their controlled rotations gives an exact $`O(N^3\mathrm{polylog}(N+1))`$ gate upper bound over arbitrary one-qubit rotations and reversible Boolean gates. The intermediate coupling choices use $`O(N)`$ bits. The final $`j`$-controlled magnetic rotations use known two-level rotations on $`O(N)`$-dimensional blocks. Feasible weights need at most $`r+1`$ layers, and the same rotations prepare the input magnetic superposition.
- **Gate precision.** The exact query result assumes exact known rotations. With a finite universal gate set, synthesize the known circuit with total operator-norm error at most $`\eta`$, for example by assigning each of $`G`$ known gates a budget of $`\eta/G`$. With exact oracle calls, the final probability of an incorrect incidence string is at most $`\eta^2`$ for every $`A`$. The query count stays at $`t`$, while the synthesis increases the known gate cost. The algorithm has one oracle layer, with known gates before and after that layer.

The transform is the change of basis described by Bacon, Chuang and Harrow. The magnetic rotation used here is determined by the signed intersection kernel of the search problem. [Efficient Quantum Circuits for Schur and Clebsch–Gordan Transforms](https://arxiv.org/abs/quant-ph/0407082)
